import pandas as pd
import numpy as np

def generate_data():
    # Generate Education Data
    education_data = {
        "Program_ID": np.arange(1, 101),
        "Location": np.random.choice(["Urban", "Rural", "Semi-Urban"], 100),
        "Enrollment": np.random.randint(50, 500, 100),
        "Completion_Rate": np.random.uniform(50, 100, 100),
        "Literacy_Improvement": np.random.uniform(0, 100, 100)
    }
    edu_df = pd.DataFrame(education_data)
    edu_df.to_csv("education_data.csv", index=False)
    
    # Generate Healthcare Data
    healthcare_data = {
        "Camp_ID": np.arange(1, 101),
        "Location": np.random.choice(["Urban", "Rural", "Semi-Urban"], 100),
        "Participants": np.random.randint(30, 300, 100),
        "Treatment_Success_Rate": np.random.uniform(50, 100, 100),
        "Satisfaction_Score": np.random.uniform(0, 100, 100)
    }
    health_df = pd.DataFrame(healthcare_data)
    health_df.to_csv("healthcare_data.csv", index=False)

    print("✅ Sample data generated and saved to CSV files!")

if __name__ == "__main__":
    generate_data()
