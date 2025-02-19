import requests
import logging

API_URL = "https://goweather.herokuapp.com/weather/{}"

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
logger = logging.getLogger(__name__)


def get_weather(city: str) -> dict[str, str]:
    """
    Fetch weather data from the API.
    :param city: City name
    :return: Weather data
    """
    response = requests.get(API_URL.format(city), timeout=10)
    response.raise_for_status()
    print(response.json().keys())
    return response.json()
