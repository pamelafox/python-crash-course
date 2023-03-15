def calculate_whininess(temperature, windspeed, incline):
    """
    Calculates how whiny I'll be if we go on a hike in
    the given conditions.
    >>> calculate_whininess(67, 3, 0)
    0
    >>> calculate_whininess(67, 6, 0)
    10
    >>> calculate_whininess(67, 6, 10)
    5
    >>> calculate_whininess(50, 0, 0)
    15
    """
    whininess = 0
    if windspeed > 5:
        whininess += 10
    elif incline > 0:
        whininess = incline / 2
    elif temperature < 65:
        whininess += 65 + temperature
    return round(whininess)

calculate_whininess(67, 6, 10)