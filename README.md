# Superset for DataTogether

**[Heroku][]** is a platform for easily hosting web apps.

**[Superset][]** is a modern, enterprise-ready business intelligence web
application.

   [Heroku]: https://www.heroku.com/about
   [Superset]: https://medium.com/airbnb-engineering/caravel-airbnb-s-data-exploration-platform-15a72aa610e5

This project is for hosting DataTogether's Superset instance on Heroku, for
visualizing live project data in dashboards.

## Requirements

* virtualenvwrapper.sh (recommended)
* Heroku CLI (recommended)
* Superset's [OS dependencies][]

   [OS dependencies]: https://superset.incubator.apache.org/installation.html#os-dependencies

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

```
# Heroku setup
heroku addons:create heroku-postgresql
heroku config:set SECRET_KEY=`openssl rand -hex 36
heroku config:set MAPBOX_API_KEY=<acquired-key>
```

## Notes

* `master` branch is auto-deployed to Heroku.
* We use the [Probot: Configurer plugin][configurer] to allow repo
  settings via pull request using [`.github/config.yml`][].
* We use a python package management strategy [explained best by Kenneth
  Reitz][pip-strat]. (A little outdated, but works fine.)

   [configurer]: https://github.com/apps/configurer
   [`.github/config.yml`]: .github/config.yml
   [pip-strat]: https://www.kennethreitz.org/essays/a-better-pip-workflow
