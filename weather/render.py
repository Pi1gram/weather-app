from jinja2 import Template
import logging
import os
from typing import Dict, Any


# Configure logging
logging.basicConfig(level=logging.INFO, format="%(message)s")
# Create a logger
logger = logging.getLogger(__name__)


def render_weather(city: str, weather_data: Dict[str, Any]) -> str:
    """
    Render weather information using a Jinja2 template.
    :param city: City name
    :param weather_data: Weather data
    :return: Rendered output
    """
    template_path = os.path.join(os.path.dirname(__file__), "text_render.jinja")
    with open(template_path, "r") as file:
        template_content = file.read()

    template = Template(template_content)
    rendered_output = template.render(city=city, weather_data=weather_data)
    logger.info(rendered_output)
    return rendered_output
