# Data Science template

A template for data science projects based on Cookiecutter Data Science https://drivendata.github.io/cookiecutter-data-science/. A project is structured as follows:

- /data/ Any raw data that cannot be pulled on-the-fly
- /notebooks/ Jupyter notebooks for explorative analysis, prototyping
- /src/ Scripts containing reusable production-ready functions
- /src/data Scripts used to get data from external sources

## Projects

1. **Time series** /data/ contains time series data from 5 traffic measuring stations along the E6 for the year 2019 from https://www.vegvesen.no/trafikkdata/. Carry out an analysis of this data, including hypotheses on potential seasonal patterns and suggestions on how to validate or reject your hypotheses.
2. **Geospatial** Carry out an analysis of traffic accidents in Norway. Which factors can be attributed to the different degrees of severity?
  - Dødsulykke
  - Alvorlig skade (meget alvorlig eller alvorlig)
  - Ingen skade (lettere eller uskadd)
