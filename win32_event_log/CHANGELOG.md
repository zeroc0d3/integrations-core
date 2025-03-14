# CHANGELOG - win32_event_log

## 2.10.0 / 2021-08-22

* [Added] Use `display_default` as a fallback for `default` when validating config models. See [#9739](https://github.com/DataDog/integrations-core/pull/9739).
* [Fixed] Fix AttributeError when filters are not set. See [#9655](https://github.com/DataDog/integrations-core/pull/9655).
* [Fixed] Document the max number of IDs that can be used for filtering per instance. See [#9749](https://github.com/DataDog/integrations-core/pull/9749).

## 2.9.1 / 2021-06-01 / Agent 7.29.0

* [Fixed] Bump minimum base package requirement. See [#9449](https://github.com/DataDog/integrations-core/pull/9449).

## 2.9.0 / 2021-05-28

* [Added] Add runtime configuration validation. See [#9006](https://github.com/DataDog/integrations-core/pull/9006).

## 2.8.0 / 2021-04-19 / Agent 7.28.0

* [Added] Upgrade pywin32 on Python 3. See [#8845](https://github.com/DataDog/integrations-core/pull/8845).
* [Fixed] Fix description of the `path` option. See [#8842](https://github.com/DataDog/integrations-core/pull/8842).

## 2.7.1 / 2021-03-07 / Agent 7.27.0

* [Fixed] Fix queries for audit success/failure. See [#8596](https://github.com/DataDog/integrations-core/pull/8596).
* [Fixed] Rename config spec example consumer option `default` to `display_default`. See [#8593](https://github.com/DataDog/integrations-core/pull/8593).
* [Fixed] Bump minimum base package version. See [#8443](https://github.com/DataDog/integrations-core/pull/8443).

## 2.7.0 / 2020-10-31 / Agent 7.24.0

* [Added] Add config specs. See [#7856](https://github.com/DataDog/integrations-core/pull/7856).

## 2.6.1 / 2020-09-21 / Agent 7.23.0

* [Fixed] Fix style for the latest release of Black. See [#7438](https://github.com/DataDog/integrations-core/pull/7438).
* [Fixed] Make it easier to configure legacy vs new options. See [#7406](https://github.com/DataDog/integrations-core/pull/7406).

## 2.6.0 / 2020-08-19

* [Added] Introduce new, more performant implementation. See [#7005](https://github.com/DataDog/integrations-core/pull/7005).

## 2.5.0 / 2020-06-29 / Agent 7.21.0

* [Added] Upgrade pywin32 to 228. See [#6980](https://github.com/DataDog/integrations-core/pull/6980).
* [Added] Override CaseInsensitiveDict `copy()` function. See [#6715](https://github.com/DataDog/integrations-core/pull/6715).

## 2.4.0 / 2020-05-17 / Agent 7.20.0

* [Added] Refactor check to support new implementation. See [#6639](https://github.com/DataDog/integrations-core/pull/6639).
* [Added] Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).
* [Fixed] Add wmi integration test and fix filter sampler. See [#6576](https://github.com/DataDog/integrations-core/pull/6576).
* [Fixed] WMI base typing and instance free API. See [#6329](https://github.com/DataDog/integrations-core/pull/6329).

## 2.3.4 / 2020-04-16

* [Fixed] Normalize integers. See [#6357](https://github.com/DataDog/integrations-core/pull/6357).

## 2.3.3 / 2020-04-04 / Agent 7.19.0

* [Fixed] Remove logs sourcecategory. See [#6121](https://github.com/DataDog/integrations-core/pull/6121).

## 2.3.2 / 2020-02-25 / Agent 7.18.0

* [Fixed] Bump minimum base check on wmi checks. See [#5860](https://github.com/DataDog/integrations-core/pull/5860).

## 2.3.1 / 2020-02-22

* [Fixed] Fix thread leak in WMI sampler. See [#5659](https://github.com/DataDog/integrations-core/pull/5659). Thanks [rlaveycal](https://github.com/rlaveycal).

## 2.3.0 / 2020-01-13 / Agent 7.17.0

* [Added] Use lazy logging format. See [#5398](https://github.com/DataDog/integrations-core/pull/5398).
* [Added] Use lazy logging format. See [#5377](https://github.com/DataDog/integrations-core/pull/5377).

## 2.2.0 / 2019-12-02 / Agent 7.16.0

* [Added] Upgrade pywin32 to 227. See [#5036](https://github.com/DataDog/integrations-core/pull/5036).

## 2.1.0 / 2019-10-11 / Agent 6.15.0

* [Added] Upgrade pywin32 to 225. See [#4563](https://github.com/DataDog/integrations-core/pull/4563).

## 2.0.1 / 2019-08-24 / Agent 6.14.0

* [Fixed] Remove check for user filter. See [#4342](https://github.com/DataDog/integrations-core/pull/4342).

## 2.0.0 / 2019-05-14 / Agent 6.12.0

* [Changed] Require the use of filters. See [#3652](https://github.com/DataDog/integrations-core/pull/3652).
* [Added] Adhere to code style. See [#3582](https://github.com/DataDog/integrations-core/pull/3582).

## 1.4.0 / 2019-02-18 / Agent 6.10.0

* [Added] Support Python 3. See [#3040](https://github.com/DataDog/integrations-core/pull/3040).

## 1.3.0 / 2018-10-12 / Agent 6.6.0

* [Added] Pin pywin32 dependency. See [#2322][1].

## 1.2.0 / 2018-09-04 / Agent 6.5.0

* [Fixed] Fix syntax. See [#2115][2].
* [Added] Check events between system boot and DataDog agent start. See [#1929][3]. Thanks [jvanlieshout][4].
* [Fixed] Add data files to the wheel package. See [#1727][5].

## 1.1.1 / 2018-01-10

* [FEATURE] Add parameters to set priority in event stream for all events or per instance See [#971][6]

## 1.0.0 / 2017-03-22

* [FEATURE] adds win32_event_log integration.

<!--- The following link definition list is generated by PimpMyChangelog --->
[1]: https://github.com/DataDog/integrations-core/pull/2322
[2]: https://github.com/DataDog/integrations-core/pull/2115
[3]: https://github.com/DataDog/integrations-core/pull/1929
[4]: https://github.com/jvanlieshout
[5]: https://github.com/DataDog/integrations-core/pull/1727
[6]: https://github.com/DataDog/integrations-core/issues/971
