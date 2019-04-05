# Run the preprocessing


 ### Clone the metadata repository
```console
$ git clone --depth=1 https://github.com/paneldata/soep-core.git
$ cd soep-core/
```


 ### Requirements and dependencies
```console
$ sudo apt-get install -y python3.6 python3.6-dev python3-pip
$ pip install --upgrade --user pipenv
$ pipenv --version
pipenv, version 2018.11.26
$ pipenv shell
# install package dependencies
$ (soep-core) pipenv install
Installing dependencies from Pipfile.lock (dcf893)…
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 45/45 — 00:00:04
  
$ (soep-core) pipenv graph
ddi==0.1.0
  - jinja2 [required: Any, installed: 2.10]
    - MarkupSafe [required: >=0.23, installed: 1.1.1]
  - lxml [required: Any, installed: 4.3.2]
  - pandas [required: Any, installed: 0.24.2]
    - numpy [required: >=1.12.0, installed: 1.16.2]
    - python-dateutil [required: >=2.5.0, installed: 2.8.0]
      - six [required: >=1.5, installed: 1.12.0]
    - pytz [required: >=2011k, installed: 2018.9]
  - pyyaml [required: Any, installed: 5.1]
  - scipy [required: Any, installed: 1.2.1]
    - numpy [required: >=1.8.2, installed: 1.16.2]

# ...

$ (soep-core) goodtables --version
2.1.1
```

### Validate the metadata 
```console
$ pipenv shell

# Run structure and schema validation 
$ (soep-core) goodtables metadata/datapackage.json

# Run relation validations
$ (soep-core) python lib_py/validation/relations.py answers
$ (soep-core) python lib_py/validation/relations.py datasets
...
```

### Run the preprocessing pipeline 
```console
$ pipenv shell
$ (soep-core) python lib_py/fill_ddionrails.py
```
