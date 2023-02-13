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
from finolog.client import FinologClient 


def main():
    client = FinologClient(api_token='YOUR TOKEN', biz_id=123)
    contractors = client.contractor.get_contractors()
    documents = client.document.get_documents()
    print(
        f'Documents: {documents}\n'
        f'Contractors: {contractors}'
    )


main()
```


## Bugs

If you have any problems, please create Issues [here](https://github.com/RTHeLL/finolog-sdk/issues)  
