# Wine Information

The Wine Information service is dedicated to ensuring the accessibility of wine data within our system. This service is the key to providing comprehensive wine-related information to our users.

## Deployment Instructions

To deploy the wine  service, start by copying the example application configuration:

```sh
cp example.app.yml app.yml
```

Next, you need to update the following variables in the `.env` file:

```yml
USER_MICROSERVICES: "YOUR-URL-USER-MANAGMENT"
SPANNER_INSTANCE: "YOUR-SPANNER_INSTANCE"
SPANNER_DATABASE: "YOUR-SPANNER_DATABASE"
```

Replace the placeholders (`YOUR-URL-USER-MANAGMENT`, `YOUR-SPANNER_INSTANCE`, and `YOUR-WINE-DATABASE`) with your actual service URL, Spanner instance name, and Spanner database name, respectively.

For a more comprehensive guide on deployment, including detailed steps and additional configurations, please refer to our [App Engine Deployment Guide](https://github.com/Vintellect/deploy_backend_guide/blob/fd5863fb17d5386cdf16eb43cf58b0c6b8cc571f/Microserivces_guide.md).
