import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Set style for plots
sns.set(style="whitegrid")

# Define file path
file_path = "Road Accident Data.xlsx"

# Load the Excel file
df = pd.read_excel(file_path, sheet_name="RAW DATA")

# Display dataset information
print("\n✅ Dataset loaded successfully!")
print(df.head())  # Show first few rows
print("\n🔍 Columns available in dataset:", df.columns)  # Verify column names

### 🟢 DATA CLEANING & PREPARATION ###

# Ensure 'Accident Date' column exists before conversion
if 'Accident Date' in df.columns:
    df['Accident Date'] = pd.to_datetime(df['Accident Date'], errors='coerce')
    df['Year'] = df['Accident Date'].dt.year
    df['Month'] = df['Accident Date'].dt.month
    df['Day_of_Week'] = df['Accident Date'].dt.day_name()
    print("\n✅ 'Accident Date' column successfully converted.")
else:
    print("\n⚠️ Warning: 'Accident Date' column not found. Skipping date-related analysis.")

# Ensure 'Time' column exists before extracting hour
if 'Time' in df.columns:
    df['Hour'] = pd.to_datetime(df['Time'], errors='coerce').dt.hour
    print("\n✅ 'Time' column successfully converted.")
else:
    print("\n⚠️ Warning: 'Time' column not found. Skipping hourly analysis.")

# Display basic dataset info
print("\n📊 Dataset Info:")
print(df.info())

# Total number of accidents
print("\n🚗 Total number of accidents:", df.shape[0])

# Define a function for safe plotting
def safe_countplot(column, title, order=None, rotate=False):
    if column in df.columns:
        plt.figure(figsize=(10,5))
        sns.countplot(x=column, data=df, order=order)
        plt.title(title)
        if rotate:
            plt.xticks(rotation=45)
        plt.show()
    else:
        print(f"\n⚠️ Warning: '{column}' column not found. Skipping {title} plot.")

### 🔹 1. Frequency of Accidents Over Time ###
fig, axes = plt.subplots(2, 2, figsize=(15, 10))

if 'Year' in df.columns:
    sns.countplot(x='Year', data=df, ax=axes[0,0])
    axes[0,0].set_title("Accidents Per Year")

if 'Month' in df.columns:
    sns.countplot(x='Month', data=df, ax=axes[0,1])
    axes[0,1].set_title("Accidents Per Month")

if 'Day_of_Week' in df.columns:
    sns.countplot(x='Day_of_Week', data=df, order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'], ax=axes[1,0])
    axes[1,0].set_title("Accidents Per Day of Week")

if 'Hour' in df.columns:
    sns.countplot(x='Hour', data=df, ax=axes[1,1])
    axes[1,1].set_title("Accidents Per Hour")

plt.tight_layout()
plt.show()

### 🔹 2. Geographical Distribution ###
safe_countplot('Location', "Accidents by Location", rotate=True)

### 🔹 3. Accident Severity Analysis ###
safe_countplot('Accident_Severity', "Accident Severity Distribution", order=['Slight','Serious','Fatal'])

if 'Accident_Severity' in df.columns:
    serious_fatal = df[df['Accident_Severity'].isin(['Serious', 'Fatal'])]
    print("\n⚠️ Percentage of Serious/Fatal Accidents:", (len(serious_fatal) / len(df)) * 100, "%")

### 🔹 4. Demographic Insights ###
safe_countplot('Gender', "Gender Distribution in Accidents")

if 'Age' in df.columns:
    plt.figure(figsize=(10,5))
    sns.histplot(df['Age'], bins=20, kde=True)
    plt.title("Age Distribution of People Involved in Accidents")
    plt.show()

### 🔹 5. Environmental and Road Conditions ###
safe_countplot('Weather_Conditions', "Accidents by Weather Condition")
safe_countplot('Road_Surface_Conditions', "Accidents by Road Surface Condition")
safe_countplot('Light_Conditions', "Accidents by Lighting Conditions")

### 🔹 6. Vehicle and Driver Information ###
safe_countplot('Vehicle_Type', "Vehicle Types Involved in Accidents")

### 🔹 7. Temporal Patterns ###
if 'Day_of_Week' in df.columns:
    df['Weekend'] = df['Day_of_Week'].isin(['Saturday', 'Sunday'])
    safe_countplot('Weekend', "Accidents: Weekdays vs. Weekends")

### 🔹 8. Contributing Factors ###
safe_countplot('Contributing_Factor', "Top Contributing Factors to Accidents", rotate=True)

### 🔹 9. Injury and Fatality Analysis ###
if 'Road_User_Type' in df.columns and 'Accident_Severity' in df.columns:
    plt.figure(figsize=(10,5))
    sns.countplot(y='Road_User_Type', hue='Accident_Severity', data=df)
    plt.title("Injuries and Fatalities by Road User Type")
    plt.show()

### 🔹 10. Comparative Analysis ###
safe_countplot('Urban_or_Rural_Area', "Accidents: Urban vs. Rural")

### ✅ Save cleaned dataset
output_file = "cleaned_road_accident_data.csv"
df.to_csv(output_file, index=False)
print(f"\n📂 Cleaned dataset saved as '{output_file}'")
