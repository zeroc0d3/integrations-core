# PostgreSQL Integration

![PostgreSQL Graph][1]

<div class="alert alert-info">This page describes the Postgres agent integration; if you are looking for the Database Monitoring product for Postgres, see <a href="https://docs.datadoghq.com/database_monitoring" target="_blank">Datadog Database Monitoring</a>.</div>

## Overview

Get metrics from PostgreSQL in real time to:

- Visualize and monitor PostgreSQL states.
- Received notifications about PostgreSQL failovers and events.

## Setup

### Installation

The PostgreSQL check is packaged with the Agent. To start gathering your PostgreSQL metrics and logs, [install the Agent][2].

### Configuration

#### Prepare Postgres

To get started with the PostgreSQL integration, create a read-only `datadog` user with proper access to your PostgreSQL server. Start `psql` on your PostgreSQL database.

For PostgreSQL version 10 and above, run:

```shell
create user datadog with password '<PASSWORD>';
grant pg_monitor to datadog;
grant SELECT ON pg_stat_database to datadog;
```

For older PostgreSQL versions, run:

```shell
create user datadog with password '<PASSWORD>';
grant SELECT ON pg_stat_database to datadog;
```

To verify the permissions are correct, run the following command:

```shell
psql -h localhost -U datadog postgres -c \
"select * from pg_stat_database LIMIT(1);" \
&& echo -e "\e[0;32mPostgres connection - OK\e[0m" \
|| echo -e "\e[0;31mCannot connect to Postgres\e[0m"
```

When it prompts for a password, enter the one used in the first command.

**Note**: For PostgreSQL versions 9.6 and below, run the following and create a `SECURITY DEFINER` to read from `pg_stat_activity`.

```shell
CREATE FUNCTION pg_stat_activity() RETURNS SETOF pg_catalog.pg_stat_activity AS
$$ SELECT * from pg_catalog.pg_stat_activity; $$
LANGUAGE sql VOLATILE SECURITY DEFINER;

CREATE VIEW pg_stat_activity_dd AS SELECT * FROM pg_stat_activity();
grant SELECT ON pg_stat_activity_dd to datadog;
```

<!-- xxx tabs xxx -->
<!-- xxx tab "Host" xxx -->

