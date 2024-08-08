from pandas as pd
from sklearn.model_selection import train_test_split

from src.features.transformations import (
    driver_distance_to_pickup,
    driver_historical_completed_booking
)
from src.utils.store import AssignmentStore
def main():
    store = AssignmentStore()

    dataset = store.get_processed("dataset.csv")
    dataset = apply_feature_engineering(dataset)


def apply_feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.pipe(driver_distance_to_pickup)
        .pipe(driver_historical_completed_booking)
    )

