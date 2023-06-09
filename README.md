# Grai Actions - Server

This Github action allows you to run updates or tests against Grai server.

## Getting Started

A basic example:

```
name: Example Push Action

on: push

jobs:
  create_run:
    runs-on: ubuntu-latest
    name: Update Grai
    steps:
      - name: Checkout
        uses: actions/checkout@v2

      - name: Create Run
        uses: grai-io/grai-actions-server@master
        with:
          api-key: ${{ secrets.GRAI_API_KEY }}
          action: update
          connection_id: ${{ secrets.GRAI_DATABASE_CONNECTION_ID }}
```

See the three example pull requests for more examples.

## Fields

### Api Key

Set to a Grai Api Key. To generate an Api key, go to settings from the profile menu, followed by Api Keys and choose Add API Key.

### Action

One of `update` or `tests`. Defaults to `update`, so is optional.

### Connection Id

Set to the UUID of an existing Connection. To find the connection id, navigate to connections and click on a connection, the UUID is then the last part of the url, after `.../connections/`. Connection Id is optional, if you don't have an existing connection you can use the following fields instead.

### Connector Name

Required if a connection id is not provided. Choose from the available connectors.

### Connector Namespace

You can supply a namespace for the connection, if no value is provided the field defaults to `default`.

### Connector Metadata

Provide a JSON string representing the connection metadata. The required keys varies for each connector, see bellow.

### Connector Secrets

Provide a JSON string representing the connection secrets. The required keys varies for each connector, see bellow.

### File Path

Provide the path to a file you would like to upload, for example a `manifest.json` file generated by dbt.

## Connector Metadata and Secrets

### Google Bigquery

| Field       | Value                                                                                                                 | Example     |
| ----------- | --------------------------------------------------------------------------------------------------------------------- | ----------- |
| project     | GCP project id                                                                                                        | grai-demo   |
| dataset     | Bigquery Dataset Id                                                                                                   | jaffle_shop |
| credentials | JSON credentials for service account, see [Credentials](https://docs.grai.io/web-app-connectors/bigquery#credentials) |             |

### Microsoft SQL Server

| Field    | Value             | Example                                                  |
| -------- | ----------------- | -------------------------------------------------------- |
| host     | Database host     | sample-database.cudyk77thtpt.us-west-2.rds.amazonaws.com |
| port     | Database port     | 5432                                                     |
| database | Database name     | jaffle_shop                                              |
| user     | Database user     |                                                          |
| password | Database password |                                                          |

### MySQL

### PostgreSQL

| Field    | Value             | Example                                                  |
| -------- | ----------------- | -------------------------------------------------------- |
| host     | Database host     | sample-database.cudyk77thtpt.us-west-2.rds.amazonaws.com |
| port     | Database port     | 5432                                                     |
| dbname   | Database Name     | jaffle_shop                                              |
| user     | Database user     |                                                          |
| password | Database password |                                                          |

### Snowflake

| Field     | Value                                                                   | Example          |
| --------- | ----------------------------------------------------------------------- | ---------------- |
| account   | Snowflake account, the characters in front of `.snowflakecomputing.com` | hujwihs-hab96881 |
| user      | Database user                                                           |                  |
| role      | Snowflake role to use                                                   | READ_ONLY        |
| warehouse | Snowflake warehouse to use                                              | COMPUTE_WH       |
| database  | Snowflake database                                                      |                  |
| schema    | Snowflake schema to use (optional)                                      |                  |
| password  | Database password                                                       |                  |

### Fivetran

| Field           | Value                                       | Example |
| --------------- | ------------------------------------------- | ------- |
| api_key         | Fivetran api key, see below                 |         |
| namespaces      | Optional                                    |         |
| endpoint        | Optional endpoint if self hosting fivetran  |         |
| limit           | Limit the number of rows returned, optional | 10000   |
| parallelization | Run connector in parallel, optional         | 10      |
| api_secret      | Fivetran api secret, see below              |         |

See [https://fivetran.com/docs/rest-api/getting-started](https://fivetran.com/docs/rest-api/getting-started) to generate an api key.
