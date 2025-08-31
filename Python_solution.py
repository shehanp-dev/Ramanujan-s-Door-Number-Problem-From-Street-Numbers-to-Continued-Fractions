import math
from fractions import Fraction

def continued_fraction_terms(number: int, max_terms: int):
    """
    Compute the continued fraction expansion of sqrt(number) 
    up to max_terms terms.
    """
    root = math.sqrt(number)
    integer_part = int(root)
    fractional_part = root - integer_part
    terms = [integer_part]

    # Generate continued fraction terms
    for _ in range(2 * max_terms):
        if fractional_part == 0:
            break
        fractional_part = 1 / fractional_part
        integer_part = int(fractional_part)
        fractional_part -= integer_part
        terms.append(integer_part)

    return terms


def continued_fraction_to_fraction(terms: list) -> Fraction:
    """
    Convert a finite list of continued fraction terms into
    a Fraction object representing the convergent.
    """
    if len(terms) == 1:
        return Fraction(terms[0])
    return Fraction(terms[0] + 1 / continued_fraction_to_fraction(terms[1:]))


# Parameters
num_terms = 50
cf_terms = continued_fraction_terms(8, num_terms)

# Generate convergents and check which ones solve the house-number problem
for k in range(1, len(cf_terms) + 1):
    convergent = continued_fraction_to_fraction(cf_terms[:k])
    denominator, numerator = convergent.denominator, convergent.numerator  # q, p

    # Relation to house-number problem
    n_value = (numerator - 1) // 2
    x_value = denominator

    # Check the condition (only valid if n and x match the problem constraints)
    if (x_value + n_value) % 2 == 0:
        print(f"(x, n) = ({x_value}, {n_value})")
