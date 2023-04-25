"""Example function for unit tests!"""

def sum(xs: list[float]) -> float:
    """returns sum of all elements in list"""
    total: float = 0.0

    for index in xs:
        total += index
    
    return total