import numpy as np
import sympy as sy
import math
import typing


def Gamma_function(z: float) -> float:
    '''
    Compute the Gamma function for a positive number z.
    
    Parameters:
    z (float): A positive number.
    
    Returns:
    float: The value of the Gamma function at z.
    '''
    if z <= 0:
        raise ValueError("Input must be a positive number.")
    return math.gamma(z)

class Beta_Distribution:
    def __init__(self, a: float, b: float, A: float, B: float):
        if a <= 0 or b <= 0:
            raise ValueError("Parameters 'a' and 'b' must be positive.")
        self.a = a
        self.b = b
        self.A = A
        self.B = B

    def pdf(self, x: float) -> float:
        '''
        Compute the probability density function (PDF) of the Beta distribution for x between A and B.
        
        Parameters:
        x (float): The point at which to evaluate the PDF.
        
        Returns:
        float: The value of the PDF at x.
        '''
        if x < 0 or x > 1:
            return 0

        P1 = 1/(self.B-self.A)
        P2 = Gamma_function(self.a + self.b) / ((Gamma_function(self.a) * Gamma_function(self.b)))
        P3 = ((x - self.A) / (self.B - self.A)) ** (self.a - 1)
        P4 = ((self.B - x) / (self.B - self.A)) ** (self.b - 1)
        value = P1 * P2 * P3 * P4
        return value

    def cdf(self, x: float) -> float:
        '''
        (TODO: Not implemented)
        Compute the cumulative distribution function (CDF) of the Beta distribution at x between A and B.
        
        Parameters:
        x (float): The point at which to evaluate the CDF.
        
        Returns:
        float: The value of the CDF at x.
        '''
        return 0.0
    
    def Expected_Value(self) -> float:
        '''
        Compute the expected value of the Beta distribution between A and B.
        
        Returns:
        float: The expected value of the distribution.
        '''
        return self.A + (self.a / (self.a + self.b)) * (self.B - self.A)
    
    def Variance(self) -> float:
        '''
        Compute the variance of the Beta distribution between A and B.
        
        Returns:
        float: The variance of the distribution.
        '''
        numerator = self.a * self.b * (self.B - self.A) ** 2
        denominator = ((self.a + self.b) ** 2) * (self.a + self.b + 1)
        value = numerator / denominator
        return value
    

class Standard_Beta_Distribution(Beta_Distribution):
    def __init__(self, a: float, b: float):
        super().__init__(a, b, A = 0, B = 1)

    def pdf(self, x: float) -> float:
        '''
        Compute the probability density function (PDF) of the standard Beta distribution for x in [0, 1].
        
        Parameters:
        x (float): The point at which to evaluate the PDF.
        
        Returns:
        float: The value of the PDF at x.
        '''
        return super().pdf(x, 0, 1)

    def cdf(self, x: float) -> float:
        '''
        Compute the cumulative distribution function (CDF) of the standard Beta distribution for x in range [0, 1].
        
        Parameters:
        x (float): The point at which to evaluate the CDF.

        Returns:
        float: The value of the CDF at x.
        '''
        
        coefficient = Gamma_function(self.a + self.b) / (Gamma_function(self.a) * Gamma_function(self.b))
        integrand = lambda t: (t ** (self.a - 1)) * (1 - t) ** (self.b - 1)
        
        t = sy.Symbol('t')
        integral = sy.integrate(integrand(t), (t, 0, x)).evalf()
        value = coefficient * integral
        return value
    
    def Expected_Value(self) -> float:
        '''
        Compute the expected value of the standard Beta distribution.
        
        Returns:
        float: The expected value of the distribution.
        '''
        return super().Expected_Value()
    
    def Variance(self) -> float:
        '''
        Compute the variance of the standard Beta distribution.

        Returns:
        float: The variance of the distribution.
        '''
        return super().Variance()


