# CHANGELOG - TLS

## 2.5.0 / 2021-05-27 / Agent 7.28.1

* [Added] Add runtime configuration validation. See [#8996](https://github.com/DataDog/integrations-core/pull/8996).
* [Fixed] Do not use check inheritance. See [#9433](https://github.com/DataDog/integrations-core/pull/9433).

## 2.4.0 / 2021-04-19 / Agent 7.28.0

* [Added] Add an option to send certificate duration. See [#9067](https://github.com/DataDog/integrations-core/pull/9067). Thanks [lindleywhite](https://github.com/lindleywhite).
* [Added] Upgrade cryptography to 3.4.6 on Python 3. See [#8764](https://github.com/DataDog/integrations-core/pull/8764).
* [Fixed] Refactor TLS check. See [#8792](https://github.com/DataDog/integrations-core/pull/8792).
* [Fixed] Add more debug lines. See [#8787](https://github.com/DataDog/integrations-core/pull/8787).

## 2.3.0 / 2021-03-07 / Agent 7.27.0

* [Fixed] Include validate_cert in backwards compatibility remapper. See [#8543](https://github.com/DataDog/integrations-core/pull/8543).
* [Security] Upgrade cryptography python package. See [#8611](https://github.com/DataDog/integrations-core/pull/8611).

## 2.2.0 / 2021-02-03

* [Added] Implement AIA chasing. See [#8521](https://github.com/DataDog/integrations-core/pull/8521).
* [Fixed] Remove outdated description of `local_cert_path` option. See [#8500](https://github.com/DataDog/integrations-core/pull/8500).
* [Fixed] Bump minimum package. See [#8443](https://github.com/DataDog/integrations-core/pull/8443).

## 2.1.0 / 2021-01-28

* [Security] Upgrade cryptography python package. See [#8476](https://github.com/DataDog/integrations-core/pull/8476).

## 2.0.0 / 2021-01-25

* [Changed] Update TLS check to use TLS context wrapper. See [#8230](https://github.com/DataDog/integrations-core/pull/8230).

## 1.8.0 / 2020-10-31 / Agent 7.24.0

* [Security] Upgrade `cryptography` dependency. See [#7869](https://github.com/DataDog/integrations-core/pull/7869).

## 1.7.0 / 2020-10-14

* [Added] Adding debug logging to tls check. See [#7664](https://github.com/DataDog/integrations-core/pull/7664).

## 1.6.0 / 2020-09-21 / Agent 7.23.0

* [Added] Add config spec. See [#7529](https://github.com/DataDog/integrations-core/pull/7529).

## 1.5.0 / 2020-05-17 / Agent 7.20.0

* [Added] Allow optional dependency installation for all checks. See [#6589](https://github.com/DataDog/integrations-core/pull/6589).

## 1.4.1 / 2020-02-12 / Agent 7.18.0

* [Fixed] Don't rely on file extension for local cert loading. See [#5694](https://github.com/DataDog/integrations-core/pull/5694).

## 1.4.0 / 2020-01-13 / Agent 7.17.0

* [Added] Use lazy logging format. See [#5398](https://github.com/DataDog/integrations-core/pull/5398).

## 1.3.0 / 2019-12-02 / Agent 7.16.0

* [Added] Upgrade cryptography to 2.8. See [#5047](https://github.com/DataDog/integrations-core/pull/5047).

## 1.2.0 / 2019-07-04 / Agent 6.13.0

* [Added] Update cryptography version. See [#4000](https://github.com/DataDog/integrations-core/pull/4000).

## 1.1.0 / 2019-06-24

* [Added] Allow certificate validation to be completely disabled. See [#3966](https://github.com/DataDog/integrations-core/pull/3966).

## 1.0.0 / 2019-04-22 / Agent 6.12.0

* [Added] Add TLS integration. See [#3256](https://github.com/DataDog/integrations-core/pull/3256).

