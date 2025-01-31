from pydantic_ai import Agent
from httpx import AsyncClient
from dataclasses import dataclass

response_agent = Agent(
    'openai:gpt-4o',
    system_prompt=(
        'Provide a detailed weather description based on the response from the weather agent. '
        'Include temperature, humidity, wind speed, and any notable conditions like rain, snow, or storms. '
        'Describe how the weather might feel to a person, such as whether it is comfortable, chilly, or humid.'
    ),
    retries=2,
    deps_type=str,
)
