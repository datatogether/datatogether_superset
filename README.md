# Superset for DataTogether

This is a Heroku-hosted Superset instance for visualizing data from the
DataTogether project.

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
