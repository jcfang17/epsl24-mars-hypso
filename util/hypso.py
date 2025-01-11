import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sklearn.metrics import r2_score


def get_hypso_vector(dem_array):
    """
    Calculate hypsometry vector for a DEM array

    Parameters:
        dem_array: numpy array
            Input DEM array. Can be 2D or flattened 1D

    Returns:
        numpy array of length 101 representing normalized elevation values
    """

    # Calculate percentiles from 0 to 100
    percentiles = np.linspace(0, 100, 101)
    elevation_values = np.percentile(dem_array, percentiles)

    # Normalize elevation values
    min_elev = np.min(elevation_values)
    max_elev = np.max(elevation_values)
    normalized_elevations = (elevation_values - min_elev) / (max_elev - min_elev)

    # Flip array to match MATLAB output
    hypso_vector = np.flip(normalized_elevations)

    return hypso_vector

def plot_hypso_vector(hypso_vector):
    x = np.linspace(0, 1, 101)
    plt.plot(x, hypso_vector)
    
    plt.xlabel('Normalized Area')
    plt.ylabel('Normalized Elevation')
    plt.title('Hypsometry Curve')

    plt.show()


def get_hypso_attributes_from_vector(fx, poly_order=9):
    """
    Calculate hypsometric attributes from a hypsometry vector using polynomial fitting

    Parameters:
        fx: hypsometry vector
        poly_order: int (default=9)
            Order of polynomial to fit

    Returns:
        dict containing the metrics:
            - INT: Integral
            - SK: Skewness
            - KUR: Kurtosis
            - DSK: Derivative Skewness
            - DKUR: Derivative Kurtosis
            - R2: R-squared value of polynomial fit
    """
    # Create x values
    x = np.linspace(0, 1, 101)

    # Fit polynomial
    coeffs = np.polyfit(x, fx, poly_order)

    # Calculate R² using the polynomial fit
    fx_fitted = np.polyval(coeffs, x)
    R2 = r2_score(fx, fx_fitted)

    # Convert to symbolic expression for integration
    r = sp.Symbol('r')
    f_poly = 0
    for i, coeff in enumerate(reversed(coeffs)):
        f_poly += coeff * r**i

    # Calculate integral
    INT = float(sp.integrate(f_poly, (r, 0, 1)))

    # Calculate first moment (mean)
    mu1 = float(sp.integrate(f_poly * r, (r, 0, 1))) / INT

    # Calculate central moments for skewness and kurtosis
    second_moment = float(sp.integrate(f_poly * (r - mu1)**2, (r, 0, 1))) / INT
    third_moment = float(sp.integrate(f_poly * (r - mu1)**3, (r, 0, 1))) / INT
    fourth_moment = float(sp.integrate(f_poly * (r - mu1)**4, (r, 0, 1))) / INT

    # Calculate skewness and kurtosis
    SK = third_moment / (second_moment**1.5)
    KUR = fourth_moment / (second_moment**2)

    # Calculate derivative metrics
    g_poly = sp.diff(f_poly, r)
    int_g = float(sp.integrate(g_poly, (r, 0, 1)))

    # Calculate mean of derivative
    mu1_g = float(sp.integrate(g_poly * r, (r, 0, 1))) / int_g

    # Calculate moments for derivative
    second_moment_g = float(sp.integrate(g_poly * (r - mu1_g)**2, (r, 0, 1))) / int_g
    third_moment_g = float(sp.integrate(g_poly * (r - mu1_g)**3, (r, 0, 1))) / int_g
    fourth_moment_g = float(sp.integrate(g_poly * (r - mu1_g)**4, (r, 0, 1))) / int_g

    # Calculate derivative skewness and kurtosis
    DSK = third_moment_g / (second_moment_g**1.5)
    DKUR = fourth_moment_g / (second_moment_g**2)

    return {
        'HI': INT,
        'SK': SK,
        'KUR': KUR,
        'DSK': DSK,
        'DKUR': DKUR,
        'R2': R2
    }
