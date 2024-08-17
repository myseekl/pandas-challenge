# Dependencies and Setup
import pandas as pd
from pathlib import Path

# File to Load (Remember to Change These)
school_data_to_load = Path("Resources/schools_complete.csv")
student_data_to_load = Path("Resources/students_complete.csv")

# Read School and Student Data File and store into Pandas DataFrames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)

# Combine the data into a single dataset.
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete

# Find total number of unique schools; used Xpert Learning Assitant to help with the code.

# Access "school_name" column from the DATAFRAME: school_data_completed 
school_names = school_data_complete["school_name"]

# Generate an empty set to store unique school names
unique_school = set()

# Iterate over the values in the 'school_name' column and add unique school names to the set
for school_name in school_names:
    unique_school.add(school_name)

# Count total number of unique school names
unique_school_count = len(unique_school)

print("Total count of schools:", unique_school_count)
