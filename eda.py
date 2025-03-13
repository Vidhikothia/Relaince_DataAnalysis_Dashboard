import pandas as pd

def perform_eda(edu_df, health_df):
    print("\n🔍 Checking for Missing Values...")
    print("\nEducation Data:")
    print(edu_df.isnull().sum())
    print("\nHealthcare Data:")
    print(health_df.isnull().sum())

    print("\n📈 Education Data Info:")
    print(edu_df.info())
    print("\n📈 Healthcare Data Info:")
    print(health_df.info())
