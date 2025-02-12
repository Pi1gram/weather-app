# Weather Forecast Project

## Description

This project retrieves and displays the weather forecast for a given city using the GoWeather API. The weather information includes temperature, wind, condition, and a forecast for the upcoming days.

## Features

- Fetch weather data from the GoWeather API
- Display weather information in the command line
- Render weather information using Jinja2 templates
- Unit tests for API and rendering functions

## Installation

To install the project dependencies, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://gitlab.com/theMarloGroup/training/jbhasin/intern_project.git
    cd intern_project
    ```

2. Create and activate a virtual environment:
    ```sh
    pip3 install virtualenv
    python3 -m virtualenv .venv
    source .venv/bin/activate  # For Unix-based systems
    # source .venv/Scripts/activate  # For Windows
    ```

3. Install the required packages:
    ```sh
    pip3 install -Ur requirements.txt
    ```

## Usage

To retrieve and display the weather forecast for a given city, run the following command:

```sh
python3 -m weather [city]