def apply_temporal_factors(date):
    weekday = date.weekday()
    day_factor = 0.9 if weekday == 5 else 0.7 if weekday == 6 else 1.0

    if (date.month == 12 and date.day in [25, 26]) or (date.month == 1 and date.day == 1):
        day_factor *= 0.5

    return day_factor