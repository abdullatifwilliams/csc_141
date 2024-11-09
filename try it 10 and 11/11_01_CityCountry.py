import pytest
from city_functions import city_country  # Import the function to test

def test_city_country():
    # Test cases to verify the city_country function
    result = city_country('santiago', 'chile')
    assert result == 'Santiago, Chile', f"Expected 'Santiago, Chile' but got {result}"

    result = city_country('paris', 'france')
    assert result == 'Paris, France', f"Expected 'Paris, France' but got {result}"

    result = city_country('tokyo', 'japan')
    assert result == 'Tokyo, Japan', f"Expected 'Tokyo, Japan' but got {result}"

    result = city_country('new york', 'united states')
    assert result == 'New York, United States', f"Expected 'New York, United States' but got {result}"