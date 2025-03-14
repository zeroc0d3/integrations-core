# CHANGELOG - mysql

## 6.0.0 / 2021-08-22

* [Added] Add agent version to mysql database monitoring payloads. See [#9916](https://github.com/DataDog/integrations-core/pull/9916).
* [Added] Add fetching of null row in events_statements_by_digest. See [#9892](https://github.com/DataDog/integrations-core/pull/9892).
* [Added] Use `display_default` as a fallback for `default` when validating config models. See [#9739](https://github.com/DataDog/integrations-core/pull/9739).
* [Changed] Update mysql obfuscator options config. See [#9885](https://github.com/DataDog/integrations-core/pull/9885).
* [Changed] Send the correct hostname with metrics when DBM is enabled. See [#9878](https://github.com/DataDog/integrations-core/pull/9878).

## 5.0.4 / 2021-07-22 / Agent 7.30.0

* [Fixed] Properly allow deprecated required config. See [#9750](https://github.com/DataDog/integrations-core/pull/9750).
* [Fixed] Bump `datadog-checks-base` version requirement. See [#9718](https://github.com/DataDog/integrations-core/pull/9718).

## 5.0.3 / 2021-07-16

* [Fixed] Support old executable names. See [#9716](https://github.com/DataDog/integrations-core/pull/9716).

## 5.0.2 / 2021-07-15

* [Fixed] fix incorrect `min_collection_interval` on DBM metrics payload. See [#9695](https://github.com/DataDog/integrations-core/pull/9695).

## 5.0.1 / 2021-07-13

* [Fixed] Fix obfuscator options being converted into bytes rather than string. See [#9676](https://github.com/DataDog/integrations-core/pull/9676).

## 5.0.0 / 2021-07-12

* [Added] Add DBM SQL obfuscator options. See [#9639](https://github.com/DataDog/integrations-core/pull/9639).
* [Added] Add truncated statement indicator to mysql query sample events. See [#9620](https://github.com/DataDog/integrations-core/pull/9620).
* [Fixed] Bump base package dependency. See [#9666](https://github.com/DataDog/integrations-core/pull/9666).
* [Changed] Change DBM `statement` config keys and metric terminology to `query`. See [#9661](https://github.com/DataDog/integrations-core/pull/9661).
* [Changed] remove execution plan cost extraction. See [#9631](https://github.com/DataDog/integrations-core/pull/9631).
* [Changed] decouple DBM query metrics interval from check run interval. See [#9658](https://github.com/DataDog/integrations-core/pull/9658).
* [Changed] DBM statement_samples enabled by default, rename DBM-enabled key. See [#9619](https://github.com/DataDog/integrations-core/pull/9619).

## 4.1.0 / 2021-06-30

* [Added] Provide a reason for not having an execution plan (MySQL). See [#9569](https://github.com/DataDog/integrations-core/pull/9569).
* [Fixed] Look for mariadbd process for MariaDB 10.5+. See [#9543](https://github.com/DataDog/integrations-core/pull/9543).
* [Fixed] Fix insufficient rate limiting of statement samples . See [#9585](https://github.com/DataDog/integrations-core/pull/9585).

## 4.0.3 / 2021-06-08 / Agent 7.29.0

* [Fixed] Enable autocommit on all connections. See [#9476](https://github.com/DataDog/integrations-core/pull/9476).

## 4.0.2 / 2021-06-07

* [Fixed] Fix missing replication_role tag on DBM metrics & events. See [#9486](https://github.com/DataDog/integrations-core/pull/9486).

## 4.0.1 / 2021-06-01

* [Fixed] Bump minimum base package requirement. See [#9449](https://github.com/DataDog/integrations-core/pull/9449).

## 4.0.0 / 2021-05-28

* [Added] Adds a `replication_role` tag to metrics emitted from AWS Aurora instances. See [#8282](https://github.com/DataDog/integrations-core/pull/8282).
* [Fixed] Fix potential erroneous mysql statement metrics on duplicate queries. See [#9253](https://github.com/DataDog/integrations-core/pull/9253).
* [Changed] Send database monitoring "full query text" events. See [#9397](https://github.com/DataDog/integrations-core/pull/9397).
* [Changed] Remove `service` event facet. See [#9275](https://github.com/DataDog/integrations-core/pull/9275).
* [Changed] Send database monitoring query metrics to new intake. See [#9223](https://github.com/DataDog/integrations-core/pull/9223).
* [Removed] Remove unused query metric limit configuration. See [#9376](https://github.com/DataDog/integrations-core/pull/9376).

## 3.0.1 / 2021-04-27 / Agent 7.28.0

* [Fixed] Account for name change in replica metrics. See [#9230](https://github.com/DataDog/integrations-core/pull/9230).

## 3.0.0 / 2021-04-19

* [Added] Add runtime configuration validation. See [#8958](https://github.com/DataDog/integrations-core/pull/8958).
* [Added] Upgrade cryptography to 3.4.6 on Python 3. See [#8764](https://github.com/DataDog/integrations-core/pull/8764).
* [Added] Add replication_mode tag to replication service check. See [#8753](https://github.com/DataDog/integrations-core/pull/8753).
* [Changed] Submit DBM query samples via new aggregator API. See [#9045](https://github.com/DataDog/integrations-core/pull/9045).

## 2.3.0 / 2021-03-07 / Agent 7.27.0

* [Added] Collect mysql statement samples & execution plans . See [#8629](https://github.com/DataDog/integrations-core/pull/8629).
* [Added] Apply default limits to MySQL statement summaries. See [#8646](https://github.com/DataDog/integrations-core/pull/8646).
* [Fixed] Rename config spec example consumer option `default` to `display_default`. See [#8593](https://github.com/DataDog/integrations-core/pull/8593).
* [Fixed] Support newer queries. See [#8402](https://github.com/DataDog/integrations-core/pull/8402).
* [Fixed] Bump minimum base package version. See [#8443](https://github.com/DataDog/integrations-core/pull/8443).
* [Security] Upgrade cryptography python package. See [#8611](https://github.com/DataDog/integrations-core/pull/8611).

## 2.2.1 / 2021-01-29 / Agent 7.26.0

* [Fixed] Fix condition for replication status. See [#8475](https://github.com/DataDog/integrations-core/pull/8475).

## 2.2.0 / 2021-01-28

* [Security] Upgrade cryptography python package. See [#8476](https://github.com/DataDog/integrations-core/pull/8476).

## 2.1.3 / 2021-01-25

* [Fixed] Simplify replication status check. See [#8401](https://github.com/DataDog/integrations-core/pull/8401).
* [Fixed] Refactor replica metrics and add some debug lines. See [#8380](https://github.com/DataDog/integrations-core/pull/8380).
* [Fixed] Tighten condition for mysql.replication.slave_running. See [#8381](https://github.com/DataDog/integrations-core/pull/8381).

## 2.1.2 / 2020-11-17 / Agent 7.25.0

* [Fixed] Add debug log line for replication status. See [#8040](https://github.com/DataDog/integrations-core/pull/8040).

## 2.1.1 / 2020-11-10 / Agent 7.24.0

* [Fixed] Change `deep_database_monitoring` language from BETA to ALPHA. See [#7948](https://github.com/DataDog/integrations-core/pull/7948).
* [Fixed] Fix configuration typo. See [#7911](https://github.com/DataDog/integrations-core/pull/7911).

## 2.1.0 / 2020-10-31

* [Added] Support MySQL statement-level metrics for deep database monitoring. See [#7851](https://github.com/DataDog/integrations-core/pull/7851).
* [Added] [doc] Add encoding in log config sample. See [#7708](https://github.com/DataDog/integrations-core/pull/7708).
* [Fixed] Fix config spec default values. See [#7687](https://github.com/DataDog/integrations-core/pull/7687).
* [Security] Upgrade `cryptography` dependency. See [#7869](https://github.com/DataDog/integrations-core/pull/7869).

## 2.0.3 / 2020-09-21 / Agent 7.23.0

* [Fixed] Use database config template in existing specs. See [#7548](https://github.com/DataDog/integrations-core/pull/7548).
* [Fixed] Do not render null defaults for config spec example consumer. See [#7503](https://github.com/DataDog/integrations-core/pull/7503).
* [Fixed] Fix style for the latest release of Black. See [#7438](https://github.com/DataDog/integrations-core/pull/7438).

## 2.0.2 / 2020-08-25

* [Fixed] Parse byte string versions. See [#7425](https://github.com/DataDog/integrations-core/pull/7425).

## 2.0.1 / 2020-08-14 / Agent 7.22.0

* [Fixed] Update config spec default values. See [#7340](https://github.com/DataDog/integrations-core/pull/7340).

## 2.0.0 / 2020-08-10

* [Added] Send more useful metrics for wsrep flow control. See [#7316](https://github.com/DataDog/integrations-core/pull/7316). Thanks [sayap](https://github.com/sayap).
* [Added] Add ability to specify which charset to use when connecting to mysql. See [#7216](https://github.com/DataDog/integrations-core/pull/7216).
* [Fixed] Update logs config service field to optional. See [#7209](https://github.com/DataDog/integrations-core/pull/7209).
* [Fixed] Refactor connection, improve documentation. See [#7204](https://github.com/DataDog/integrations-core/pull/7204).
* [Fixed] Extract version utils. See [#7198](https://github.com/DataDog/integrations-core/pull/7198).
* [Fixed] Split config out. See [#7195](https://github.com/DataDog/integrations-core/pull/7195).
* [Changed] Fix mysql metric for innodb row lock time. See [#7289](https://github.com/DataDog/integrations-core/pull/7289). Thanks [sayap](https://github.com/sayap).

## 1.15.0 / 2020-06-29 / Agent 7.21.0

* [Added] Catch unicode error. See [#6947](https://github.com/DataDog/integrations-core/pull/6947).
* [Fixed] Add config spec. See [#6908](https://github.com/DataDog/integrations-core/pull/6908).

## 1.14.0 / 2020-06-03

* [Added] Add custom queries. See [#6776](https://github.com/DataDog/integrations-core/pull/6776).

## 1.13.0 / 2020-05-17 / Agent 7.20.0

* [Added] Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).

## 1.12.1 / 2020-04-04 / Agent 7.19.0

* [Fixed] Remove logs sourcecategory. See [#6121](https://github.com/DataDog/integrations-core/pull/6121).

## 1.12.0 / 2020-01-13 / Agent 7.17.0

* [Added] Use lazy logging format. See [#5398](https://github.com/DataDog/integrations-core/pull/5398).
* [Added] Use lazy logging format. See [#5377](https://github.com/DataDog/integrations-core/pull/5377).

## 1.11.0 / 2019-12-20

* [Added] Document log_processing_rules for MySQL slow query logs. See [#5237](https://github.com/DataDog/integrations-core/pull/5237).
* [Fixed] Fix formatting and typos in the MySQL documentation. See [#5238](https://github.com/DataDog/integrations-core/pull/5238).
* [Fixed] Improve perf (minor) by only defining metadata namedtuple once. See [#5138](https://github.com/DataDog/integrations-core/pull/5138).

## 1.10.0 / 2019-12-02 / Agent 7.16.0

* [Added] Upgrade cryptography to 2.8. See [#5047](https://github.com/DataDog/integrations-core/pull/5047).
* [Fixed] Fix TypeError in schema size check. See [#5043](https://github.com/DataDog/integrations-core/pull/5043). Thanks [rayatbuzzfeed](https://github.com/rayatbuzzfeed).
* [Added] Submit version metadata. See [#4814](https://github.com/DataDog/integrations-core/pull/4814).

## 1.9.1 / 2019-10-11 / Agent 6.15.0

* [Fixed] Fix typo in logs (Instace -> Instance). See [#4715](https://github.com/DataDog/integrations-core/pull/4715). Thanks [ajacoutot](https://github.com/ajacoutot).

## 1.9.0 / 2019-07-04 / Agent 6.13.0

* [Added] Update cryptography version. See [#4000](https://github.com/DataDog/integrations-core/pull/4000).

## 1.8.0 / 2019-05-14 / Agent 6.12.0

* [Added] Adhere to code style. See [#3541](https://github.com/DataDog/integrations-core/pull/3541).

## 1.7.0 / 2019-02-27 / Agent 6.10.0

* [Added] Remove Encrypted column from results. See [#3174](https://github.com/DataDog/integrations-core/pull/3174).

## 1.6.0 / 2019-02-18

* [Added] Finish Python 3 Support. See [#2948](https://github.com/DataDog/integrations-core/pull/2948).

## 1.5.0 / 2018-11-30 / Agent 6.8.0

* [Added] Support Python 3. See [#2630][1].
* [Fixed] Use raw string literals when \ is present. See [#2465][2].

## 1.4.0 / 2018-09-04 / Agent 6.5.0

* [Fixed] Make sure all checks' versions are exposed. See [#1945][3].
* [Added] Add channel tag to replica metrics. See [#1753][4].
* [Fixed] Add data files to the wheel package. See [#1727][5].

## 1.3.0 / 2018-06-13

* [Added] Make the max custom queries configurable in the yaml file. See [#1713][6].

### 1.2.1 / 2018-05-31

* [Fixed] Fix replication data extraction when replication channel is set. See [#1639][7].
* [Fixed] Fix error while fetching mysql pid from psutil . See [#1620][8].

## 1.2.0 / 2018-05-11

* [FEATURE] Add custom tag support to service checks.
* [BUGFIX] reports slave_service check as `CRITICAL` if `Slave_running` global variable is OFF.

## 1.1.3 / 2018-03-23

* [BUGFIX] Fixes the buffer pool metric to return the aggregated values
* [DEPENDENCY] Bump the pymysql version from 0.6.6 to 0.8.0

## 1.1.2 / 2018-02-13

* [DOC] Adding configuration for log collection in `conf.yaml`

## 1.1.1 / 2018-02-13

* [BUGFIX] Changes default value of `connect_timeout` to 10. See [#1020][9]

## 1.1.0 / 2018-01-10

* [FEATURE] Add support for multi-source replication in both MariaDB and MySQL
* [FEATURE] tag `mysql.replication.*` metrics with the replication channel name

## 1.0.5 / 2017-11-21

* [BUGFIX] Fixes [#783][10]

## 1.0.4 / 2017-08-28

* [BUGFIX] Add new innodb aio read/write format and prevent future crashes from new format. See [#660][11]
* [BUGFIX] Fix bug when options dict is empty. See [#637][12]
* [BUGFIX] Fix slow query check for 95th us percentile. See [#586][13], thanks [@EdwardMcConnell][14]

## 1.0.3 / 2017-05-11

* [BUGFIX] MySQL: Fix replication service check for <5.6. See [#394][15]

## 1.0.2 / 2017-04-24

* [BUGFIX] MySQL: Fix for replication service check. See [#329][16]

## 1.0.1 / 2017-03-23

* [BUGFIX] MySQL: Allow for configurable collection of replica statuses. See [#288][17]
* [BUGFIX] MySQL: Slaves_connected should be a gauge. See [#291][18]

## 1.0.0 / 2017-03-23

* [FEATURE] adds mysql integration.

<!--- The following link definition list is generated by PimpMyChangelog --->
[1]: https://github.com/DataDog/integrations-core/pull/2630
[2]: https://github.com/DataDog/integrations-core/pull/2465
[3]: https://github.com/DataDog/integrations-core/pull/1945
[4]: https://github.com/DataDog/integrations-core/pull/1753
[5]: https://github.com/DataDog/integrations-core/pull/1727
[6]: https://github.com/DataDog/integrations-core/pull/1713
[7]: https://github.com/DataDog/integrations-core/pull/1639
[8]: https://github.com/DataDog/integrations-core/pull/1620
[9]: https://github.com/DataDog/integrations-core/issues/1020
[10]: https://github.com/DataDog/integrations-core/issues/783
[11]: https://github.com/DataDog/integrations-core/issues/660
[12]: https://github.com/DataDog/integrations-core/issues/637
[13]: https://github.com/DataDog/integrations-core/issues/586
[14]: https://github.com/EdwardMcConnell
[15]: https://github.com/DataDog/integrations-core/issues/394
[16]: https://github.com/DataDog/integrations-core/issues/329
[17]: https://github.com/DataDog/integrations-core/issues/288
[18]: https://github.com/DataDog/integrations-core/issues/291
