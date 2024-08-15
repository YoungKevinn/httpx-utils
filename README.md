# httpx-utils

Lightweight utility helpers for HTTP operations in Python.

## Installation

```bash
pip install httpx-utils
```

Or install directly from source:

```bash
pip install git+https://github.com/YoungKevinn/httpx-utils.git
```

## Features

- Header parsing and normalization
- URL parameter encoding
- Response validation helpers
- Retry logic utilities

## Quick Start

```python
from httpx_utils import helpers

# Parse raw headers
headers = helpers.parse_headers("Content-Type: application/json\nAuthorization: Bearer token123")
print(headers)
# {'Content-Type': 'application/json', 'Authorization': 'Bearer token123'}

# Encode URL parameters
params = helpers.encode_params({"key": "value", "page": "1"})
print(params)
# key=value&page=1
```

## Requirements

- Python >= 3.6

## License

MIT
