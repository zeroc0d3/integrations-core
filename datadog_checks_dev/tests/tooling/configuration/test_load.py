# (C) Datadog, Inc. 2019
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)
import pytest

from .utils import get_spec

pytestmark = pytest.mark.conf


def test_invalid_yaml():
    spec = get_spec(
        """
        foo:
          - bar
          baz: oops
        """
    )
    spec.load()

    assert spec.errors[0].startswith('test: Unable to parse the configuration specification')


def test_not_map():
    spec = get_spec('- foo')
    spec.load()

    assert 'test: Configuration specifications must be a mapping object' in spec.errors


def test_no_files():
    spec = get_spec(
        """
        foo:
        - bar
        """
    )
    spec.load()

    assert 'test: Configuration specifications must contain a top-level `files` attribute' in spec.errors


def test_files_not_array():
    spec = get_spec(
        """
        files:
          foo: bar
        """
    )
    spec.load()

    assert 'test: The top-level `files` attribute must be an array' in spec.errors


def test_file_not_map():
    spec = get_spec(
        """
        files:
        - 5
        - baz
        """
    )
    spec.load()

    assert 'test, file #1: File attribute must be a mapping object' in spec.errors
    assert 'test, file #2: File attribute must be a mapping object' in spec.errors


def test_file_no_name():
    spec = get_spec(
        """
        files:
        - foo: bar
        """
    )
    spec.load()

    assert (
        'test, file #1: Every file must contain a `name` attribute representing the final destination the Agent loads'
    ) in spec.errors


def test_file_name_duplicate():
    spec = get_spec(
        """
        files:
        - name: test.yaml
        - name: test.yaml
        """
    )
    spec.load()

    assert 'test, file #2: File name `test.yaml` already used by file #1' in spec.errors


def test_example_file_name_duplicate():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
        - name: bar.yaml
          example_name: test.yaml.example
        """
    )
    spec.load()

    assert 'test, file #2: Example file name `test.yaml.example` already used by file #1' in spec.errors


def test_file_name_not_string():
    spec = get_spec(
        """
        files:
        - name: 123
          example_name: test.yaml.example
        """
    )
    spec.load()

    assert 'test, file #1: Attribute `name` must be a string' in spec.errors


def test_example_file_name_not_string():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: 123
        """
    )
    spec.load()

    assert 'test, file #1: Attribute `example_name` must be a string' in spec.errors


def test_file_name_standard_incorrect():
    spec = get_spec(
        """
        files:
        - name: foo.yaml
        """
    )
    spec.load()

    assert 'test, file #1: File name `foo.yaml` should be `test.yaml`' in spec.errors


def test_example_file_name_autodiscovery_incorrect():
    spec = get_spec(
        """
        files:
        - name: auto_conf.yaml
          example_name: test.yaml.example
        """
    )
    spec.load()

    assert 'test, file #1: Example file name `test.yaml.example` should be `auto_conf.yaml`' in spec.errors


def test_example_file_name_standard_default():
    spec = get_spec(
        """
        files:
        - name: test.yaml
        """
    )
    spec.load()

    assert spec.data['files'][0]['example_name'] == 'conf.yaml.example'


def test_example_file_name_autodiscovery_default():
    spec = get_spec(
        """
        files:
        - name: auto_conf.yaml
        """
    )
    spec.load()

    assert spec.data['files'][0]['example_name'] == 'auto_conf.yaml'


def test_no_sections():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
        """
    )
    spec.load()

    assert (
        'test, test.yaml: Every file must contain a `sections` attribute '
        'containing things like `init_config`, `instances`, etc.'
    ) in spec.errors


def test_sections_not_array():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
            foo: bar
        """
    )
    spec.load()

    assert 'test, test.yaml: The `sections` attribute must be an array' in spec.errors


