# OpenF1 Python SDK

A Python SDK for the [OpenF1 Api](https://github.com/br-g/openf1) that provides easy access to Formula 1 data.

## Introduction

This Python SDK simplifies interactions with the OpenF1 API, allowing you to easily retrieve various types of Formula 1 data such as lap times, driver information, car telemetry, and more directly within your Python applications.

NB: As this is a side project developed in my spare time with assistance from Gemini CLI, please bear with any imperfections.

## Installation

To install the OpenF1 Python SDK, you can use pip:

```bash
pip install openf1-sdk
```

### Dependencies

The SDK relies on the following core dependencies:
- `requests`: For making HTTP requests to the OpenF1 API.
- `pydantic`: For data validation and parsing API responses into Python objects.
- `pandas`: For convenient data manipulation and analysis of API responses.
- `loguru`: For flexible logging.

## Usage

Here's a quick example demonstrating how to fetch lap data for a specific driver and session:

```python
from openf1.client import OpenF1Client
import pandas as pd

def main():
    client = OpenF1Client()

    # Example: Get lap data for driver 63 (George Russell) in session 9161 (2023 Abu Dhabi Grand Prix - Race)
    laps = client.laps.get_laps(
        session_key=9161, 
        driver_number=63, 
        lap_number=8
    )
    if laps:
        df = pd.DataFrame([d.model_dump() for d in laps])
        print(df)
    else:
        print("No lap data found.")

if __name__ == "__main__":
    main()
```

## Available Endpoints

The `OpenF1Client` provides access to the following data endpoints:

- `client.car_data`: Access car telemetry data.
- `client.drivers`: Retrieve driver information.
- `client.intervals`: Get interval data between cars.
- `client.laps`: Fetch lap-by-lap data.
- `client.location`: Obtain car location data.
- `client.meetings`: Get information about race meetings.
- `client.overtakes`: Access overtake events data.
- `client.pit`: Retrieve pit stop data.
- `client.position`: Get car position data.
- `client.race_control`: Access race control messages.
- `client.session_result`: Get session results.
- `client.sessions`: Retrieve session information.
- `client.starting_grid`: Access starting grid data.
- `client.stints`: Get stint data.
- `client.team_radio`: Access team radio messages.
- `client.weather`: Retrieve weather data.

Each endpoint typically offers a `get_<data_type>` method (e.g., `client.laps.get_laps()`) which accepts keyword arguments (`**kwargs`) for filtering and querying the data. These keyword arguments directly correspond to the available query parameters of the OpenF1 API.

## Data Models

The SDK utilizes Pydantic models to represent the data returned by the OpenF1 API. This ensures type safety and easy access to data attributes. Each endpoint's `get_` method returns a list of corresponding Pydantic model instances (e.g., `List[Lap]` for `client.laps.get_laps()`).

## Contributing

Contributions are welcome! Please refer to the main project's `CONTRIBUTING.md` for guidelines on how to contribute.

## License

This SDK is released under the MIT License. See the `LICENSE` file in the main project repository for more details.