# Python 计算两个日期之间的所有日子

Refer to: https://kite.com/python/examples/4656/datetime-get-all-dates-between-two-dates

```py
def parse_date_filter_to_days(date_filter):
    date = date_filter['date']
    fmt = '%Y-%m-%d'
    start = datetime.strptime(date['between'][0], fmt)
    end = datetime.strptime(date['between'][1], fmt)
    datetimes = [start + timedelta(d) for d in range((end - start).days + 1)]
    days = [d.strftime('%Y%m%d') for d in datetimes]
    return days


date_filter = {'date': {'between': ['2019-04-25', '2019-05-2']}}
result = parse_date_filter_to_days(date_filter)
self.assertListEqual(
    result,
    ['20190425', '20190426', '20190427', '20190428', '20190429', '20190430', '20190501', '20190502'])
```