**Note**: When generating custom metrics that require querying additional tables, you may need to grant the `SELECT` permission on those tables to the `datadog` user. Example: `grant SELECT on <TABLE_NAME> to datadog;`. Check the [FAQ section](#faq) for more information.

#### Host

To configure this check for an Agent running on a host:

##### Metric collection

1. Edit the `postgres.d/conf.yaml` file to point to your `host` / `port` and set the masters to monitor. See the [sample postgres.d/conf.yaml][3] for all available configuration options.

   ```yaml
   init_config:

   instances:
     ## @param host - string - required
     ## The hostname to connect to.
     ## NOTE: Even if the server name is "localhost", the agent connects to
     ## PostgreSQL using TCP/IP, unless you also provide a value for the sock key.
     #
     - host: localhost

       ## @param port - integer - required
       ## Port to use when connecting to PostgreSQL.
       #
       port: 5432

       ## @param user - string - required
       ## Datadog Username created to connect to PostgreSQL.
       #
       username: datadog

       ## @param pass - string - required
       ## Password associated with the Datadog user.
       #
       password: "<PASSWORD>"

       ## @param dbname - string - optional - default: postgres
       ## Name of the PostgresSQL database to monitor.
       ## Note: If omitted, the default system postgres database is queried.
       #
       dbname: "<DB_NAME>"
   ```

2. [Restart the Agent][4].

##### Trace collection

Datadog APM integrates with Postgres to see the traces across your distributed system. Trace collection is enabled by default in the Datadog Agent v6+. To start collecting traces:

1. [Enable trace collection in Datadog][5].
2. [Instrument your application that makes requests to Postgres][6].

##### Log collection

_Available for Agent versions >6.0_

PostgreSQL default logging is to `stderr`, and logs do not include detailed information. It is recommended to log into a file with additional details specified in the log line prefix. Refer to the PostgreSQL [documentation][16] on this topic for additional details.

1. Logging is configured within the file `/etc/postgresql/<VERSION>/main/postgresql.conf`. For regular log results, including statement outputs, uncomment the following parameters in the log section:

   ```conf
     logging_collector = on
     log_directory = 'pg_log'  # directory where log files are written,
                               # can be absolute or relative to PGDATA
     log_filename = 'pg.log'   # log file name, can include pattern
     log_statement = 'all'     # log all queries
     #log_duration = on
     log_line_prefix= '%m [%p] %d %a %u %h %c '
     log_file_mode = 0644
     ## For Windows
     #log_destination = 'eventlog'
   ```

2. To gather detailed duration metrics and make them searchable in the Datadog interface, they should be configured inline with the statement themselves. See below for the recommended configuration differences from above and note that both `log_statement` and `log_duration` options are commented out. See discussion on this topic [here][17].

    This config logs all statements, but to reduce the output to those which have a certain duration, set the `log_min_duration_statement` value to the desired minimum duration (in milliseconds):

   ```conf
     log_min_duration_statement = 0    # -1 is disabled, 0 logs all statements
                                       # and their durations, > 0 logs only
                                       # statements running at least this number
                                       # of milliseconds
     #log_statement = 'all'
     #log_duration = on
   ```

3. Collecting logs is disabled by default in the Datadog Agent, enable it in your `datadog.yaml` file:

   ```yaml
   logs_enabled: true
   ```

4. Add and edit this configuration block to your `postgres.d/conf.yaml` file to start collecting your PostgreSQL logs:

   ```yaml
   logs:
     - type: file
       path: "<LOG_FILE_PATH>"
       source: postgresql
       service: "<SERVICE_NAME>"
       #To handle multi line that starts with yyyy-mm-dd use the following pattern
       #log_processing_rules:
       #  - type: multi_line
       #    pattern: \d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])
       #    name: new_log_start_with_date
   ```

      Change the `service` and `path` parameter values to configure for your environment. See the [sample postgres.d/conf.yaml][3] for all available configuration options.

5. [Restart the Agent][4].

<!-- xxz tab xxx -->
<!-- xxx tab "Docker" xxx -->

#### Docker

To configure this check for an Agent running on a container:

##### Metric collection

Set [Autodiscovery Integrations Templates][20] as Docker labels on your application container:

```yaml
LABEL "com.datadoghq.ad.check_names"='["postgres"]'
LABEL "com.datadoghq.ad.init_configs"='[{}]'
LABEL "com.datadoghq.ad.instances"='[{"host":"%%host%%", "port":5432,"username":"datadog","password":"<PASSWORD>"}]'
```

##### Log collection


Collecting logs is disabled by default in the Datadog Agent. To enable it, see the [Docker log collection documentation][21].

Then, set [Log Integrations][22] as Docker labels:

```yaml
LABEL "com.datadoghq.ad.logs"='[{"source":"postgresql","service":"postgresql"}]'
```

##### Trace collection

APM for containerized apps is supported on Agent v6+ but requires extra configuration to begin collecting traces.

Required environment variables on the Agent container:

| Parameter            | Value                                                                      |
| -------------------- | -------------------------------------------------------------------------- |
| `<DD_API_KEY>` | `api_key`                                                                  |
| `<DD_APM_ENABLED>`      | true                                                              |
| `<DD_APM_NON_LOCAL_TRAFFIC>`  | true |

See [Tracing Docker Applications][31] for a complete list of available environment variables and configuration.

Then, [instrument your application container that makes requests to Postgres][32] and set `DD_AGENT_HOST` to the name of your Agent container.


<!-- xxz tab xxx -->
<!-- xxx tab "Kubernetes" xxx -->

#### Kubernetes

To configure this check for an Agent running on Kubernetes:

##### Metric collection

Set [Autodiscovery Integrations Templates][23] as pod annotations on your application container. Aside from this, templates can also be configured with [a file, a configmap, or a key-value store][24].

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: postgres
  annotations:
    ad.datadoghq.com/postgresql.check_names: '["postgres"]'
    ad.datadoghq.com/postgresql.init_configs: '[{}]'
    ad.datadoghq.com/postgresql.instances: |
      [
        {
          "host": "%%host%%",
          "port":"5432",
          "username":"datadog",
          "password":"<PASSWORD>"
        }
      ]
spec:
  containers:
    - name: postgres
```

##### Log collection


Collecting logs is disabled by default in the Datadog Agent. To enable it, see the [Kubernetes log collection documentation][25].

Then, set [Log Integrations][26] as pod annotations. This can also be configured with [a file, a configmap, or a key-value store][27].

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: postgres
  annotations:
    ad.datadoghq.com/postgres.logs: '[{"source":"postgresql","service":"<SERVICE_NAME>"}]'
spec:
  containers:
    - name: postgres
```

##### Trace collection

APM for containerized apps is supported on hosts running Agent v6+ but requires extra configuration to begin collecting traces.

Required environment variables on the Agent container:

| Parameter            | Value                                                                      |
| -------------------- | -------------------------------------------------------------------------- |
| `<DD_API_KEY>` | `api_key`                                                                  |
| `<DD_APM_ENABLED>`      | true                                                              |
| `<DD_APM_NON_LOCAL_TRAFFIC>`  | true |

See [Tracing Kubernetes Applications][33] and the [Kubernetes DaemonSet Setup][34] for a complete list of available environment variables and configuration.

Then, [instrument your application container that makes requests to Postgres][32].

<!-- xxz tab xxx -->
<!-- xxx tab "ECS" xxx -->

#### ECS

To configure this check for an Agent running on ECS:

##### Metric collection

Set [Autodiscovery Integrations Templates][28] as Docker labels on your application container:

```json
{
  "containerDefinitions": [{
    "name": "postgres",
    "image": "postgres:latest",
    "dockerLabels": {
      "com.datadoghq.ad.check_names": "[\"postgres\"]",
      "com.datadoghq.ad.init_configs": "[{}]",
      "com.datadoghq.ad.instances": "[{\"host\":\"%%host%%\", \"port\":5432,\"username\":\"datadog\",\"password\":\"<PASSWORD>\"}]"
    }
  }]
}
```

##### Log collection


Collecting logs is disabled by default in the Datadog Agent. To enable it, see the [ECS log collection documentation][29].

Then, set [Log Integrations][30] as Docker labels:

```json
{
  "containerDefinitions": [{
    "name": "postgres",
    "image": "postgres:latest",
    "dockerLabels": {
      "com.datadoghq.ad.logs": "[{\"source\":\"postgresql\",\"service\":\"postgresql\"}]"
    }
  }]
}
```

##### Trace collection

APM for containerized apps is supported on Agent v6+ but requires extra configuration to begin collecting traces.

Required environment variables on the Agent container:

| Parameter            | Value                                                                      |
| -------------------- | -------------------------------------------------------------------------- |
| `<DD_API_KEY>` | `api_key`                                                                  |
| `<DD_APM_ENABLED>`      | true                                                              |
| `<DD_APM_NON_LOCAL_TRAFFIC>`  | true |

See [Tracing Docker Applications][31] for a complete list of available environment variables and configuration.

Then, [instrument your application container that makes requests to Postgres][32] and set `DD_AGENT_HOST` to the [EC2 private IP address][33].

<!-- xxz tab xxx -->
<!-- xxz tabs xxx -->

### Validation

[Run the Agent's status subcommand][9] and look for `postgres` under the Checks section.

## Data Collected

Some of the metrics listed below require additional configuration, see the [sample postgres.d/conf.yaml][3] for all configurable options.

### Metrics

See [metadata.csv][10] for a list of metrics provided by this integration.

### Events

The PostgreSQL check does not include any events.

### Service Checks

See [service_checks.json][34] for a list of service checks provided by this integration.

## Troubleshooting

Need help? Contact [Datadog support][35].

## Further Reading

Additional helpful documentation, links, and articles:

### FAQ

- [PostgreSQL custom metric collection explained][11]

### Blog posts

- [100x faster Postgres performance by changing 1 line][12]
- [Key metrics for PostgreSQL monitoring][13]
- [Collecting metrics with PostgreSQL monitoring tools][14]
- [How to collect and monitor PostgreSQL data with Datadog][15]

[1]: https://raw.githubusercontent.com/DataDog/integrations-core/master/postgres/images/postgresql_dashboard.png
[2]: https://app.datadoghq.com/account/settings#agent
[3]: https://github.com/DataDog/integrations-core/blob/master/postgres/datadog_checks/postgres/data/conf.yaml.example
[4]: https://docs.datadoghq.com/agent/guide/agent-commands/#start-stop-and-restart-the-agent
[5]: https://docs.datadoghq.com/tracing/send_traces/
[6]: https://docs.datadoghq.com/tracing/setup/
[7]: https://docs.datadoghq.com/agent/kubernetes/integrations/
[8]: https://docs.datadoghq.com/agent/kubernetes/log/
[9]: https://docs.datadoghq.com/agent/guide/agent-commands/#agent-status-and-information
[10]: https://github.com/DataDog/integrations-core/blob/master/postgres/metadata.csv
[11]: https://docs.datadoghq.com/integrations/faq/postgres-custom-metric-collection-explained/
[12]: https://www.datadoghq.com/blog/100x-faster-postgres-performance-by-changing-1-line
[13]: https://www.datadoghq.com/blog/postgresql-monitoring
[14]: https://www.datadoghq.com/blog/postgresql-monitoring-tools
[15]: https://www.datadoghq.com/blog/collect-postgresql-data-with-datadog
[16]: https://www.postgresql.org/docs/11/runtime-config-logging.html
[17]: https://www.postgresql.org/message-id/20100210180532.GA20138@depesz.com
[18]: https://docs.datadoghq.com/agent/kubernetes/apm/?tab=java
[19]: https://docs.datadoghq.com/agent/kubernetes/daemonset_setup/?tab=k8sfile#apm-and-distributed-tracing
[20]: https://docs.datadoghq.com/agent/docker/integrations/?tab=docker
[21]: https://docs.datadoghq.com/agent/docker/log/?tab=containerinstallation#installation
[22]: https://docs.datadoghq.com/agent/docker/log/?tab=containerinstallation#log-integrations
[23]: https://docs.datadoghq.com/agent/kubernetes/integrations/?tab=kubernetes
[24]: https://docs.datadoghq.com/agent/kubernetes/integrations/?tab=kubernetes#configuration
[25]: https://docs.datadoghq.com/agent/kubernetes/log/?tab=containerinstallation#setup
[26]: https://docs.datadoghq.com/agent/docker/log/?tab=containerinstallation#log-integrations
[27]: https://docs.datadoghq.com/agent/kubernetes/log/?tab=daemonset#configuration
[28]: https://docs.datadoghq.com/agent/docker/integrations/?tab=docker
[29]: https://docs.datadoghq.com/agent/amazon_ecs/logs/?tab=linux
[30]: https://docs.datadoghq.com/agent/docker/log/?tab=containerinstallation#log-integrations
[31]: https://docs.datadoghq.com/agent/amazon_ecs/logs/?tab=linux
[32]: https://docs.datadoghq.com/agent/docker/log/?tab=containerinstallation#log-integrations
[33]: https://docs.datadoghq.com/agent/amazon_ecs/apm/?tab=ec2metadataendpoint#setup
[34]: https://github.com/DataDog/integrations-core/blob/master/postgres/assets/service_checks.json
[35]: https://docs.datadoghq.com/help
