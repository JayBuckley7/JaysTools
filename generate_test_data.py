import argparse
import json
import random
import datetime
import urllib.request

FIRST_NAMES = [
    "Adeline", "John", "Michael", "Sarah", "Jessica", "David", "Emily",
    "Daniel", "Laura", "Robert", "Olivia", "James"
]

LAST_NAMES = [
    "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis",
    "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas"
]

STREET_NAMES = [
    "Oak", "Maple", "Pine", "Cedar", "Elm", "Washington",
    "Lake", "Hill", "View", "High", "Park", "River"
]

CITIES = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix",
    "Philadelphia", "San Antonio", "San Diego", "Dallas", "San Jose"
]

STATES = [
    "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA",
    "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
    "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
    "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
    "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"
]

def random_name():
    first = random.choice(FIRST_NAMES)
    last = random.choice(LAST_NAMES)
    suffix = random.choice(["", " Jr.", " Sr.", " II", " III", " IV"])
    return f"{first} {last}{suffix}".strip()

def random_address():
    number = random.randint(100, 9999)
    street = random.choice(STREET_NAMES)
    suffix = random.choice(["St", "Ave", "Blvd", "Rd", "Ln", "Dr"])
    return f"{number} {street} {suffix}"

def random_city():
    return random.choice(CITIES)

def random_state():
    return random.choice(STATES)

def random_zip():
    return "{:05d}".format(random.randint(0, 99999))

def random_dob(start_year=1940, end_year=2002):
    start = datetime.date(start_year, 1, 1)
    end = datetime.date(end_year, 12, 31)
    days_between = (end - start).days
    random_days = random.randrange(days_between)
    dob = start + datetime.timedelta(days=random_days)
    return dob.strftime("%m-%d-%Y")

def random_phone():
    return "".join(str(random.randint(0, 9)) for _ in range(10))

def random_ssn():
    parts = (
        random.randint(100, 899),
        random.randint(10, 99),
        random.randint(1000, 9999)
    )
    return f"{parts[0]:03d}-{parts[1]:02d}-{parts[2]:04d}"

def random_ccn():
    digits = [random.randint(0, 9) for _ in range(15)]
    # Luhn checksum for the last digit
    def luhn_checksum(nums):
        total = 0
        reverse = nums[::-1]
        for i, n in enumerate(reverse):
            if i % 2 == 0:
                n *= 2
                if n > 9:
                    n -= 9
            total += n
        return (10 - (total % 10)) % 10
    checksum = luhn_checksum(digits)
    digits.append(checksum)
    # group digits as xxxx xxxx xxxx xxxx
    ccn_str = "".join(str(d) for d in digits)
    return " ".join([ccn_str[i:i+4] for i in range(0, 16, 4)])

def random_exp(months=60):
    today = datetime.date.today()
    future = today + datetime.timedelta(days=30 * random.randint(1, months))
    return future.strftime("%m/%y")

def random_cvv():
    return "{:03d}".format(random.randint(0, 999))

def random_data():
    fname = random_name()
    data = {
        "fname": fname,
        "address": random_address(),
        "city": random_city(),
        "state": random_state(),
        "zip": random_zip(),
        "dob": random_dob(),
        "phone": random_phone(),
        "ssn": random_ssn(),
        "mmn": random.choice(LAST_NAMES),
        "cname": fname,
        "ccn": random_ccn(),
        "exp": random_exp(),
        "cvv": random_cvv(),
        "amex_cid": ""
    }
    return data

def post_data(url, payload):
    data_bytes = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data_bytes, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req) as response:
        return response.read()

def main():
    parser = argparse.ArgumentParser(description="Generate test data and POST to a URL")
    parser.add_argument("url", help="Destination URL")
    parser.add_argument("--count", type=int, default=1, help="Number of records to send")
    args = parser.parse_args()
    for _ in range(args.count):
        payload = random_data()
        print("Sending:", json.dumps(payload))
        try:
            resp = post_data(args.url, payload)
            print("Response:", resp)
        except Exception as e:
            print("Error posting data:", e)

if __name__ == "__main__":
    main()
