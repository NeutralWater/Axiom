import math

def discriminant(a, b, c):
    return b ** 2 - 4 * a * c

    
def quadratic (a, b, c):
    if a == 0:
        return None
    
    d = discriminant(a, b, c)
    denominator = 2 * a
    if d < 0:
        return ()
    
    if d == 0:
        return (-b / denominator,)
    
    x1 = (-b + math.sqrt(d)) / denominator
    x2 = (-b - math.sqrt(d)) / denominator
    
    return (x1, x2)

def slope(x1, y1, x2, y2):
    if x1 == x2:
        return None
    return (y2 - y1) / (x2 - x1)

def midpoint (x1, y1, x2, y2):
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def distance (x1, y1, x2, y2):
    return math.hypot(x2 - x1,y2 - y1)

def point_slope(x1, y1, m): 
    return f"y= {y1} = {m}(x - {x1})"

def slope_intercept(m, x1, y1):
    b = y1 - m * x1
    return f"y= {m}x + {b}"