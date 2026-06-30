import math

def mean(values):
    return sum(values) / len(values)

def range_value(values):
    return max(values) - min(values)

def simple_interest(p, r, t):
    return p * r * t

def compound_interest(p, r, n, t):
    return p * (1 + r / n) ** (n * t)