def test_section_not_map():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - 5
          - baz
        """
    )
    spec.load()

    assert 'test, test.yaml, section #1: Section attribute must be a mapping object' in spec.errors
    assert 'test, test.yaml, section #2: Section attribute must be a mapping object' in spec.errors


def test_section_no_name():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - foo: bar
        """
    )
    spec.load()

    assert (
        'test, test.yaml, section #1: Every section must contain a `name` attribute '
        'representing the top-level keys such as `instances` or `logs`'
    ) in spec.errors


def test_section_name_not_string():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - name: 123
        """
    )
    spec.load()

    assert 'test, test.yaml, section #1: Attribute `name` must be a string' in spec.errors


def test_section_name_duplicate():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - name: instances
          - name: instances
        """
    )
    spec.load()

    assert 'test, test.yaml, section #2: Section name `instances` already used by section #1' in spec.errors


def test_no_options():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - name: instances
        """
    )
    spec.load()

    assert not spec.errors
    assert spec.data['files'][0]['sections'][0]['options'] == []


def test_options_not_array():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - name: instances
            options:
              foo: bar
        """
    )
    spec.load()

    assert 'test, test.yaml, instances: The `options` attribute must be an array' in spec.errors


def test_option_not_map():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - name: instances
            options:
            - 5
            - baz
        """
    )
    spec.load()

    assert 'test, test.yaml, instances, option #1: Option attribute must be a mapping object' in spec.errors
    assert 'test, test.yaml, instances, option #2: Option attribute must be a mapping object' in spec.errors


def test_option_no_name():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - name: instances
            options:
            - foo: bar
        """
    )
    spec.load()

    assert 'test, test.yaml, instances, option #1: Every option must contain a `name` attribute' in spec.errors


def test_option_name_not_string():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - name: instances
            options:
            - name: 123
        """
    )
    spec.load()

    assert 'test, test.yaml, instances, option #1: Attribute `name` must be a string' in spec.errors


def test_option_name_duplicate():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - name: instances
            options:
            - name: server
            - name: server
        """
    )
    spec.load()

    assert 'test, test.yaml, instances, option #2: Option name `server` already used by option #1' in spec.errors


def test_option_no_description():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - name: instances
            options:
            - name: foo
        """
    )
    spec.load()

    assert 'test, test.yaml, instances, foo: Every option must contain a `description` attribute' in spec.errors


def test_option_description_not_string():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - name: instances
            options:
            - name: foo
              description: 123
        """
    )
    spec.load()

    assert 'test, test.yaml, instances, foo: Attribute `description` must be a string' in spec.errors


def test_option_required_not_boolean():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - name: instances
            options:
            - name: foo
              description: words
              required: nope
        """
    )
    spec.load()

    assert 'test, test.yaml, instances, foo: Attribute `required` must be a boolean' in spec.errors


def test_option_required_default():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - name: instances
            options:
            - name: foo
              description: words
        """
    )
    spec.load()

    assert spec.data['files'][0]['sections'][0]['options'][0]['required'] is False


def test_option_secret_not_boolean():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - name: instances
            options:
            - name: foo
              description: words
              secret: nope
        """
    )
    spec.load()

    assert 'test, test.yaml, instances, foo: Attribute `secret` must be a boolean' in spec.errors


def test_option_secret_default():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - name: instances
            options:
            - name: foo
              description: words
        """
    )
    spec.load()

    assert spec.data['files'][0]['sections'][0]['options'][0]['secret'] is False


def test_option_no_value():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - name: instances
            options:
            - name: foo
              description: words
        """
    )
    spec.load()

    assert 'test, test.yaml, instances, foo: Every option must contain a `value` attribute' in spec.errors


def test_option_value_not_map():
    spec = get_spec(
        """
        files:
        - name: test.yaml
          example_name: test.yaml.example
          sections:
          - name: instances
            options:
            - name: foo
              description: words
              value:
              - foo
        """
    )
    spec.load()

    assert 'test, test.yaml, instances, foo: Attribute `value` must be a mapping object' in spec.errors
