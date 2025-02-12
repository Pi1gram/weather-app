"""Test the render_weather function."""

from weather.render import render_weather


def test_render_weather_basic():
    """Test the render_weather function."""
    city = "Test City"
    weather_data: dict[str, str | list[dict[str, str]]] = {
        "temperature": "20°C",
        "wind": "5 km/h",
        "description": "Sunny",
        "forecast": [],
    }

    expected_output = (
        "Weather in Test City:\n- Temperature: 20°C\n- Wind: 5 km/h\n- Condition: Sunny"
    )
    out = render_weather(city, weather_data)
    assert out == expected_output


def test_render_weather_with_forecast():
    """Test the render_weather function with forecast data."""
    city = "Test City"
    weather_data: dict[str, str | list[dict[str, str]]] = {
        "temperature": "20°C",
        "wind": "5 km/h",
        "description": "Sunny",
        "forecast": [
            {"day": "Monday", "temperature": "22°C", "wind": "10 km/h"},
            {"day": "Tuesday", "temperature": "18°C", "wind": "15 km/h"},
        ],
    }

    expected_output = (
        "Weather in Test City:\n"
        "- Temperature: 20°C\n"
        "- Wind: 5 km/h\n"
        "- Condition: Sunny\n"
        "Forecast:\n"
        "  Day Monday: 22°C, Wind: 10 km/h\n"
        "  Day Tuesday: 18°C, Wind: 15 km/h"
    )
    out = render_weather(city, weather_data)
    print(render_weather(city, weather_data))
    print(expected_output)

    assert out == expected_output


def test_render_weather_empty_forecast():
    """Test the render_weather function with an empty forecast."""
    city = "Test City"
    weather_data: dict[str, str | list[dict[str, str]]] = {
        "temperature": "20°C",
        "wind": "5 km/h",
        "description": "Sunny",
        "forecast": [],
    }

    expected_output = (
        "Weather in Test City:\n- Temperature: 20°C\n- Wind: 5 km/h\n- Condition: Sunny"
    )
    out = render_weather(city, weather_data)

    assert out == expected_output
