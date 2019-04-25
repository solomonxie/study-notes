# Python Datetime [DRAFT]

## Understand Date & Time in general
.........

## Understand Datetime in Python
.........

## How to check the type of a datetime object

Types of a datetime object:
- `Naive`: simple like `2018-01-01` without any locale or more infomation
- `Aware`: explicit date time like `2018-01-25T11:36:55.000+10`

How to check if a given string is a `naive` or `aware`?

[Refer to Stackoverflow: How to check if a datetime object is localized with pytz?](https://stackoverflow.com/a/27596917/9172013)

- A datetime object `dt` is **aware** iff:
```py
d.tzinfo is not None and d.tzinfo.utcoffset(d) is not None
```
- A datetime object `dt` is **naive** iff:
```py
d.tzinfo is None or d.tzinfo.utcoffset(d) is None
```
