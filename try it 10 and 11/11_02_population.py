import pytest
from city_functions import city_country  # Import the function to test

def test_city_country():
    # Test cases to verify the city_country function without population
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile', f"Expected 'Santiago, Chile' but got {result}"

    result = city_country('paris', 'france')
    assert result == 'Paris, France', f"Expected 'Paris, France' but got {result}"

    result = city_country('tokyo', 'japan')
    assert result == 'Tokyo, Japan', f"Expected 'Tokyo, Japan' but got {result}"

    result = city_country('new york', 'united states')
    assert result == 'New York, United States', f"Expected 'New York, United States' but got {result}"

def test_city_country_population():
    # Test cases to verify the city_country function with population
    result = city_country('santiago', 'chile', 5000000)
    assert result == 'Santiago, Chile – population 5,000,000', f"Expected 'Santiago, Chile – population 5,000,000' but got {result}"

    result = city_country('paris', 'france', 2148000)
    assert result == 'Paris, France – population 2,148,000', f"Expected 'Paris, France – population 2,148,000' but got {result}"

    result = city_country('tokyo', 'japan', 13960000)
    assert result == 'Tokyo, Japan – population 13,960,000', f"Expected 'Tokyo, Japan – population 13,960,000' but got {result}"

    result = city_country('new york', 'united states', 8419600)
    assert result == 'New York, United States – population 8,419,600', f"Expected 'New York, United States – population 8,419,600' but got {result}"