<p align="center">
    <img src="https://i.imgur.com/DpAUHQv.png" alt="Fashion: python openfaas" />
</p>

# Fashion [![Python 3](https://img.shields.io/badge/Python-3-brightgreen.svg)](https://github.com/Miserlou/Fashion)
### aka, python-openfaas

_Work in progress!_

**Fashion** is a library for using [OpenFaaS](https://openfaas.com) functions in a Pythonic way.

For instance, let's imagine that we've installed the `figlet` function from the OpenFaaS function store. To call it from our application, we can simply:

```python
from fashion import figlet
hi = figlet("Hello, world!")
#  _   _      _ _                             _     _ _
# | | | | ___| | | ___    __      _____  _ __| | __| | |
# | |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` | |
# |  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |_|
# |_| |_|\___|_|_|\___( )   \_/\_/ \___/|_|  |_|\__,_(_)
#                    |/
```

Fashion doesn't need any prior knowledge of the OpenFaas function, you can simply call it as if it were a local function!

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
  - [Ordinary Usage](#ordinary-usage)
  - [Async](#async)
  - [Other OpenFaaS utilities](#other-openfaas-utilities)
  - [Settings](#settings)
- [Related Projects](#related-projects)
- [TODO](#todo)
- [License](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Installation

(Coming [soon](https://github.com/pypa/warehouse/issues/6725)!)
```
pip install fashion
```

## Usage

### Ordinary Usage

Fashion is very easy to use, just import your OpenFaaS function as if it were native!

For instance:
```python
from fashion import leftpad
leftpad("Hello!") # "      Hello!"
```

Alternately, you can use Fashion's `trigger` function directly, like so:

```python
import fashion
fashion.trigger("leftpad", "Hello!") #"      Hello!"
```

### Async
_(Still working on the interface for this, hang on a bit!)_
Similarly, you can use OpenFaaS functions asyncronously. To invoke an async function, import it with the prefix `async_` like so:

```python
from fashion import async_leftpad
async_leftpad("Hello!") # "6a3ae7fb-a8ee-4988-b7de-e3b81d1aed65"
```

or the old fashioned way:

```python
import fashion
fashion.trigger("leftpad", "Hello!") # "6a3ae7fb-a8ee-4988-b7de-e3b81d1aed65"
```

### Other OpenFaaS utilities
`XXX TODO XXX`

### Settings
You can configure your endpoints and other variables like so:

```python
import fashion

fashion.GATEWAY_URL = "http://internal.network.location"
fashion.GATEWAY_PORT = 8081
fashion.TIMEOUT_SECONDS = 30
```

## Related Projects
 * [Zappa](https://github.com/Miserlou/Zappa) - Python's Serverless Framework for AWS Lambda

## TODO
  * Tests
  * Async
  * Auth/HMAC settings
  * Turn left__pad into left-pad invocation

## License

(C) Rich Jones 2019, MIT License.