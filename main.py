from data_generator import generate_data
from data_loader import load_data
from eda import perform_eda
from model_trainer import train_models
from visualizer import plot_education_data, plot_healthcare_data

if __name__ == "__main__":
    # Step 1: Generate Data
    generate_data()
    
    # Step 2: Load Data
    edu_df, health_df = load_data()
    
    # Step 3: Perform EDA
    perform_eda(edu_df, health_df)
    
    # Step 4: Train and Evaluate Models
    train_models(edu_df, health_df)
    
    # Step 5: Visualize the Data
    plot_education_data(edu_df)
    plot_healthcare_data(health_df)
