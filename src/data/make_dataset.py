import pandas as pd
# from Enum import Enum
from src.utils.config import load_config
from src.utils.store import AssignmentStore
# from src.utils.specs import specs_config
def imp_status(Enum):

# Extraction and Transform    
def main():
    pass



def clean_booking_df(df: pd.DataFrame) -> pd.DataFrame: #clean different data files
    unique_columns = [
        "order_id",
        "trip_distance",
        "pickup_latitude",
        "pickup_longitude",
        "booking_status",
        "driver_id"
    ]
    # drop duplicates - need a test?
    df = df.drop_duplicates(subset=unique_columns)
    # Also acts as a test to remove other values
    df = df[df.booking_status.isin(['COMPLETED','CUSTOMER_CANCELLED','DRIVER_CANCELLED'])]

    df = df.dropna(subset = ['event_timestamp'])

    return df

def clean_participant_df(df:pd.DataFrame) -> pd.DataFrame: #clean different data files
    df = df.drop_duplicates()

    df = df[df.participant_status.isin(['ACCEPTED','REJECTED'])]
    return df

def merge_dataset(bookings: pd.DataFrame, participants: pd.DataFrame) -> pd.DataFrame:
    df = pd.merge(bookings, participants, how="left", on="order_id")
    
    df = df[~((df.booking_status == 'CUSTOMER_CANCELLED') & (df.participant_status.isnull()))]

def create_target(df: pd.DataFrame, target_col: str):
    df[target_col] = df["booking_status"].apply(lambda x:int(x=="COMPLETED"))
    return df