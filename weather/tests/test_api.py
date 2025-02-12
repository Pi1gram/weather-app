"""imports"""

import requests
from weather.api import get_weather
from pytest_mock import MockerFixture
import pytest


@pytest.fixture
def weather_response() -> dict[str, str | list[dict[str, str]]]:
    """Create a sample weather response."""
    return {
        "temperature": "20°C",
        "wind": "10 km/h",
        "description": "Sunny",
        "forecast": [{"day": "1", "temperature": "18°C", "wind": "5 km/h"}],
    }


@pytest.fixture
def mock_response(
    mocker: MockerFixture, weather_response: dict[str, str | list[dict[str, str]]]
):
    """Create a mock response object."""
    mock_response = mocker.Mock()
    mock_response.json.return_value = weather_response
    return mock_response


def test_get_weather_success(
    mocker: MockerFixture,
    mock_response: requests.models.Response,
    weather_response: dict[str, str | list[dict[str, str]]],
):
    """Test a successful API call."""
    mocker.patch("weather.api.requests.get", return_value=mock_response)
    result = get_weather("London")
    assert result == weather_response


def test_get_weather_no_temperature(
    mocker: MockerFixture, caplog: pytest.LogCaptureFixture
):
    """Test a successful API call with missing temperature data."""
    mock_response = mocker.Mock()
    mock_response.json.return_value = {
        "wind": "10 km/h",
        "description": "Sunny",
        "forecast": [{"day": "1", "temperature": "18°C", "wind": "5 km/h"}],
    }
    mocker.patch("weather.api.requests.get", return_value=mock_response)
    result = get_weather("London")
    assert result == {
        "wind": "10 km/h",
        "description": "Sunny",
        "forecast": [{"day": "1", "temperature": "18°C", "wind": "5 km/h"}],
    }


def test_get_weather_api_failure(mocker: MockerFixture):
    """Test a failed API call."""
    mocker.patch(
        "weather.api.requests.get", side_effect=requests.exceptions.RequestException
    )

    with pytest.raises(requests.exceptions.RequestException):
        get_weather("London")


def test_get_weather_invalid_city(mocker: MockerFixture):
    """Test a failed API call."""
    mocker.patch("weather.api.requests.get", side_effect=requests.HTTPError)

    with pytest.raises(requests.HTTPError):
        get_weather("asd")
