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
  `git push` (`git push -u origin branch_name` if pushing a new branch)
- Create a PR on Github
- Request a code review from one of your teammates
- Merge PR into main after approval

## Projects

1. **Time series** /data/ contains time series data from 5 traffic measuring stations along the E6 for the year 2019 from https://www.vegvesen.no/trafikkdata/. Carry out an analysis of this data, including hypotheses on potential seasonal patterns and suggestions on how to validate or reject your hypotheses.
2. **Geospatial** Carry out an analysis of traffic accidents in Norway. Which factors can be attributed to the different degrees of severity?
    - Dødsulykke
    - Alvorlig skade (meget alvorlig eller alvorlig)
    - Ingen skade (lettere eller uskadd)

## Conda

To use conda with this repo, follow the instructions given by Conda docs https://docs.conda.io/projects/conda/en/latest/index.html

TL;DR:
- conda env create -f requirements.yml
- conda env export > requirements.yml

Find more commands in the [conda cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)

## Website

To create a simple website to feature your work follow the instructions:
1. Enable GitHub Pages on your repo
2. Alter the code and templates in the "website/" folder to fit your project
  * Change the template.md to use your group name
  * Link to your own notebooks (hint: find them in github, and click "raw" to get the raw link to the notebook, and link this up in the script which compile the site)

### Challenge
1. Save one image of a plot from your notebook, which you feel like displaying (hint: plt.savefig('present_notebook1.png'))
2. Also move all png images to the build/ folder in the github action : .github/workflows/build-site.yml (hint: inspect where the html is moved to the build folder) 
3. Instead of linking to your notebook using a hyperlink, use a clickable image of the saved plot to navigate to your notebook. You may write some html here -> generate img and a tags in the compilation script in the website/
4. OPTIONAL: Make your website look more presentable with some more html and css

## References
- vegdata api
  * datakatalog : https://datakatalogen.vegdata.no/
  * api nettside : https://api.vegdata.no/
  * Boilerplate kode for å hente ut med python finner du i dette repo
- Trafikkdata api : https://www.vegvesen.no/trafikkdata/
- Conda docs https://docs.conda.io/projects/conda/en/latest/index.html#
