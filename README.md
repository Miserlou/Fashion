<p align="center">
    <img src="https://i.imgur.com/DpAUHQv.png" alt="Fashion: python openfaas" />
</p>

# Fashion [![Python 3](https://img.shields.io/badge/Python-3-brightgreen.svg)](https://github.com/Miserlou/Fashion)
### aka, python-openfaas

_Work in progress!_

**Fashion** is a library for using [OpenFaaS](https://openfaas.com) functions in a Pythonic way. Fashion functions run inside their own Docker containers in your cluster, but act like local functions in your application's code! **Cool!**

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
    - [Callbacks](#callbacks)
    - [Instance Type Limiting / Automatic Cost Optimization](#instance-type-limiting--automatic-cost-optimization)
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
Functions can be chained together without friction:

```python
from fashion import leftpad, figlet
figlet(leftpad("Hello!"))
#  _                _   _      _ _       _ _
# ( )              | | | | ___| | | ___ | ( )
# |/               | |_| |/ _ \ | |/ _ \| |/
#                  |  _  |  __/ | | (_) |_|
#                  |_| |_|\___|_|_|\___/(_)
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
fashion.async_trigger("leftpad", "Hello!") # "6a3ae7fb-a8ee-4988-b7de-e3b81d1aed65"
```

#### Callbacks

Async functions can have their results sent to callback URLs and other OpenFaaS functions. For example, you can send to a pastebin like this:

```python
from fashion import async_leftpad
async_leftpad("Hello", callback_url="https://postb.in/b/1269724059086-0568930923473")
```

or to another OpenFaaS function like this:

```python
from fashion import async_leftpad
async_leftpad("Hello", callback_function="figlet")
```

#### Instance Type Limiting / Automatic Cost Optimization

An interesting use of this is limiting execution of functions to **certain instance types**. For instance, if this is included in an `update_model` function definition:

```yaml
#update_model.yml
  [..]
   constraints:
     - "node.labels.instance_type == gpu"
```

Then you can write code which is **automatically cost-optimized** when it executes:

```python
# Runs on expensive GPU instance
from fashion import update_model

# Runs on cheap CPU instance
from fashion import send_result_email

result = update_model(input)
send_email(result)
# Email sent!
```

### Other OpenFaaS utilities
You can use Fashion to progromatically get information about all your OpenFaaS functions like so:

```python
import fashion
fashion.system_functions()
```

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