# ❖ Python: Everything About Date & Time [DRAFT]

Unlike directly manipulate a string `2019-06-01`, there're so many more things you should consider about on the date in a program, like the Timezone, and how to count days in different months, years.


## Time Delta (+-)
> `Time Delta` enables to do "onwards/backwards" on dates, just like what we usually do: 10 days later, 2 months ago.


> Timedelta doesn't support "yearly delta".



## Change year

```py
>>> target_date = datetime(2019,1,1)
>>> target_date.replace(year=2000)
datetime.datetime(2000, 1, 1, 0, 0)
```


## Last Day of The Month

```py
import calendar

>>> calendar.monthrange(2019, 2)[1]
28
>>> calendar.monthrange(2019, 4)[1]
30
>>> calendar.monthrange(2019, 5)[1]
31
```
