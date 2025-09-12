import numpy as np
from typing import Sequence
import matplotlib.pyplot as plt

def calculate_mean(data: Sequence[int | float]) -> float:
    """Return mean of list of data

    Args:
        data (Sequence[int  |  float]): List of numbers (int or float)

    Returns:
        float: mean of the data
    """    
    return sum(data) / len(data)

def calculate_median(data: Sequence[int | float]) -> float:
    """Return median of list of data (does not need to be sorted)

    Args:
        data (Sequence[int  |  float]): List of numbers (int or float)

    Returns:
        float: median of the data
    """    
    n = len(data)
    sorted_data = sorted(data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]

def calculate_mode(data: Sequence[int | float]) -> Sequence[int | float]:
    """Return mode(s) of list of data

    Args:
        data (Sequence[int  |  float]): List of numbers (int or float)

    Returns:
        Sequence[int  |  float]: mode(s) of the data
    """    
    frequency: dict[int | float, int] = {}
    for value in data:
        if value in frequency:
            frequency[value] += 1
        else:
            frequency[value] = 1
    max_freq: int = max(frequency.values())
    modes: Sequence[int | float] = [key for key, freq in frequency.items() if freq == max_freq]
    return modes

def calculate_min(data: Sequence[int | float]) -> int | float:
    """Return minimum value of list of data

    Args:
        data (Sequence[int  |  float]): List of numbers (int or float)

    Returns:
        int  |  float: minimum value of the data
    """    
    return min(data)

def calculate_max(data: Sequence[int | float]) -> int | float:
    """Return maximum value of list of data

    Args:
        data (Sequence[int  |  float]): List of numbers (int or float)

    Returns:
        int  |  float: maximum value of the data
    """    
    return max(data)

def calculate_range(data: Sequence[int | float]) -> int | float:
    """Return range of list of data

    Args:
        data (Sequence[int  |  float]): List of numbers (int or float)

    Returns:
        int  |  float: range of the data
    """    
    range: int | float = calculate_max(data) - calculate_min(data)
    return range

def calculate_variance(data: Sequence[int | float]) -> float:
    """Return variance of list of data

    Args:
        data (Sequence[int  |  float]): List of numbers (int or float)

    Returns:
        float: variance of the data
    """    
    mean: float = calculate_mean(data)
    variance: float = sum(np.square(x - mean) for x in data) / (len(data) - 1)
    return variance

def calculate_standard_deviation(data: Sequence[int | float]) -> float:
    """Return standard deviation of list of data

    Args:
        data (Sequence[int  |  float]): List of numbers (int or float)

    Returns:
        float: standard deviation of the data
    """    
    variance: float = calculate_variance(data)
    standard_deviation: float = np.sqrt(variance)
    return standard_deviation

def calculate_quartiles(data: Sequence[int | float]) -> tuple[float, float, float]:
    """Return first, second (median), and third quartiles of list of data

    Args:
        data (Sequence[int  |  float]): List of numbers (int or float)

    Returns:
        tuple[float, float, float]: first, second (median), and third quartiles of the data
    """    
    sorted_data: Sequence[int | float] = sorted(data)
    n: int = len(sorted_data)
    mid: int = n // 2

    if n % 2 == 0:
        lower_half: Sequence[int | float] = sorted_data[:mid]
        upper_half: Sequence[int | float] = sorted_data[mid:]
    else:
        lower_half: Sequence[int | float] = sorted_data[:mid]
        upper_half: Sequence[int | float] = sorted_data[mid + 1:]

    Q1: float = calculate_median(lower_half)
    Q2: float = calculate_median(sorted_data)
    Q3: float = calculate_median(upper_half)

    return (Q1, Q2, Q3)

def calculate_iqr(data: Sequence[int | float]) -> float:
    """Return interquartile range (IQR), also known as the fourth spread, of list of data

    Args:
        data (Sequence[int  |  float]): List of numbers (int or float)

    Returns:
        float: interquartile range (IQR) of the data
    """    
    Q1, _, Q3 = calculate_quartiles(data)
    IQR: float = Q3 - Q1
    return IQR

def print_statistical_values(data: Sequence[int | float]) -> None:
    """Prints various statistical values of the given data.

    Args:
        data (Sequence[int  |  float]): List of numbers (int or float)
    """    
    print(f"Data: {data}")
    print(f"Mean: {calculate_mean(data)}")
    print(f"Median: {calculate_median(data)}")
    print(f"Mode: {calculate_mode(data)}")
    print(f"Min: {calculate_min(data)}")
    print(f"Max: {calculate_max(data)}")
    print(f"Range: {calculate_range(data)}")
    print(f"Variance: {calculate_variance(data)}")
    print(f"Standard Deviation: {calculate_standard_deviation(data)}")
    Q1, Q2, Q3 = calculate_quartiles(data)
    print(f"Q1: {Q1}, Q2 (Median): {Q2}, Q3: {Q3}")
    print(f"IQR: {calculate_iqr(data)}")

def construct_boxplot(data: Sequence[int | float]) -> None:
    """Constructs a boxplot for the given data using matplotlib.

    Args:
        data (Sequence[int  |  float]): List of numbers (int or float)
    """    

    plt.boxplot(data, vert=True, patch_artist=True)
    plt.title("Boxplot")
    plt.ylabel("Values")
    plt.grid(True)
    plt.show()