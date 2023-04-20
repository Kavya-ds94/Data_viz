import pandas as pd

# Load the data into a pandas DataFrame
df = pd.read_csv('WhatsgoodlyData-6.csv',encoding='latin-1')

# Remove rows with count=0
df = df[df['Count'] != 0]

# Rename the columns
df = df.rename(columns={'Segment Type': 'Segment_Type'})
df = df.rename(columns={'Segment Description': 'Segment_Description'})
df = df.rename(columns={'Answer': 'Platform'})

# Drop the column to be removed
df = df.drop('Question', axis=1)
df = df.drop('Percentage', axis=1)
df = df.drop('Segment_Type', axis=1)

# Group by the Segment_Description, and Platform columns and sum the Count column
summed_df = df.groupby(['Segment_Description', 'Platform']).agg({'Count': 'sum'}).reset_index()

# Save the resulting DataFrame to a CSV file
summed_df.to_csv('Social_media_shopping.csv', index=False)