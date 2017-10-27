# Superset for DataTogether

<!-- Repo Badges for: Github Project, Slack, License-->

[![GitHub](https://img.shields.io/badge/project-Data_Together-487b57.svg?style=flat-square)](http://github.com/datatogether)
[![Slack](https://img.shields.io/badge/slack-Archivers-b44e88.svg?style=flat-square)](https://archivers-slack.herokuapp.com/)
[![License](https://img.shields.io/github/license/datatogether/datatogether_superset.svg)](./LICENSE) 

Project for hosting DataTogether's Superset instance on Heroku, for visualizing 
live project data in dashboards.

**[Heroku][]** is a platform for easily hosting web apps.

**[Superset][]** is a modern, enterprise-ready business intelligence web
application.

   [Heroku]: https://www.heroku.com/about
   [Superset]: https://medium.com/airbnb-engineering/caravel-airbnb-s-data-exploration-platform-15a72aa610e5

## License & Copyright

Copyright (C) 2017 Data Together  
This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Affero General Public License as published by the Free Software
Foundation, version 3.0.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.

See the [`LICENSE`](./LICENSE) file for details.

## Getting Involved

We would love involvement from more people! If you notice any errors or would like to submit changes, please see our [Contributing Guidelines](./.github/CONTRIBUTING.md). 

We use GitHub issues for [tracking bugs and feature requests](https://github.com/datatogether/datatogether-superset/issues) and Pull Requests (PRs) for [submitting changes](https://github.com/datatogether/datatogether-superset/pulls)

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
