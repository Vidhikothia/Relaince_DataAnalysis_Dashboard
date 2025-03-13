import pandas as pd

def load_data():
    edu_df = pd.read_csv("education_data.csv")
    health_df = pd.read_csv("healthcare_data.csv")
    return edu_df, health_df

if __name__ == "__main__":
    edu_df, health_df = load_data()
    print("📂 Education Data:")
    print(edu_df.head())
    print("\n📂 Healthcare Data:")
    print(health_df.head())
