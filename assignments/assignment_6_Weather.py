import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV data
file_path = r"C:\Users\Chris\Desktop\PFDA\assignments\hly4935.csv"
column_names = ['date', 'ind1', 'rain', 'ind2', 'temp', 'ind3', 'wetb', 'dewpt', 'vappr', 'rhum',
                'msl', 'ind4', 'wdsp', 'ind5', 'wddir', 'ww', 'w', 'sun', 'vis', 'clht', 'clamt']
data = pd.read_csv(file_path, skiprows=8, names=column_names, header=None, low_memory=False)

# Convert date and temperature
data['date'] = pd.to_datetime(data['date'], errors='coerce', format='%d-%b-%Y %H:%M')
data['temp'] = pd.to_numeric(data['temp'], errors='coerce')

# Drop rows with missing values
data = data.dropna(subset=['date', 'temp'])

# Plot Temperature vs Date
plt.figure(figsize=(10, 5))
plt.plot(data['date'], data['temp'], color='orange', label='Temperature')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Calculate and plot Mean Temperature per Day
data['mean_temp'] = data.groupby(data['date'].dt.date)['temp'].transform('mean')
plt.figure(figsize=(10, 5))
plt.plot(data['date'], data['mean_temp'], color='blue', label='Mean Temperature')
plt.xlabel('Date')
plt.ylabel('Mean Temperature (°C)')
plt.title('Mean Temperature Per Day')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Calculate and plot Mean Temperature per Month
data['month'] = data['date'].dt.to_period('M')
monthly_mean_temp = data.groupby('month')['temp'].mean()

plt.figure(figsize=(10, 5))
monthly_mean_temp.plot(color='green', label='Mean Monthly Temperature')
plt.xlabel('Month')
plt.ylabel('Mean Temperature (°C)')
plt.title('Mean Temperature Per Month')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()


