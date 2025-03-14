# CHANGELOG - Confluent Platform

## 1.5.0 / 2021-07-12 / Agent 7.30.0

* [Added] Enable `new_gc_metrics` JMX config option for new installations. See [#9501](https://github.com/DataDog/integrations-core/pull/9501).

## 1.4.1 / 2021-05-28 / Agent 7.29.0

* [Fixed] Fix defaults for `collect_default_metrics` JMX config option. See [#9441](https://github.com/DataDog/integrations-core/pull/9441).
* [Fixed] Fix JMX config spec. See [#9364](https://github.com/DataDog/integrations-core/pull/9364).

## 1.4.0 / 2021-03-30 / Agent 7.28.0

* [Added] Add 'DelayQueueSize'. See [#9033](https://github.com/DataDog/integrations-core/pull/9033).
* [Added] Add 'RequestHandlerAvgIdlePercent' as a 'OneMinuteRate'. See [#9032](https://github.com/DataDog/integrations-core/pull/9032).

## 1.3.1 / 2021-03-07 / Agent 7.27.0

* [Fixed] Bump minimum base package version. See [#8443](https://github.com/DataDog/integrations-core/pull/8443).

## 1.3.0 / 2020-12-11 / Agent 7.25.0

* [Added] Document new collect_default_jvm_metrics flag for JMXFetch integrations. See [#8153](https://github.com/DataDog/integrations-core/pull/8153).

## 1.2.0 / 2020-10-31 / Agent 7.24.0

* [Added] [doc] Add encoding in log config sample. See [#7708](https://github.com/DataDog/integrations-core/pull/7708).

## 1.1.3 / 2020-09-21 / Agent 7.23.0

* [Fixed] Use consistent formatting for boolean values. See [#7405](https://github.com/DataDog/integrations-core/pull/7405).

## 1.1.2 / 2020-08-10 / Agent 7.22.0

* [Fixed] Update logs config service field to optional. See [#7209](https://github.com/DataDog/integrations-core/pull/7209).
* [Fixed] Add new_gc_metrics to all jmx integrations. See [#7073](https://github.com/DataDog/integrations-core/pull/7073).

## 1.1.1 / 2020-06-29 / Agent 7.21.0

* [Fixed] Fix template specs typos. See [#6912](https://github.com/DataDog/integrations-core/pull/6912).
* [Fixed] Adjust jmxfetch config. See [#6864](https://github.com/DataDog/integrations-core/pull/6864).

## 1.1.0 / 2020-05-17 / Agent 7.20.0

* [Added] Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).
* [Added] Add rmi_connection_timeout & rmi_client_timeout to config spec. See [#6459](https://github.com/DataDog/integrations-core/pull/6459).
* [Added] Add default template to openmetrics & jmx config. See [#6328](https://github.com/DataDog/integrations-core/pull/6328).

## 1.0.0 / 2020-04-03 / Agent 7.19.0

* [Added] Add Confluent Platform new integration. See [#5733](https://github.com/DataDog/integrations-core/pull/5733).

