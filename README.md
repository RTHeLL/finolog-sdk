# Finolog Python API

Wrapper for working with Finolog service API

[![N|Solid](https://img.shields.io/pypi/pyversions/finolog-sdk.svg)](https://pypi.python.org/pypi/finolog-sdk)

### Installation
You can install or upgrade package with:
```
$ pip install finolog-sdk --upgrade
```
Or you can install from source with:
```
$ git clone https://github.com/RTHeLL/finolog-sdk
$ cd finolog-sdk
$ python setup.py install
```
...or install from source buth with pip
```
$ pip install git+https://github.com/RTHeLL/finolog-sdk
```
### Example

```python
from finolog.services import FinologService 


def main():
    client = FinologService(api_token='YOUR TOKEN', biz_id=123)
    documents = client.document.get_documents()
    print(documents)


main()
```


## Bugs

If you have any problems, please create Issues [here](https://github.com/RTHeLL/finolog-sdk/issues)  
