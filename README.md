# Fashion [![Python 3](https://img.shields.io/badge/Python-3-brightgreen.svg)](https://github.com/Miserlou/Fashion)
## aka, python-openfaas

**Fashion** is a library for using OpenFaaS functions in a Pythonic way.

For instance, let's imagine that we've installed the "left_pad" function from the OpenFaaS function store. To call it from our application, we can simply:

```
from fashion import left_pad
left_pad("Hello!", 6) # "      Hello!"
```

Fashion doesn't need any prior knowledge of the OpenFaas function, you can simply call it as if it were a local function!

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Installation](#installation)
- [Usage](#usage)
  - [Ordinary Usage](#ordinary-usage)
  - [Async](#async)
  - [Other OpenFaaS utilities](#other-openfaas-utilities)
  - [Advanced Usage](#advanced-usage)
- [Related Projects](#related-projects)
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
```
from fashion import left_pad
left_pad(input="Hello!", 6) # "      Hello!"
```

Alternately, you can use Fashion's `trigger` function directly, like so:

```
import Fashion
fashion.trigger("left_pad", value="Hello!", amount=6) "      Hello!"
```

### Async
Similarly, you can use OpenFaaS functions asyncronously.
`XXX TODO XXX`

### Other OpenFaaS utilities
`XXX TODO XXX`

### Advanced Usage
`XXX TODO XXX`

## Related Projects
 * [Zappa](https://github.com/Miserlou/Zappa) - Python's Serverless Framework for AWS Lambda

## License

(C) Rich Jones 2019, MIT License.