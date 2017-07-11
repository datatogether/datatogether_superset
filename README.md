# Superset for DataTogether

[**Heroku**][] is a platform for easily hosting apps. [**Superset**][] is a
modern, enterprise-ready business intelligence web application.

   [Heroku]: https://www.heroku.com/about
   [Superset]: https://medium.com/airbnb-engineering/caravel-airbnb-s-data-exploration-platform-15a72aa610e5

This project is for hosting DataTogether's Superset instance on Heroku, for
visualizing live project data in dashboards.

## Requirements

* virtualenvwrapper.sh (recommended)
* Superset's [OS dependencies][]

   [OS dependecies]: https://superset.incubator.apache.org/installation.html#os-dependencies

## Usage

```
# Setup
mkvirtualenv datatogether-superset --python=`which python3`
make pip-install
make setup
```

```
# Running
workon datatogether-superset
make run
```

## Notes

* `master` branch is auto-deployed to Heroku.
* We use the [Probot: Configurer plugin][configurer] to allow repo settings to be
  changes via pull request.

   [configurer]: https://github.com/apps/configurer
