# Get Date For Ranges

```py
def get_dates_from_range(granularity, start_date, end_date):
    """
        print(get_dates_from_range('monthly', '2019-01-01', '2019-10-20'), '\n\n')
        print(get_dates_from_range('weekly', '2019-01-01', '2019-10-20'), '\n\n')
        print(get_dates_from_range('daily', '2019-01-01', '2019-01-20'), '\n\n')
        [('2018-12-30', 'weekly'), ('2019-01-06', 'weekly'), ('2019-01-01', 'daily')....]
    """
    start, end = datetime.strptime(start_date, '%Y-%m-%d'), datetime.strptime(end_date, '%Y-%m-%d')
    daily_dates = [start + timedelta(days=i) for i in range((end - start).days + 1)]

    target_dates = []
    if granularity == 'daily':
        target_dates = daily_dates
    elif granularity == 'weekly':
        # Start from Monday: weeday_index = day.weekday()
        # Start from Sunday: weeday_index = (day.weekday() + 1) % 7
        target_dates = sorted(set([day - timedelta(days=(day.weekday() + 1) % 7) for day in daily_dates]))  # Sundays
    elif granularity == 'monthly':
        target_dates = sorted(set([day.replace(day=1) for day in daily_dates]))

    combos = [(day.strftime('%Y-%m-%d'), granularity) for day in target_dates]
    return combos
```

## Get Start & End date

```py
def get_start_end_date(target_date, granularity):
    target = datetime.strptime(target_date, '%Y-%m-%d') if isinstance(target_date, str) else target_date
    if granularity == 'daily':
        start = end = target
    elif granularity == 'weekly':
        start = target - timedelta(days=target.weekday() + 1)
        end = target + timedelta(days=6)
    elif granularity == 'monthly':
        start = target.replace(day=1)
        any_day_in_next_month = target.replace(day=28) + timedelta(days=4)
        end = any_day_in_next_month - timedelta(days=any_day_in_next_month.day)
    return start.strftime('%Y-%m-%d'), end.strftime('%Y-%m-%d')
```
