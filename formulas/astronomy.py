import math
from formulas import constant_values as c


def escape_velocity(M, r):
    return math.sqrt((2 * c.G * M) / r)


def orbital_velocity(M, r):
    return math.sqrt((c.G * M) / r)


def orbital_period(M, r):
    return 2 * math.pi * math.sqrt((r ** 3) / (c.G * M))


def gravitational_force(m1, m2, r):
    return (c.G * m1 * m2) / (r ** 2)


def surface_gravity(M, r):
    return (c.G * M) / (r ** 2)


def schwarzschild_radius(M):
    return (2 * c.G * M) / (c.C ** 2)


def light_travel_time(d):
    return d / c.C


def parallax_distance(p):
    return 1 / p


def luminosity(R, T):
    return 4 * math.pi * (R ** 2) * c.SIGMA * (T ** 4)


def flux(L, d):
    return L / (4 * math.pi * (d ** 2))


def distance_modulus(m, M):
    return 10 ** (((m - M) / 5) + 1)


def hubbles_law(H0, d):
    return H0 * d


def redshift_velocity(z):
    return z * c.C


def keplers_third_law(M, r):
    return 2 * math.pi * math.sqrt((r ** 3) / (c.G * M))


def wiens_law(T):
    return c.WIEN / T


def stefan_boltzmann(A, T):
    return c.SIGMA * A * (T ** 4)


def mass_energy(m):
    return m * (c.C ** 2)


def doppler_shift(delta_lambda, wavelength):
    return (delta_lambda / wavelength) * c.C


def roche_limit(R, M, m):
    return 2.44 * R * ((M / m) ** (1 / 3))


def hill_sphere(a, M, m):
    return a * ((M / (3 * m)) ** (1 / 3))


def rocket_equation(Ve, m0, mf):
    return Ve * math.log(m0 / mf)


def escape_energy(M, m, r):
    return (c.G * M * m) / r