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
import asyncio
from finolog.client import FinologClient


async def main():
    client = FinologClient(api_token='YOUR TOKEN', biz_id=123)
    contractors, documents = await asyncio.gather(
        client.contractor.get_contractors(), client.document.get_documents()
    )
    print(f"Documents: {documents}\n" f"Contractors: {contractors}")
    await client.close()

if __name__ == "__main__":
    asyncio.run(main())

```


## Bugs

If you have any problems, please create Issues [here](https://github.com/RTHeLL/finolog-sdk/issues)  
