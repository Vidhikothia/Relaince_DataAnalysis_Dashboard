import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

# Load Data
@st.cache_data
def load_data():
    edu_df = pd.read_csv("education_data.csv")
    health_df = pd.read_csv("healthcare_data.csv")
    return edu_df, health_df

edu_df, health_df = load_data()

# Dashboard Title
st.title("Reliance Foundation Data Analysis Dashboard")
st.sidebar.title("Navigation")

# Sidebar Navigation
options = ["Education Data", "Healthcare Data"]
choice = st.sidebar.selectbox("Select Dataset to Visualize", options)

# Common Filter for Both Datasets
st.sidebar.subheader("Filter Data by Location")
locations = sorted(edu_df["Location"].unique())
selected_location = st.sidebar.selectbox("Choose Location", ["All"] + locations)

if selected_location != "All":
    edu_df = edu_df[edu_df["Location"] == selected_location]
    health_df = health_df[health_df["Location"] == selected_location]

# Education Data Visualization
if choice == "Education Data":
    st.header("📚 Education Data Analysis")

    # Display Dataset
    st.write("### Education Dataset")
    st.dataframe(edu_df)

    # Plot 1: Enrollment by Location
    st.write("### 📊 Enrollment by Location")
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Location", y="Enrollment", data=edu_df, ci=None, palette="viridis")
    plt.title("Enrollment by Location")
    plt.xticks(rotation=45)
    st.pyplot(plt)
    plt.clf()

    # Plot 2: Completion Rate Distribution
    st.write("### 📈 Completion Rate Distribution")
    plt.figure(figsize=(10, 6))
    sns.histplot(edu_df["Completion_Rate"], kde=True, color="blue")
    plt.title("Completion Rate Distribution")
    st.pyplot(plt)
    plt.clf()

    # Plot 3: Literacy Improvement by Location
    st.write("### 📉 Literacy Improvement by Location")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="Location", y="Literacy_Improvement", data=edu_df, palette="coolwarm")
    plt.title("Literacy Improvement by Location")
    plt.xticks(rotation=45)
    st.pyplot(plt)
    plt.clf()

    # Generate Insights
    st.write("### 📋 Insights")
    avg_completion = edu_df["Completion_Rate"].mean()
    avg_literacy_improvement = edu_df["Literacy_Improvement"].mean()
    st.write(f"Average Completion Rate: **{avg_completion:.2f}%**")
    st.write(f"Average Literacy Improvement: **{avg_literacy_improvement:.2f}**")

# Healthcare Data Visualization
elif choice == "Healthcare Data":
    st.header("🏥 Healthcare Data Analysis")
    
    # Display Dataset
    st.write("### Healthcare Dataset")
    st.dataframe(health_df)

    # Plot 1: Participants by Location
    st.write("### 📊 Participants by Location")
    plt.figure(figsize=(10, 6))
    sns.barplot(x="Location", y="Participants", data=health_df, ci=None, palette="viridis")
    plt.title("Participants by Location")
    plt.xticks(rotation=45)
    st.pyplot(plt)
    plt.clf()

    # Plot 2: Treatment Success Rate Distribution
    st.write("### 📈 Treatment Success Rate Distribution")
    plt.figure(figsize=(10, 6))
    sns.histplot(health_df["Treatment_Success_Rate"], kde=True, color="green")
    plt.title("Treatment Success Rate Distribution")
    st.pyplot(plt)
    plt.clf()

    # Plot 3: Satisfaction Score by Location
    st.write("### 📉 Satisfaction Score by Location")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x="Location", y="Satisfaction_Score", data=health_df, palette="coolwarm")
    plt.title("Satisfaction Score by Location")
    plt.xticks(rotation=45)
    st.pyplot(plt)
    plt.clf()

    # Generate Insights
    st.write("### 📋 Insights")
    avg_success_rate = health_df["Treatment_Success_Rate"].mean()
    avg_satisfaction_score = health_df["Satisfaction_Score"].mean()
    st.write(f"Average Treatment Success Rate: **{avg_success_rate:.2f}%**")
    st.write(f"Average Satisfaction Score: **{avg_satisfaction_score:.2f}**")
