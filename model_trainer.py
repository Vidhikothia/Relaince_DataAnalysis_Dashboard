from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import pandas as pd

def train_models(edu_df, health_df):
    # Education Model
    edu_features = pd.get_dummies(edu_df[["Enrollment", "Location"]], drop_first=True)
    edu_target = edu_df["Literacy_Improvement"]
    X_train_edu, X_test_edu, y_train_edu, y_test_edu = train_test_split(edu_features, edu_target, test_size=0.2, random_state=42)

    edu_model = LinearRegression().fit(X_train_edu, y_train_edu)
    y_pred_edu = edu_model.predict(X_test_edu)
    print(f"\n📚 Education Model MSE: {mean_squared_error(y_test_edu, y_pred_edu)}")
    print(f"📚 Education Model R² Score: {r2_score(y_test_edu, y_pred_edu)}")

    # Healthcare Model
    health_features = pd.get_dummies(health_df[["Participants", "Location"]], drop_first=True)
    health_target = health_df["Treatment_Success_Rate"]
    X_train_health, X_test_health, y_train_health, y_test_health = train_test_split(health_features, health_target, test_size=0.2, random_state=42)

    health_model = LinearRegression().fit(X_train_health, y_train_health)
    y_pred_health = health_model.predict(X_test_health)
    print(f"\n🏥 Healthcare Model MSE: {mean_squared_error(y_test_health, y_pred_health)}")
    print(f"🏥 Healthcare Model R² Score: {r2_score(y_test_health, y_pred_health)}")
