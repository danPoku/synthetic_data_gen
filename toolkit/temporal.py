from datetime import datetime, timedelta


def temporal_factors(date):
    """
    Adjusting daily counts of cases based on weekdays, weekends, and public holidays.

    Args:
        date (datetime.date or datetime.datetime): The date for which 
        the adjustment factor is calculated.

    Returns:
        float: Adjustment factor to scale daily expected disease counts.

    Adjustment Rules:
        - Weekdays (Monday-Friday): no adjustment (factor = 1.0)
        - Saturday: reduced by 10% (factor = 0.9)
        - Sunday: reduced by 30% (factor = 0.7)
        - Major holidays: reduced by 50% (factor = 0.5)

    Major Holidays:
        - New Year's Day (January 1)
        - Constitution Day (January 7, since 2019)
        - Independence Day (March 6)
        - Labour Day (May 1)
        - Kwame Nkrumah Memorial Day (September 21)
        - Christmas Day and Boxing Day (December 25, 26)
    """

    # Counts adjusted based on day of the week
    weekday = date.weekday()  # Monday = 0, Sunday = 6
    if weekday == 5:  # Saturday
        day_factor = 0.9
    elif weekday == 6:  # Sunday
        day_factor = 0.7
    else:
        day_factor = 1.0

    # Reducing counts on major holidays by reducing day_factor
    if (
        (date.month == 1 and date.day == 1)  # New Year
        or (date.month == 3 and date.day == 6)  # Independence Day
        or (date.month == 5 and date.day == 1)  # Labour Day
        or (date.month == 9 and date.day == 21)  # Kwame Nkrumah Memorial Day
        or (date.month == 12 and date.day in [25, 26])  # Christmas and Boxing Days
    ):
        day_factor *= 0.5

    # Constitution Day - effective from 2019 and beyond
    if date.year >= 2019 and date.month == 1 and date.day == 7:
        day_factor *= 0.5

    # Good Friday and Easter Monday
    easter = calculate_easter(date.year)
    good_friday = easter - timedelta(days=2)
    easter_monday = easter + timedelta(days=1)
    if date == good_friday or date == easter_monday:
        day_factor *= 0.5

    # Farmers' Day (First Friday of December)
    if date.month == 12 and date.weekday() == 4:  # Friday
        first_friday = (7 - datetime(date.year, 12, 1).weekday()) % 7 + 1
        if date.day == first_friday:
            day_factor *= 0.5

    # Eid festivals (Eid al-Fitr and Eid al-Adha)
    eid_dates = get_eid_dates(date.year)
    if date in eid_dates:
        day_factor *= 0.5

def calculate_easter(year):
    """Calculate the date of Easter Sunday for a given year."""
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = ((h + l - 7 * m + 114) % 31) + 1
    return datetime(year, month, day)

def get_eid_dates(year):
    """Placeholder function to return Eid dates for a given year."""
    return []