class Lognormal_Distribution():
    def __init__(self, mu: float, sigma: float) -> None:
        if sigma <= 0:
            raise ValueError("Parameter 'sigma' must be positive.")
        self.mu = mu
        self.sigma = sigma
        
    def pdf(self, x: float) -> float:
        '''
        Compute the probability density function (PDF) of the Lognormal distribution for x > 0.
        
        Parameters:
        x (float): The point at which to evaluate the PDF.
        
        Returns:
        float: The value of the PDF at x.
        '''
        if x <= 0:
            return 0

        denominator = (x * self.sigma * np.sqrt(2 * np.pi))
        exponent = -((np.log(x) - self.mu) ** 2) / (2 * self.sigma ** 2)
        value = np.exp(exponent) / denominator
        return value
    
    def cdf(self, x: float) -> float:
        '''
        Compute the cumulative distribution function (CDF) of the Lognormal distribution for x > 0.
        
        Parameters:
        x (float): The point at which to evaluate the CDF.
        
        Returns:
        float: The value of the CDF at x.
        '''
        if x <= 0:
            return 0

        z = (np.log(x) - self.mu) / self.sigma
        value = 0.5 * (1 + math.erf(z / np.sqrt(2)))
        return value
    
    def Expected_Value(self) -> float:
        '''
        Compute the expected value of the Lognormal distribution.
        
        Returns:
        float: The expected value of the distribution.
        '''
        value = np.exp(self.mu + (self.sigma ** 2) / 2)
        return value
    
    def Variance(self) -> float:
        '''
        Compute the variance of the Lognormal distribution.
        
        Returns:
        float: The variance of the distribution.
        '''
        value = (np.exp(self.sigma ** 2) - 1) * np.exp(2 * self.mu + self.sigma ** 2)
        return value


class Weibull_Distribution():
    def __init__(self, a: float, b: float) -> None:
        if a <= 0 or b <= 0:
            raise ValueError("Parameters 'a' and 'b' must be positive.")
        self.a = a
        self.b = b
        
    def pdf(self, x: float) -> float:
        '''
        Compute the probability density function (PDF) of the Weibull distribution for x >= 0.

        Parameters:
        x (float): The point at which to evaluate the PDF.

        Returns:
        float: The value of the PDF at x.
        '''
        if x < 0:
            return 0
        
        p1 = self.a * (x ** (self.a - 1))
        p2 = np.exp(-(x / self.b) ** self.a)
        value = (p1 / (self.b ** self.a)) * p2
        return value
    
    
    def cdf(self, x: float) -> float:
        '''
        Compute the cumulative distribution function (CDF) of the Weibull distribution for x >= 0.

        Parameters:
        x (float): The point at which to evaluate the CDF.

        Returns:
        float: The value of the CDF at x.
        '''
        if x < 0:
            return 0
        
        value = 1 - np.exp(-(x / self.b) ** self.a)
        return value
    
    def Expected_Value(self) -> float:
        '''
        Compute the expected value of the Weibull distribution.

        Returns:
        float: The expected value of the distribution.
        '''
        value = self.b * Gamma_function(1 + 1 / self.a)
        return value
    
    def Variance(self) -> float:
        '''
        Compute the variance of the Weibull distribution.

        Returns:
        float: The variance of the distribution.
        '''
        p1 = Gamma_function( 1 + 2 / self.a)
        p2 = (Gamma_function(1 + 1 / self.a)) ** 2
        value = (p1 - p2) * (self.b ** 2)
        return value
    
    
class Gamma_Distribution():
    def __init__(self, a: float, b: float) -> None:
        if a <= 0 or b <= 0:
            raise ValueError("Parameters 'a' and 'b' must be positive.")
        self.a = a
        self.b = b
        
    def pdf(self, x: float) -> float:
        '''
        Compute the probability density function (PDF) of the Gamma distribution for x >= 0.

        Parameters:
        x (float): The point at which to evaluate the PDF.

        Returns:
        float: The value of the PDF at x.
        '''
        if x < 0:
            return 0

        p1 = (x ** (self.a - 1)) * np.exp(-x / self.b)
        p2 = (self.b ** self.a) * Gamma_function(self.a)
        value = p1 / p2
        return value
    
    def cdf(self, x: float) -> float:
        '''
        Compute the cumulative distribution function (CDF) of the Gamma distribution for x >= 0.

        Parameters:
        x (float): The point at which to evaluate the CDF.

        Returns:
        float: The value of the CDF at x.
        '''
        if x < 0:
            return 0
        
        coefficient = 1 / (self.b ** self.a * Gamma_function(self.a))
        integrand = lambda t: (t ** (self.a - 1)) * (np.e ** (-t / self.b))
        
        t = sy.Symbol('t')
        integral = sy.integrate(integrand(t), (t, 0, x)).evalf()
        value = coefficient * integral
        return value
    
    def Expected_Value(self) -> float:
        '''
        Compute the expected value of the Gamma distribution.

        Returns:
        float: The expected value of the distribution.
        '''
        value = self.a * self.b
        return value
    
    def Variance(self) -> float:
        '''
        Compute the variance of the Gamma distribution.

        Returns:
        float: The variance of the distribution.
        '''
        value = self.a * (self.b ** 2)
        return value
    
