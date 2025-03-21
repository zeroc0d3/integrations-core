# CHANGELOG - mapreduce

## 2.0.0 / 2021-08-22

* [Changed] Remove messages for integrations for OK service checks. See [#9888](https://github.com/DataDog/integrations-core/pull/9888).

## 1.14.0 / 2021-03-07 / Agent 7.27.0

* [Added] Rename cluster_name tag to mapreduce_cluster. See [#8588](https://github.com/DataDog/integrations-core/pull/8588).
* [Fixed] Bump minimum base package version. See [#8443](https://github.com/DataDog/integrations-core/pull/8443).

## 1.13.0 / 2020-10-31 / Agent 7.24.0

* [Added] Add ability to dynamically get authentication information. See [#7660](https://github.com/DataDog/integrations-core/pull/7660).
* [Added] [doc] Add encoding in log config sample. See [#7708](https://github.com/DataDog/integrations-core/pull/7708).

## 1.12.0 / 2020-09-21 / Agent 7.23.0

* [Added] Add RequestsWrapper option to support UTF-8 for basic auth. See [#7441](https://github.com/DataDog/integrations-core/pull/7441).
* [Added] Add mapreduce config specs. See [#7178](https://github.com/DataDog/integrations-core/pull/7178).
* [Fixed] Fix style for the latest release of Black. See [#7438](https://github.com/DataDog/integrations-core/pull/7438).

## 1.11.1 / 2020-08-10 / Agent 7.22.0

* [Fixed] Update ntlm_domain example. See [#7118](https://github.com/DataDog/integrations-core/pull/7118).

## 1.11.0 / 2020-06-29 / Agent 7.21.0

* [Added] Add note about warning concurrency. See [#6967](https://github.com/DataDog/integrations-core/pull/6967).

## 1.10.0 / 2020-05-17 / Agent 7.20.0

* [Added] Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).

## 1.9.0 / 2020-04-04 / Agent 7.19.0

* [Added] Version metadata. See [#5448](https://github.com/DataDog/integrations-core/pull/5448).

## 1.8.0 / 2020-01-13 / Agent 7.17.0

* [Added] Use lazy logging format. See [#5398](https://github.com/DataDog/integrations-core/pull/5398).
* [Added] Use lazy logging format. See [#5377](https://github.com/DataDog/integrations-core/pull/5377).

## 1.7.0 / 2019-12-02 / Agent 7.16.0

* [Added] Add auth type to RequestsWrapper. See [#4708](https://github.com/DataDog/integrations-core/pull/4708).

## 1.6.0 / 2019-10-11 / Agent 6.15.0

* [Added] Add option to override KRB5CCNAME env var. See [#4578](https://github.com/DataDog/integrations-core/pull/4578).

## 1.5.0 / 2019-07-12 / Agent 6.13.0

* [Added] Use the new RequestsWrapper for connecting to services. See [#4094](https://github.com/DataDog/integrations-core/pull/4094).

## 1.4.0 / 2019-05-14 / Agent 6.12.0

* [Added] Adhere to code style. See [#3535](https://github.com/DataDog/integrations-core/pull/3535).

## 1.3.0 / 2019-02-18 / Agent 6.10.0

* [Added] Support Python 3. See [#2870](https://github.com/DataDog/integrations-core/pull/2870).

## 1.2.1 / 2018-09-04 / Agent 6.5.0

* [Fixed] Fix bug and typo in DEFAULT_CLUSTER_NAME for YARN check. See [#1814][1]. Thanks [eplanet][2].
* [Fixed] Add data files to the wheel package. See [#1727][3].

## 1.2.0 / 2018-06-06

* [Added] Add support for HTTP authentication. See [#1678][4].
* [Added] Adds skip ssl validation. See [#1470][5].

## 1.1.0 / 2018-03-23

* [FEATURE] Adds custom tag support to service check.

## 1.0.0 / 2017-03-22

* [FEATURE] adds mapreduce integration.
[1]: https://github.com/DataDog/integrations-core/pull/1814
[2]: https://github.com/eplanet
[3]: https://github.com/DataDog/integrations-core/pull/1727
[4]: https://github.com/DataDog/integrations-core/pull/1678
[5]: https://github.com/DataDog/integrations-core/pull/1470
