import pandas as pd
import re

def preprocess(data):
    # Split the data into lines
    lines = data.split('\n')
    
    # Create a list to hold the processed messages
    messages = []
    
    for line in lines:
        # Use regex to extract the date, user, and message
        match = re.match(r'(\d+/\d+/\d+,\s\d+:\d+\s[ap]m)\s-\s(.*?):\s(.*)', line)
        if match:
            date, user, message = match.groups()
            messages.append([date, user, message])
        else:
            print(f"No match for line: {line}")  # Debugging line to show unmatched lines
    
    # Create a DataFrame
    df = pd.DataFrame(messages, columns=['date', 'user', 'message'])
    
    # Debugging: Print the number of messages processed
    print(f"Total messages processed: {len(messages)}")
    
    # Convert the 'message' column to string type
    df['message'] = df['message'].astype(str)
    
    # Convert 'date' column to datetime
    df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y, %I:%M %p')
    
    # Extract additional features
    df['only_date'] = df['date'].dt.date  # Create 'only_date' column
    df['year'] = df['date'].dt.year
    df['month'] = df['date'].dt.month_name()
    df['month_num'] = df['date'].dt.month
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    
    return df
