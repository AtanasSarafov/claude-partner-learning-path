def greeting():
    print("Hello, World!")


def calculate_pi():
    """
    Calculate pi to 10 decimal places using the Machin formula.
    Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    
    Returns:
        float: Pi calculated to 10 decimal places
    """
    from decimal import Decimal, getcontext
    
    # Set precision high enough to ensure 10 decimal places accuracy
    getcontext().prec = 50
    
    def arctan(x, num_terms=100):
        """Calculate arctan using Taylor series expansion."""
        x = Decimal(x)
        power = x
        result = power
        for n in range(1, num_terms):
            power *= -x * x
            result += power / (2 * n + 1)
        return result
    
    # Machin's formula: pi/4 = 4*arctan(1/5) - arctan(1/239)
    pi = 4 * (4 * arctan(Decimal(1) / Decimal(5)) - arctan(Decimal(1) / Decimal(239)))
    
    # Round to 10 decimal places
    return round(float(pi), 10)