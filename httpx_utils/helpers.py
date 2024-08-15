# Utility functions

def encode_params(params):
    return "&".join(f"{k}={v}" for k, v in params.items())

def parse_headers(raw):
    headers = {}
    for line in raw.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            headers[k.strip()] = v.strip()
    return headers