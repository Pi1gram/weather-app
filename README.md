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

### Clone the repository

```sh
git clone https://gitlab.com/theMarloGroup/training/jbhasin/intern_project.git
cd intern_project
```

### Create and activate a virtual environment

```sh
pip3 install virtualenv
python3 -m virtualenv .venv
source .venv/bin/activate  # For Unix-based systems
# source .venv/Scripts/activate  # For Windows
```

### Install the required packages

```sh
pip3 install -Ur requirements.txt
```

## Usage

To retrieve and display the weather forecast for a given city, run the following command:

```sh
python3 -m weather [city]
```

## GitLab CI/CD Pipeline

This project uses GitLab CI/CD to automate the process of linting, testing, and validating the code. The pipeline is defined in the `.gitlab-ci.yml` file and consists of a single stage called `validate`.

### Pipeline Stages

#### validate job

This stage sets up the environment, installs dependencies, checks formatting, lints the code, and runs unit tests.

### Explanation

#### default

Specifies default settings for all jobs. The `tags` keyword indicates that jobs should be picked up by runners tagged with `build-runner`.

#### stages

Defines a single stage called `validate`.

#### cache

Configures caching for the virtual environment (`.venv`). The cache is pulled before running the job and pushed after the job completes.

#### validate

 A job that runs in the `validate` stage. It sets up the environment, installs dependencies, checks formatting, lints the code, and runs unit tests. The generated artifacts (e.g., linting reports and test reports) are stored in the `public` directory.

By combining all tasks into a single `validate` stage, the pipeline becomes simpler and faster. The virtual environment is cached to speed up subsequent pipeline runs, and only the generated artifacts are stored.

### Reports

- [Wiki](https://gitlab.com/theMarloGroup/training/students/jbhasin/initial/-/wikis/home)
- [API](https://themarlogroup.gitlab.io/training/students/jbhasin/initial)
- [Coverage](https://themarlogroup.gitlab.io/training/students/jbhasin/initial/coverage/index.html)
- [Test](https://themarlogroup.gitlab.io/training/students/jbhasin/initial/pytest_report.html)
