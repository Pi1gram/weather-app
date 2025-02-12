"""Imports"""

import argparse
from weather.api import get_weather
from weather.render import render_weather
import logging
from requests.exceptions import HTTPError

__version__ = "1.0.0"


def main():
    """
    The main function retrieves and displays the weather forecast for a given city
    using command-line arguments.
    """
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    logging.getLogger(__name__)
    parser = argparse.ArgumentParser(
        prog="weather",
        usage="python3 -m weather [city] [options]",
        description="Retrieve the weather forecast for a given city.",
        epilog="Example: python3 -m weather Melbourne",
    )
    parser.add_argument("city", nargs="?", default="Melbourne", help="City name")

    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"weather version {__version__}",
        help="Show the version number and exit.",
    )
    parser = argparse.ArgumentParser(
        description="Retrieve the weather forecast for a given city."
    )
    parser.add_argument(
        "city", nargs="?", default="Melbourne", help="City name (default: Melbourne)"
    )

    args = parser.parse_args()
    try:
        weather_data = get_weather(args.city)
        render_weather(args.city, weather_data)
    except HTTPError:
        logging.exception("An error occurred while fetching weather data.")


if __name__ == "__main__":
    main()
