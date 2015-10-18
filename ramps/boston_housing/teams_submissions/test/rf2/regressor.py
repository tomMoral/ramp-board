from sklearn.base import BaseEstimator
from sklearn.ensemble import RandomForestRegressor


class Regressor(BaseEstimator):
    def __init__(self):
        pass

    def fit(self, X, y):
        self.reg = RandomForestRegressor(
            n_estimators=10, max_leaf_nodes=5)
        self.reg.fit(X, y)

    def predict(self, X):
        return self.reg.predict(X)
