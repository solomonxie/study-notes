# Convert Epoach Time

Epoch time to Normal date format
```py
import datetime
datetime.datetime.utcfromtimestamp(int(1571356800000)/1000).strftime('%Y-%m-%d')
```

Normal time to Epoch Time:
```py
def convert_date_to_timestamp(date_str):
    """
    Trans date value to utc timestamp.
    """
    utc_dt = datetime.strptime(date_str, '%Y-%m-%d')
    utc_timestamp = calendar.timegm(utc_dt.timetuple())

    # Need to align with Micro-services in the unit of: milliseconds
    return utc_timestamp * 1000
```
