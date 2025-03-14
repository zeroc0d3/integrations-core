# CHANGELOG - etcd

## 2.7.1 / 2021-07-12 / Agent 7.30.0

* [Fixed] etcd signature. See [#9551](https://github.com/DataDog/integrations-core/pull/9551).

## 2.7.0 / 2021-05-28 / Agent 7.29.0

* [Added] Support "ignore_tags" configuration. See [#9392](https://github.com/DataDog/integrations-core/pull/9392).

## 2.6.1 / 2021-01-25 / Agent 7.26.0

* [Fixed] Update prometheus_metrics_prefix documentation. See [#8236](https://github.com/DataDog/integrations-core/pull/8236).

## 2.6.0 / 2020-10-31 / Agent 7.24.0

* [Added] Sync openmetrics config specs with new option ignore_metrics_by_labels. See [#7823](https://github.com/DataDog/integrations-core/pull/7823).
* [Added] Add config specs. See [#7850](https://github.com/DataDog/integrations-core/pull/7850).

## 2.5.0 / 2020-09-21 / Agent 7.23.0

* [Added] Add support for etcd logs. See [#7431](https://github.com/DataDog/integrations-core/pull/7431).

## 2.4.1 / 2020-08-10 / Agent 7.22.0

* [Fixed] Update ntlm_domain example. See [#7118](https://github.com/DataDog/integrations-core/pull/7118).

## 2.4.0 / 2020-06-29 / Agent 7.21.0

* [Added] Add note about warning concurrency. See [#6967](https://github.com/DataDog/integrations-core/pull/6967).

## 2.3.0 / 2020-05-17 / Agent 7.20.0

* [Added] Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).

## 2.2.1 / 2020-02-22 / Agent 7.18.0

* [Fixed] Update auto_conf yaml to default to preview. See [#5661](https://github.com/DataDog/integrations-core/pull/5661).

## 2.2.0 / 2020-01-13 / Agent 7.17.0

* [Added] Use lazy logging format. See [#5377](https://github.com/DataDog/integrations-core/pull/5377).

## 2.1.0 / 2019-11-06 / Agent 7.16.0

* [Fixed] Add ssl config options necessary for Openmetrics base. See [#4951](https://github.com/DataDog/integrations-core/pull/4951).
* [Added] Add version metadata. See [#4950](https://github.com/DataDog/integrations-core/pull/4950).
* [Added] Add auth type to RequestsWrapper. See [#4708](https://github.com/DataDog/integrations-core/pull/4708).

## 2.0.1 / 2019-10-16 / Agent 6.15.0

* [Fixed] Set use_preview to True in init as well. See [#4792](https://github.com/DataDog/integrations-core/pull/4792).

## 2.0.0 / 2019-10-11

* [Changed] Etcd uses V3 preview by default. See [#4656](https://github.com/DataDog/integrations-core/pull/4656).
* [Added] Add option to override KRB5CCNAME env var. See [#4578](https://github.com/DataDog/integrations-core/pull/4578).

## 1.9.0 / 2019-08-24 / Agent 6.14.0

* [Added] Add requests wrapper to etcd. See [#4323](https://github.com/DataDog/integrations-core/pull/4323).

## 1.8.0 / 2019-05-14 / Agent 6.12.0

* [Added] Adhere to code style. See [#3505](https://github.com/DataDog/integrations-core/pull/3505).

## 1.7.0 / 2019-02-18 / Agent 6.10.0

* [Fixed] Use alpha grpc gateway endpoint. See [#3125](https://github.com/DataDog/integrations-core/pull/3125).
* [Added] Make `is_leader` tag optional. See [#3114](https://github.com/DataDog/integrations-core/pull/3114).

## 1.6.1 / 2019-01-04 / Agent 6.9.0

* [Fixed] Postpone deprecation warning to 6.10. See [#2844][1].
* [Fixed] Fix indentation for end of .example file. See [#2843][2].

## 1.6.0 / 2018-11-07 / Agent 6.8.0

* [Added] Add support for ETCD v3 API, begin deprecation of ETCD < v3. See [#2506][3].

## 1.5.1 / 2018-09-04 / Agent 6.5.0

* [Fixed] Add data files to the wheel package. See [#1727][4].

## 1.5.0 / 2018-06-13 / Agent 6.4.0

* [Added] Package `auto_conf.yaml` for appropriate integrations. See [#1664][5].

## 1.4.0 / 2018-05-11

* [IMPROVEMENT] Get the right metrics depending on the instance state. See [#1348][6].
* [FEATURE] Hardcode the 2379 port in the Autodiscovery template. See [#1444][7] for more information.

## 1.3.0 / 2018-01-10

* [FEATURE] Add a Service Check to report whether a member node is healty or not. See [#917][8], thanks [@stensonb][9].

## 1.2.0 / 2017-11-21

* [UPDATE] Update auto_conf template to support agent 6 and 5.20+. See [#860][10]

## 1.1.0 / 2017-10-10

* [FEATURE] Updates the Service Check tag to only use the base URL. See [#736][11].

## 1.0.0 / 2017-03-22

* [FEATURE] adds etcd integration.

<!--- The following link definition list is generated by PimpMyChangelog --->
[1]: https://github.com/DataDog/integrations-core/pull/2844
[2]: https://github.com/DataDog/integrations-core/pull/2843
[3]: https://github.com/DataDog/integrations-core/pull/2506
[4]: https://github.com/DataDog/integrations-core/pull/1727
[5]: https://github.com/DataDog/integrations-core/pull/1664
[6]: https://github.com/DataDog/integrations-core/issues/1348
[7]: https://github.com/DataDog/integrations-core/pull/1444
[8]: https://github.com/DataDog/integrations-core/issues/917
[9]: https://github.com/stensonb
[10]: https://github.com/DataDog/integrations-core/issues/860
[11]: https://github.com/DataDog/integrations-core/issues/736
