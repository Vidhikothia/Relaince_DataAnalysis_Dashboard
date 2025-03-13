import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

def plot_education_data(edu_df):
    # Plot 1: Enrollment by Location
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Location", y="Enrollment", data=edu_df, ci=None, palette="viridis")
    plt.title("Enrollment by Location")
    plt.xlabel("Location")
    plt.ylabel("Enrollment Count")
    plt.show()

    # Plot 2: Completion Rate Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(edu_df["Completion_Rate"], kde=True, color="blue")
    plt.title("Completion Rate Distribution")
    plt.xlabel("Completion Rate (%)")
    plt.ylabel("Frequency")
    plt.show()

    # Plot 3: Literacy Improvement by Location
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="Location", y="Literacy_Improvement", data=edu_df, palette="coolwarm")
    plt.title("Literacy Improvement by Location")
    plt.xlabel("Location")
    plt.ylabel("Literacy Improvement Score")
    plt.show()

def plot_healthcare_data(health_df):
    # Plot 1: Participants by Location
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Location", y="Participants", data=health_df, ci=None, palette="viridis")
    plt.title("Participants by Location")
    plt.xlabel("Location")
    plt.ylabel("Participants Count")
    plt.show()

    # Plot 2: Treatment Success Rate Distribution
    plt.figure(figsize=(10, 6))
    sns.histplot(health_df["Treatment_Success_Rate"], kde=True, color="green")
    plt.title("Treatment Success Rate Distribution")
    plt.xlabel("Success Rate (%)")
    plt.ylabel("Frequency")
    plt.show()

    # Plot 3: Satisfaction Score by Location
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="Location", y="Satisfaction_Score", data=health_df, palette="coolwarm")
    plt.title("Satisfaction Score by Location")
    plt.xlabel("Location")
    plt.ylabel("Satisfaction Score")
    plt.show()
