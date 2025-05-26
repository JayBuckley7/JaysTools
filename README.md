# JaysTools Test Data Generator

Phishing is dumnb.

I got a phising link pretending to be amazon trying to steal account details by posting a payloud up to https://prime.activation.billing.jto.gim.mybluehost.me/auth/card

so here's a generator to fill that database with froggy data


## Usage

Run the script with Python and specify a destination URL. Optionally, use `--count` to send multiple payloads.

```bash
python generate_test_data.py http://example.com/api --count 5
```

Each payload includes random fields like name, address, phone number, credit card number, etc., formatted as JSON. If the POST request fails, the script prints the error to the console.
