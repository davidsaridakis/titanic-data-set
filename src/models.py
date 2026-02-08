from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline


def get_models():
    """
    Returns a {dictionary of model_name : model_instance}.
    All models used fixed random_state for reproducibility.
    Logistic Regresion includes scaling via Pipeline.
    """
    models = {
        "Logistic Regression": Pipeline([
            ("scaler", StandardScaler()),
            ("model", LogisticRegression(max_iter=5000, solver="liblinear", random_state=42))
        ]),
        "Random Forest": RandomForestClassifier(
            n_estimators=100, 
            random_state=42
        ),
        "Gradient Boosting": GradientBoostingClassifier(
            n_estimators=100,
            learning_rate=0.1,
            max_depth=3,
            random_state=42
        )
    }

    return models