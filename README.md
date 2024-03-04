# hdns

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![PyPI version](https://badge.fury.io/py/your-package-name.svg)](https://badge.fury.io/py/your-package-name)

## Overview

This library is intended for users who don't have a static IP from their ISP but want to keep their A records updated on the Hetzner DNS service.

## Installation

```bash
pip install hdns requests 
```

### Dependencies

- [requests](https://pypi.org/project/requests/) - Requests is a simple, yet elegant, HTTP library.


Example Usage
```python
from hdns import arecords, ipv4

# Provide your Hetzner zone ID and authentication token
zone_id = "XXXXXXX"
auth_api_token = "XXXXXX"

# Get the current IPv4 address
ip = ipv4.get_ipv4()

# Retrieve all A records for the specified zone
records = arecords.get_all(zone_id, auth_api_token)

# Initialize a list to store records with different IP addresses
different_ip_zone_ids = []

# Check if any records have a different IP address than the current one
for record in records:
    if record["value"] != ip:
        record["value"] = ip
        different_ip_zone_ids.append(record)

# Update the A records if there are differences
if different_ip_zone_ids:
    insert_records = arecords.insert_records(auth_api_token, different_ip_zone_ids)
    print(insert_records)
else:
    print("No need for update, IPv4 is still the same!")
```

> ℹ️ **Info:** Feel free to replace the placeholder values with your actual zone ID and authentication token.

Components
- ipv4: Uses the https://api.ipify.org API to retrieve your IPv4 public IP address.
- arecords.get_all(): Retrieves all A records for a specified zone using the provided zone ID and authentication token.
- ipv4.get_ipv4(): Returns your public IPv4 address.
- arecords.insert_records(): Updates A records with new IP addresses using the provided authentication token and a JSON array object containing the records to be modified.

