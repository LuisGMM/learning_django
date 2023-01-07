# Template

![Tests](https://github.com/LuisGMM/Template/actions/workflows/tests.yml/badge.svg)


# Readme

## Installing

Run the following commands:

```windows shell
py -3.11 -m venv venv  
```

```bash
virtualenv -p /usr/bin/python3.11 venv
```

```bash
source venv/bin/activate
```

```bash
pip install -e .
```

```bash
pip install -r requirements/required.txt
pip install -r requirements/tests.txt
pip install -r requirements/docs.txt
```

To make and see the documentation:

```bash
make docs && google-chrome $(pwd)/docs/build/html/index.html
```
within backbone's project folder. This command will build and open the rendered documentation in the browser.
