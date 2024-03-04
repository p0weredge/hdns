from hdns import arecords, ipv4

zone_id = "XXXXXX"
auth_api_token = "XXXXX"

ip = ipv4.get_ipv4()
records = arecords.get_all(zone_id, auth_api_token)

different_ip_zone_ids = []

for record in records:
    if record["value"] != ip:
        record["value"] = ip
        different_ip_zone_ids.append(record)
if different_ip_zone_ids:
    insert_records = arecords.insert_records(auth_api_token, different_ip_zone_ids)
    print(insert_records)
else:
    print("No ip difference found!")
