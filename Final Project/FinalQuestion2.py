import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from FinalQuestion1 import cycle_index_start_finish
from FinalQuestion1 import reverse_cycle_index_start_finish
import math

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

# Get the start and end indices for the first cycle using the custom function
first_cycle_start, first_cycle_end = cycle_index_start_finish(mode_data)
last_cycle_start, last_cycle_end = reverse_cycle_index_start_finish(mode_data)

# The code below extracts the relevant data for the last cycle.
# I use .reset_index to ensure the indices are in sequential order
load_current_last_cycle = load_current[last_cycle_start:last_cycle_end].reset_index(drop=True)
time_last_cycle = time[last_cycle_start:last_cycle_end].reset_index(drop=True)
time_last_cycle = time_last_cycle - time_last_cycle.iloc[0]
battery_voltage_last_cycle = battery_voltage[last_cycle_start:last_cycle_end].reset_index(drop=True)

# The code below extracts the relevant data for the first cycle.
# I use .reset_index to ensure the indices are in sequential order
load_current_first_cycle = load_current[first_cycle_start:first_cycle_end].reset_index(drop=True)
time_first_cycle = time[first_cycle_start:first_cycle_end].reset_index(drop=True)
time_first_cycle = time_first_cycle - time_first_cycle.iloc[0]
battery_voltage_first_cycle = battery_voltage[first_cycle_start:first_cycle_end].reset_index(drop=True)

# The code below gets the end time and load current for the last cycle
time_last_cycle = time_last_cycle[:-1]
load_current_last_cycle = load_current_last_cycle[:-1]
# Ensure both arrays have the same length for plotting
# Trim the last element to match the length of derivative_load_current
time_first_cycle = time_first_cycle[:-1]
load_current_first_cycle = load_current_first_cycle[:-1]

# The code below resamples the data every 50th point for more drastic difference
resample_factor = 50
load_current_resampled = load_current_first_cycle[::resample_factor].reset_index(drop=True)
first_time_resampled = time_first_cycle[::resample_factor].reset_index(drop=True)
battery_voltage_resampled = battery_voltage_first_cycle[::resample_factor].reset_index(drop=True)

last_load_current_resampled = load_current_last_cycle[::resample_factor].reset_index(drop=True)
last_time_resampled = time_last_cycle[::resample_factor].reset_index(drop=True)
last_battery_voltage_resampled = battery_voltage_last_cycle[::resample_factor].reset_index(drop=True)


# Define the rate_of_change function
def rate_of_change(array1, array2):
    # Initialize empty arrays to hold the rate of change values
    temp_array1 = [0] * (len(array1) - 1)
    temp_array2 = [0] * (len(array2) - 1)

    # Calculate difference for array1
    for i in range(len(array1) - 1):
        temp_array1[i] = array1[i + 1] - array1[i]

    # Calculate difference for array2
    for i in range(len(array2) - 1):
        temp_array2[i] = array2[i + 1] - array2[i]

    # Calculate rate of change
    roc = [x / y if y != 0 else 0 for x, y in zip(temp_array1, temp_array2)]
    return roc

# For first cycle:
# Calculate the derivative of load_current with respect to time
derivative_load_current = rate_of_change(load_current_first_cycle, time_first_cycle)
# Calculate the derivative of battery voltage with respect to time
derivative_battery_voltage = rate_of_change(battery_voltage_first_cycle, time_first_cycle)
# Calculate the derivative of resampled battery voltage with respect to time
resampled_derivative_battery_voltage = rate_of_change(battery_voltage_resampled, first_time_resampled)

# Does the same function as likes 78-83 but for the last cycle
last_derivative_load_current = rate_of_change(load_current_last_cycle, time_last_cycle)
last_derivative_battery_voltage = rate_of_change(battery_voltage_last_cycle, time_last_cycle)
last_resampled_derivative_battery_voltage = rate_of_change(last_battery_voltage_resampled, last_time_resampled)

# Trim last elements to match length of derivative of load current
first_time_resampled = first_time_resampled[:-1]
last_time_resampled = last_time_resampled[:-1]

# Plot the data
fig, ((ax1, ax12), (ax2, ax22)) = plt.subplots(2, 2, figsize=(8, 10))  # 2 rows, 2 column

ax1.plot(time_first_cycle, load_current_first_cycle, label='Current Load (A)', color='blue', marker='*')  # Trim load_current_first_cycle to match time_first_cycle
ax1.set_title("First Cycle: Current Load (A) vs Time (s)")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Current (A)")
ax1.legend()
ax1.grid(True)
ax1.set_ylim(math.floor(load_current_first_cycle.min()), math.ceil(load_current_first_cycle.max()))

ax12.plot(first_time_resampled, resampled_derivative_battery_voltage, label='Battery Voltage Rate of Change (dV/dt)', color='blue', marker='*')  # Trim load_current_first_cycle to match time_first_cycle
ax12.set_title("First Cycle: Battery Voltage Rate of Change (dV/dt) vs Time (s)")
ax12.set_xlabel("Time (s)")
ax12.set_ylabel("Battery Voltage Rate of Change (dV/dt)")
ax12.legend()
ax12.grid(True)
ax12.set_ylim(math.floor(min(resampled_derivative_battery_voltage)), math.ceil(max(resampled_derivative_battery_voltage)) + 1)


ax2.plot(time_last_cycle, load_current_last_cycle, label='Current Load (A)', color='green', marker='*')  # Trim load_current_first_cycle to match time_first_cycle
ax2.set_title("Last Cycle: Current Load (A) vs Time (s)")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Current (A)")
ax2.legend()
ax2.grid(True)
ax2.set_ylim(math.floor(load_current_last_cycle.min()), math.ceil(load_current_last_cycle.max()))


ax22.plot(last_time_resampled, last_resampled_derivative_battery_voltage, label='Battery Voltage Rate of Change (dV/dt)', color='green', marker='*')
ax22.set_title("Last Cycle: Battery Voltage Rate of Change (dV/dt) vs Time (s)")
ax22.set_xlabel("Time (s)")
ax22.set_ylabel("Battery Voltage Rate of Change (dV/dt)")
ax22.legend()
ax22.grid(True)
ax22.set_ylim(math.floor(min(last_resampled_derivative_battery_voltage)), math.ceil(max(last_resampled_derivative_battery_voltage)) + 1)


plt.tight_layout()
plt.show()
