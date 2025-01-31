import asyncio
import os
from httpx import AsyncClient
import logfire
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from weather_agent import weather_agent, Deps
from response_generator_agent import response_agent

# 'if-token-present' means nothing will be sent (and the example will work) if you don't have logfire configured
logfire.configure(send_to_logfire='if-token-present')


async def main():
    async with AsyncClient() as client:
        # Get location from user input
        location = input("Enter a location: ")
        # create a free API key at https://www.tomorrow.io/weather-api/
        weather_api_key = os.getenv('WEATHER_API_KEY')
        # create a free API key at https://geocode.maps.co/
        geo_api_key = os.getenv('GEO_API_KEY')
        deps = Deps(
            client=client, weather_api_key=weather_api_key, geo_api_key=geo_api_key
        )
        result = await weather_agent.run(
            f'What is the weather like in {location}?', deps=deps
        )
        response = await response_agent.run(
            f'Please generate a response based on the weather data for {location}: {result.data}',
            deps=result.data,
        )
        print('Response:', response.data)


if __name__ == "__main__":
    asyncio.run(main())
