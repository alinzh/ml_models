from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

diabetes = fetch_california_housing()
X, y = diabetes.data, diabetes.target
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

reg1 = GradientBoostingRegressor(
    random_state=0,
    max_depth=80,
    n_estimators=400,
    min_samples_split=5
)

reg2 = RandomForestRegressor(
    random_state=0,
    max_depth=100,
    n_estimators=600,
    min_samples_split=5
)

reg1 = reg1.fit(X_train, y_train)
# reg2 = reg2.fit(X_train, y_train)

pred_1 = reg1.predict(X_test)
# pred_2 = reg2.predict(X_test)

mse_1 = mean_squared_error(y_test, pred_1)
# mse_2 = mean_squared_error(y_test, pred_2)

print("GradientBoostingRegressor MSE:", mse_1)
# print("RandomForestRegressor Model MSE:", mse_2)

