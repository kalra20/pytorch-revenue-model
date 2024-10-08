# Model with abstraction
from abc import ABC, abstractmethod
from typing import List, Dict
from sklearn.linear_model import LogisticRegression

import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator

class Classifier(ABC):
    @abstractmethod
    def train(self, **params) -> None:
        pass

    @abstractmethod
    def evaluate(self, **params) -> Dict[str, float]:
        pass

    @abstractmethod
    def predict(self, **params) -> np.ndarray:
        pass

class SklearnClassifier(Classifier):
    def __init__(
            self, estimator: BaseEstimator, features: List[str], target:str
            ):
        self.clf = estimator
        self.features = features
        self.target = target

    def train(self, df_train: pd.DataFrame):
        self.clf.fit(df_train[self.features].values, df_train[self.target].values)

    def evaluate(self, df_test: pd.DataFrame) -> Dict[str, float]:
        raise NotImplementedError(
            f"You're almost there! Identify an appropriate evaluation metric for your model and implement it here. "
            f"The expected output is a dictionary of the following schema: {{metric_name: metric_score}}"
        )

    def predict(self, df:pd.DataFrame)->np.ndarray:
        return self.clf.predict_proba(df[self.features].values)[:,1]
    

