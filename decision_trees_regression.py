import optuna
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.tree import DecisionTreeRegressor


diabetes = fetch_california_housing()
X, y = diabetes.data, diabetes.target
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.2, random_state=0)


def objective(trial):
    # hyperparameter ranges
    min_samples_split = trial.suggest_int('min_samples_split', 2, 40)
    min_samples_leaf = trial.suggest_int('min_samples_leaf', 2, 40)
    max_depth = trial.suggest_int('max_depth', 1, 100)

    # Create model with hyperparameters
    model = DecisionTreeRegressor(
        min_samples_split=min_samples_split,
        min_samples_leaf=min_samples_leaf,
        max_depth=max_depth,
        random_state=0
    )

    # fitting
    model.fit(X_train, y_train)

    pred = model.predict(X_test)
    mse = mean_squared_error(y_test, pred)

    return mse

study = optuna.create_study(direction='minimize')  # 'minimize' for less MSE
study.optimize(objective, n_trials=300)  # Numeric of test to find hyperparameters

best_params = study.best_params
best_mse = study.best_value
print("Best Hyperparameters:", best_params)
print("Best MSE:", best_mse)

best_min_samples_split = best_params['min_samples_split']
best_min_samples_leaf = best_params['min_samples_leaf']
best_max_depth = best_params['max_depth']

best_model = DecisionTreeRegressor(
    min_samples_split=best_min_samples_split,
    min_samples_leaf=best_min_samples_leaf,
    max_depth=best_max_depth,
    random_state=0
)

best_model.fit(X_train, y_train)
best_pred = best_model.predict(X_test)
best_mse = mean_squared_error(y_test, best_pred)
print("Best Model MSE:", best_mse)