# (C) Datadog, Inc. 2019
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import yaml


class ConfigSpec(object):
    def __init__(self, contents, integration=None):
        self.contents = contents
        self.integration = integration
        self.data = None
        self.errors = []
        self.warnings = []
        self.messages = []

    def load(self):
        """
        This function de-serializes the specification and:

        1. fills in default values
        2. populates any selected templates
        3. accumulates all error/warning messages
        """
        try:
            self.data = yaml.safe_load(self.contents)
        except Exception as e:
            self.errors.append('{}: Unable to parse the configuration specification: {}'.format(self.integration, e))
            return

        if not isinstance(self.data, dict):
            self.errors.append('{}: Configuration specifications must be a mapping object'.format(self.integration))
            return

        if 'files' not in self.data:
            self.errors.append(
                '{}: Configuration specifications must contain a top-level `files` attribute'.format(self.integration)
            )
            return

        files = self.data['files']
        if not isinstance(files, list):
            self.errors.append('{}: The top-level `files` attribute must be an array'.format(self.integration))
            return

        file_names_origin = {}
        example_file_names_origin = {}
        for file_index, config_file in enumerate(files, 1):
            if not isinstance(config_file, dict):
                self.errors.append(
                    '{}, file #{}: File attribute must be a mapping object'.format(self.integration, file_index)
                )
                continue

            if 'name' not in config_file:
                self.errors.append(
                    '{}, file #{}: Every file must contain a `name` attribute representing the '
                    'final destination the Agent loads'.format(self.integration, file_index)
                )
                continue

            file_name = config_file['name']
            if not isinstance(file_name, str):
                self.errors.append(
                    '{}, file #{}: Attribute `name` must be a string'.format(self.integration, file_index)
                )

            if file_name in file_names_origin:
                self.errors.append(
                    '{}, file #{}: File name `{}` already used by file #{}'.format(
                        self.integration, file_index, file_name, file_names_origin[file_name]
                    )
                )
            else:
                file_names_origin[file_name] = file_index

            if file_name == 'auto_conf.yaml':
                if 'example_name' in config_file and config_file['example_name'] != file_name:
                    self.errors.append(
                        '{}, file #{}: Example file name `{}` should be `{}`'.format(
                            self.integration, file_index, config_file['example_name'], file_name
                        )
                    )

                example_file_name = config_file.setdefault('example_name', file_name)
            else:
                expected_name = '{}.yaml'.format(self.integration or 'conf')
                if file_name != expected_name:
                    self.errors.append(
                        '{}, file #{}: File name `{}` should be `{}`'.format(
                            self.integration, file_index, file_name, expected_name
                        )
                    )

                example_file_name = config_file.setdefault('example_name', 'conf.yaml.example')

            if not isinstance(example_file_name, str):
                self.errors.append(
                    '{}, file #{}: Attribute `example_name` must be a string'.format(self.integration, file_index)
                )

            if example_file_name in example_file_names_origin:
                self.errors.append(
                    '{}, file #{}: Example file name `{}` already used by file #{}'.format(
                        self.integration, file_index, example_file_name, example_file_names_origin[example_file_name]
                    )
                )
            else:
                example_file_names_origin[example_file_name] = file_index

            if 'sections' not in config_file:
                self.errors.append(
                    '{}, {}: Every file must contain a `sections` attribute containing things like '
                    '`init_config`, `instances`, etc.'.format(self.integration, file_name)
                )
                continue

            sections = config_file['sections']
            if not isinstance(sections, list):
                self.errors.append(
                    '{}, {}: The `sections` attribute must be an array'.format(self.integration, file_name)
                )
                continue

            section_names_origin = {}
            for section_index, section in enumerate(sections, 1):
                if not isinstance(section, dict):
                    self.errors.append(
                        '{}, {}, section #{}: Section attribute must be a mapping object'.format(
                            self.integration, file_name, section_index
                        )
                    )
                    continue

                if 'name' not in section:
                    self.errors.append(
                        '{}, {}, section #{}: Every section must contain a `name` attribute representing the top-level '
                        'keys such as `instances` or `logs`'.format(self.integration, file_name, section_index)
                    )
                    continue

                section_name = section['name']
                if not isinstance(section_name, str):
                    self.errors.append(
                        '{}, {}, section #{}: Attribute `name` must be a string'.format(
                            self.integration, file_name, section_index
                        )
                    )

                if section_name in section_names_origin:
                    self.errors.append(
                        '{}, {}, section #{}: Section name `{}` already used by section #{}'.format(
                            self.integration, file_name, section_index, section_name, section_names_origin[section_name]
                        )
                    )
                else:
                    section_names_origin[section_name] = section_index

                if 'options' not in section:
                    section['options'] = []
                    continue

                options = section['options']
                if not isinstance(options, list):
                    self.errors.append(
                        '{}, {}, {}: The `options` attribute must be an array'.format(
                            self.integration, file_name, section_name
                        )
                    )
                    continue

                option_names_origin = {}
                for option_index, option in enumerate(options, 1):
                    if not isinstance(option, dict):
                        self.errors.append(
                            '{}, {}, {}, option #{}: Option attribute must be a mapping object'.format(
                                self.integration, file_name, section_name, option_index
                            )
                        )
                        continue

                    if 'name' not in option:
                        self.errors.append(
                            '{}, {}, {}, option #{}: Every option must contain a `name` attribute'.format(
                                self.integration, file_name, section_name, option_index
                            )
                        )
                        continue

                    option_name = option['name']
                    if not isinstance(option_name, str):
                        self.errors.append(
                            '{}, {}, {}, option #{}: Attribute `name` must be a string'.format(
                                self.integration, file_name, section_name, option_index
                            )
                        )

                    if option_name in option_names_origin:
                        self.errors.append(
                            '{}, {}, {}, option #{}: Option name `{}` already used by option #{}'.format(
                                self.integration,
                                file_name,
                                section_name,
                                option_index,
                                option_name,
                                option_names_origin[option_name],
                            )
                        )
                    else:
                        option_names_origin[option_name] = option_index

                    if 'description' not in option:
                        self.errors.append(
                            '{}, {}, {}, {}: Every option must contain a `description` attribute'.format(
                                self.integration, file_name, section_name, option_name
                            )
                        )
                        continue

                    description = option['description']
                    if not isinstance(description, str):
                        self.errors.append(
                            '{}, {}, {}, {}: Attribute `description` must be a string'.format(
                                self.integration, file_name, section_name, option_name, description
                            )
                        )

                    option.setdefault('required', False)
                    if not isinstance(option['required'], bool):
                        self.errors.append(
                            '{}, {}, {}, {}: Attribute `required` must be a boolean'.format(
                                self.integration, file_name, section_name, option_name
                            )
                        )

                    option.setdefault('secret', False)
                    if not isinstance(option['secret'], bool):
                        self.errors.append(
                            '{}, {}, {}, {}: Attribute `secret` must be a boolean'.format(
                                self.integration, file_name, section_name, option_name
                            )
                        )

                    if 'value' not in option:
                        self.errors.append(
                            '{}, {}, {}, {}: Every option must contain a `value` attribute'.format(
                                self.integration, file_name, section_name, option_name
                            )
                        )
                        continue

                    value = option['value']
                    if not isinstance(value, dict):
                        self.errors.append(
                            '{}, {}, {}, {}: Attribute `value` must be a mapping object'.format(
                                self.integration, file_name, section_name, option_name
                            )
                        )
                        continue

    def render_example_config_files(self):
        pass
