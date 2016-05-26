def to_float(x):
    """
    attempts to convert x to a floating point value,
    first removing some common punctuation. returns
    None if conversion failed.
    """

    if x is None:
        return None
    # normalize punctuation
    x = x.replace(';', '.').replace(',', '.')
    try:
        return float(x)
    except ValueError:
        return None
