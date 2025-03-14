# CHANGELOG - wmi_check

## 1.11.0 / 2021-08-22

* [Added] Use `display_default` as a fallback for `default` when validating config models. See [#9739](https://github.com/DataDog/integrations-core/pull/9739).

## 1.10.0 / 2021-04-19 / Agent 7.28.0

* [Added] Add runtime configuration validation. See [#9008](https://github.com/DataDog/integrations-core/pull/9008).
* [Added] Upgrade pywin32 on Python 3. See [#8845](https://github.com/DataDog/integrations-core/pull/8845).

## 1.9.3 / 2021-03-07 / Agent 7.27.0

* [Fixed] Rename config spec example consumer option `default` to `display_default`. See [#8593](https://github.com/DataDog/integrations-core/pull/8593).
* [Fixed] Bump minimum base package version. See [#8443](https://github.com/DataDog/integrations-core/pull/8443).

## 1.9.2 / 2020-10-06 / Agent 7.24.0

* [Fixed] Fix missing tags from tag_by. See [#7706](https://github.com/DataDog/integrations-core/pull/7706).

## 1.9.1 / 2020-08-10 / Agent 7.22.0

* [Fixed] Fix namespace default value. See [#7179](https://github.com/DataDog/integrations-core/pull/7179).

## 1.9.0 / 2020-06-29 / Agent 7.21.0

* [Added] Upgrade pywin32 to 228. See [#6980](https://github.com/DataDog/integrations-core/pull/6980).
* [Added] Support multiple properties in tag_by. See [#6614](https://github.com/DataDog/integrations-core/pull/6614).
* [Fixed] Remove multi-instances support. See [#6325](https://github.com/DataDog/integrations-core/pull/6325).

## 1.8.0 / 2020-05-17 / Agent 7.20.0

* [Added] Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).
* [Added] Add config specs. See [#6409](https://github.com/DataDog/integrations-core/pull/6409).
* [Fixed] WMI base typing and instance free API. See [#6329](https://github.com/DataDog/integrations-core/pull/6329).

## 1.7.3 / 2020-04-04 / Agent 7.19.0

* [Fixed] Update deprecated imports. See [#6088](https://github.com/DataDog/integrations-core/pull/6088).

## 1.7.2 / 2020-02-25 / Agent 7.18.0

* [Fixed] Bump minimum base check on wmi checks. See [#5860](https://github.com/DataDog/integrations-core/pull/5860).

## 1.7.1 / 2020-02-22

* [Fixed] Fix thread leak in WMI sampler. See [#5659](https://github.com/DataDog/integrations-core/pull/5659). Thanks [rlaveycal](https://github.com/rlaveycal).
* [Fixed] Change wmi_check to use lists instead of tuples for filters. See [#5510](https://github.com/DataDog/integrations-core/pull/5510).

## 1.7.0 / 2020-01-13 / Agent 7.17.0

* [Added] Use lazy logging format. See [#5398](https://github.com/DataDog/integrations-core/pull/5398).

## 1.6.0 / 2019-12-02 / Agent 7.16.0

* [Added] Upgrade pywin32 to 227. See [#5036](https://github.com/DataDog/integrations-core/pull/5036).

## 1.5.0 / 2019-10-11 / Agent 6.15.0

* [Added] Upgrade pywin32 to 225. See [#4563](https://github.com/DataDog/integrations-core/pull/4563).

## 1.4.2 / 2019-07-13 / Agent 6.13.0

* [Fixed] Avoid WMISampler inheriting from Thread. See [#4051](https://github.com/DataDog/integrations-core/pull/4051).

## 1.4.1 / 2019-07-04

* [Fixed] Make WMISampler hashable. See [#4043](https://github.com/DataDog/integrations-core/pull/4043).

## 1.4.0 / 2019-05-14 / Agent 6.12.0

* [Added] Adhere to code style. See [#3584](https://github.com/DataDog/integrations-core/pull/3584).

## 1.3.0 / 2019-02-18 / Agent 6.10.0

* [Added] Support Python 3 for WMI. See [#3031](https://github.com/DataDog/integrations-core/pull/3031).

## 1.2.0 / 2018-10-12 / Agent 6.6.0

* [Added] Pin pywin32 dependency. See [#2322][1].

## 1.1.2 / 2018-09-04 / Agent 6.5.0

* [Fixed] Moves WMI Check to Pytest. See [#2133][2].
* [Fixed] Add data files to the wheel package. See [#1727][3].

## 1.1.1 / 2018-03-23

* [BUGFIX] change `constant_tags` field in configuration to `tags` for consistency.

## 1.0.0 / 2017-03-22

* [FEATURE] adds wmi_check integration.
[1]: https://github.com/DataDog/integrations-core/pull/2322
[2]: https://github.com/DataDog/integrations-core/pull/2133
[3]: https://github.com/DataDog/integrations-core/pull/1727
