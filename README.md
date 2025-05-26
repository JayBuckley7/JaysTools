# JaysTools Test Data Generator

This repository contains a simple Python script for generating synthetic test data and sending it to a URL via HTTP POST.

## Usage

Run the script with Python and specify a destination URL. Optionally, use `--count` to send multiple payloads.

```bash
python generate_test_data.py http://example.com/api --count 5
```

Each payload includes random fields like name, address, phone number, credit card number, etc., formatted as JSON. If the POST request fails, the script prints the error to the console.
