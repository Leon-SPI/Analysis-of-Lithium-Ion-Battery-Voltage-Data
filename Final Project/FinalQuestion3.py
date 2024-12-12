import pandas as pd
import numpy as np
from pathlib import Path

# Load the CSV file
current_dir = Path(__file__).parent

# Construct the file path
csv_file_path = current_dir / "regular_alt_batteries" / "battery20.csv"
data = pd.read_csv(csv_file_path)

# Extract relevant columns
time = data['time']
battery_voltage = data['voltage_charger']
load_voltage = data['voltage_load']
load_current = data['current_load']
mode_data = data['mode']
battery_temp = data['temperature_battery']

# Initialize lists to hold the first and last voltage and temperature values for each discharge cycle
first_voltage_indices = []
last_voltage_indices = []

# Iterate through the mode_data to find the start and end of each discharge cycle
for i in range(len(mode_data)):
    if mode_data[i] == -1 and mode_data[i - 1] != -1:
        if mode_data[i + 3] == -1:
            first_voltage_indices.append(i + 3)
    if mode_data[i] == -1 and mode_data[i + 1] != -1:
        if mode_data[i - 3] == -1:
            last_voltage_indices.append(i - 3)

# Convert the indices lists to NumPy arrays
first_voltage_indices = np.array(first_voltage_indices)
last_voltage_indices = np.array(last_voltage_indices)

# Initialize empty lists
first_voltage_values = []
first_voltage_time = []
last_voltage_values = []
last_voltage_time = []
cycle_mean_current = []
start_temperature = []
end_temperature = []
temp_exceeds_60 = []

# Extract values based on indices
for i in first_voltage_indices:
    first_voltage_values.append(battery_voltage[i])
    first_voltage_time.append(time[i])
    start_temperature.append(battery_temp[i])

for i in last_voltage_indices:
    last_voltage_values.append(battery_voltage[i])
    last_voltage_time.append(time[i])
    end_temperature.append(battery_temp[i])

# Check if the temperature exceeds 60 degrees Celsius
for start_temp, end_temp in zip(start_temperature, end_temperature):
    if start_temp > 45 or end_temp > 45:
        temp_exceeds_60.append("Yes")
    else:
        temp_exceeds_60.append("No")

# Print total number of cycles
print(f'Number of cycles: {len(first_voltage_values)}')

# Calculate the mean current for each cycle
for i in range(len(first_voltage_indices)):
    mean_current = np.mean(load_current[first_voltage_indices[i]:last_voltage_indices[i]])
    cycle_mean_current.append(mean_current)

# Calculate the time taken for each cycle
time_taken = np.array(last_voltage_time) - np.array(first_voltage_time)

# Calculate the rate of change in voltage for each cycle
rate_of_change = (np.array(last_voltage_values) - np.array(first_voltage_values)) / time_taken

# Create a DataFrame to store the data
df = pd.DataFrame({
    'Start Voltage (V)': first_voltage_values,
    'End Voltage (V)': last_voltage_values,
    'Rate of Change (V/s)': rate_of_change,
    'Time Taken (s)': time_taken,
    'Average Current (A)': cycle_mean_current,
    'Start Temperature (°C)': start_temperature,
    'End Temperature (°C)': end_temperature,
    'Battery Overheating': temp_exceeds_60
})

# Set pandas options to display all columns in the same space
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

# Print the table
print(df)
