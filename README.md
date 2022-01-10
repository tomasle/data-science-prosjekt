# Data Science template

A template for data science projects based on Cookiecutter Data Science https://drivendata.github.io/cookiecutter-data-science/. A project is structured as follows:

- /data/ Any raw data that cannot be pulled on-the-fly
- /notebooks/ Jupyter notebooks for explorative analysis, prototyping
- /src/ Scripts containing reusable production-ready functions
- /src/data Scripts used to get data from external sources

## How to use this repository

- Fork the repository into your own (only one per team)
- Go to "Settings" in your repository, choose "Manage access", and use the button "Add people" to add your teammates to your repository.
- Checkout the repository locally
- Create a branch and start working

## Merging your work

- *Recommendation* Keep only finished work in main, all prototyping is done in branches
- Pull and merge the latest changes from main into your local branch
  ```
  git pull
  git merge main
  ```
- Push your local branch to the remote
  `git push` (`git push -u origin branch_name`)
- Create a PR on Github
- Request a code review from one of your teammates
- Merge PR into main after approval

## Projects

1. **Time series** /data/ contains time series data from 5 traffic measuring stations along the E6 for the year 2019 from https://www.vegvesen.no/trafikkdata/. Carry out an analysis of this data, including hypotheses on potential seasonal patterns and suggestions on how to validate or reject your hypotheses.
2. **Geospatial** Carry out an analysis of traffic accidents in Norway. Which factors can be attributed to the different degrees of severity?
  - Dødsulykke
  - Alvorlig skade (meget alvorlig eller alvorlig)
  - Ingen skade (lettere eller uskadd)
