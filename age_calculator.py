from datetime import datetime, date
from dateutil import relativedelta

def get_age(start_date: str, end_date: str):
    """Returns the age (start date to end date)
    in years, months, weeks, days, hours, minutes and seconds"""
    #print(start_date) > 2022-02-03
    start = datetime.strptime(start_date, "%Y-%m-%d")
    end = datetime.strptime(end_date, "%Y-%m-%d")
    if end < start:
        return False
    seconds = get_seconds(start, end)
    minutes = seconds / 60
    hours = seconds / 3600
    days = get_days(start, end)
    weeks = get_weeks(days)
    ymd = get_ymd(start, end)

    #print(f"Seconds: {seconds}\nMinutes: {minutes}\nHours: {hours}")
    #print(f"Days: {days}")
    #print(f"Weeks: {weeks[0]} and {weeks[1]} days")
    #print(f"Months: {ymd[1][0]}, Days: {ymd[1][1]}")
    #print(f"Years: {ymd[0][0]}, Months: {ymd[0][1]}, Days: {ymd[0][2]}")

    return [seconds, minutes, hours, days, weeks, ymd]


def get_seconds(start_date: datetime, end_date: datetime):
    """Returns the total seconds between two dates"""
    diff = (end_date - start_date)
    total = diff.total_seconds()
    return total

def get_days(start_date: datetime, end_date: datetime):
    """Returns the total days between two dates"""
    diff = (end_date - start_date)
    total = diff.days
    return total

def get_weeks(days: int):
    """Returns the total weeks and excess days between two dates"""
    rest = days % 7
    full_weeks = (days - rest) / 7
    return (full_weeks, rest)

def get_ymd(start_date: datetime, end_date: datetime):
    """Returns the total years/months/days, months/days between two dates"""
    delta = relativedelta.relativedelta(end_date, start_date)
    years = delta.years
    months = delta.months
    days = delta.days

    return [(years, months, days), (years * 12 + months, days)]