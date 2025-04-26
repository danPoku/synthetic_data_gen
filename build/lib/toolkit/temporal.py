<<<<<<< HEAD
def apply_temporal_factors(date):
    weekday = date.weekday()
    day_factor = 0.9 if weekday == 5 else 0.7 if weekday == 6 else 1.0

    if (date.month == 12 and date.day in [25, 26]) or (date.month == 1 and date.day == 1):
        day_factor *= 0.5

    return day_factor
=======
def temporal_factors(date):
    """
    Adjusting daily counts of cases based on weekdays, weekends, and public holidays.

    Args:
        date (datetime.date or datetime.datetime): The date for which the adjustment factor is calculated.

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
    if weekday == 5: # Saturday
        day_factor = 0.9
    elif weekday == 6: # Sunday
        day_factor = 0.7
    else:
        day_factor = 1.0

    # Reducing counts on major holidays by reducing day_factor
    if (
        (date.month == 1 and date.day == 1) # New Year
        or (date.month == 3 and date.day == 6) # Independence Day
        or (date.month == 5 and date.day == 1) # Labour Day
        or (date.month == 9 and date.day == 21) # Kwame Nkrumah Memorial Day
        or (date.month == 12 and date.day in [25, 26]) # Christmas and Boxing Days
    ):
        day_factor *= 0.5
        
    # Constitution Day - effective from 2019 and beyond
    if date.year >= 2019 and date.month == 1 and date.day == 7:
        day_factor *= 0.5
    
    # TODO: Implement logic for calculating Eid festivals, Good Friday, Easter Monday, and Farmers' Day
    
    return day_factor
>>>>>>> origin/copd-assumptions
