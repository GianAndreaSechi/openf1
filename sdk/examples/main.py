from openf1.client import OpenF1Client
import pandas as pd

def main():
    client = OpenF1Client()

    # Get car data for a specific driver in a session
    # car_data_list = client.car_data.get_car_data(
    #     session_key=9159,
    #     driver_number=55,
    #     speed='>=150'
    # )

    # if car_data_list:
    #     # Convert the list of Pydantic models to a DataFrame for display
    #     df = pd.DataFrame([d.model_dump() for d in car_data_list])
    #     print(df)

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
