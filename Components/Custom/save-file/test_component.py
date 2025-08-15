#!/usr/bin/env python3
"""
Test script to verify the DataFrame creation logic works with JSON data.
"""

import pandas as pd

# Simulate the data structure that comes from the JSON file
test_data = [
    {"id": 1, "first_name": "Tobe", "last_name": "O'Logan", "email": "tologan0@flavors.me", "gender": "Female", "ip_address": "129.108.64.170"},
    {"id": 2, "first_name": "Livvie", "last_name": "Wastling", "email": "lwastling1@theatlantic.com", "gender": "Genderfluid", "ip_address": "125.79.122.29"},
    {"id": 3, "first_name": "Jeannine", "last_name": "Testro", "email": "jtestro2@cyberchimps.com", "gender": "Agender", "ip_address": "112.101.29.51"}
]

def create_dataframe_from_data(data):
    """Test the DataFrame creation logic."""
    try:
        if isinstance(data, list) and len(data) > 0:
            if isinstance(data[0], dict):
                # List of dictionaries - perfect for DataFrame
                return pd.DataFrame(data)
            else:
                # List of other types - try to convert directly
                return pd.DataFrame(data)
        elif isinstance(data, dict):
            # Single dictionary - convert to DataFrame with one row
            return pd.DataFrame([data])
        else:
            # Other data types - try to convert directly
            return pd.DataFrame(data)
    except Exception as e:
        print(f"Error creating DataFrame from data: {str(e)}")
        raise

# Test the function
print("Testing DataFrame creation...")
df = create_dataframe_from_data(test_data)
print(f"DataFrame created successfully!")
print(f"Shape: {df.shape}")
print(f"Columns: {list(df.columns)}")
print("\nFirst few rows:")
print(df.head())

# Test saving to CSV
print("\nTesting CSV export...")
df.to_csv("test_output.csv", index=False)
print("CSV file created successfully!")

print("\n✅ All tests passed!")
