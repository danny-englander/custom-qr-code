## Custom QR code generator

This is loosely based on https://github.com/lincolnloop/python-qrcode.

## Getting started

`cd` into the root of the project directory and run:

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
```

That will create a virtual environment and install the dependencies. Then run `source .venv/bin/activate` to set up the virtual environment so that you can simply use `python3` to run the script.

## Usage

basic QR code generation:

```bash
python3 main.py "https://example.com"
```

This will generate a QR code and save it to the `codes` directory.

## Options


This will show you the available options.
