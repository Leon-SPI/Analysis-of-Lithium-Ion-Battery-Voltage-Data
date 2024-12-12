import pandas as pd
import matplotlib.pyplot as plt
from scipy import signal as sg
import math
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



## The function below finds the indices for the start and end of a discharge cycle.
## Discharge data is indicated by a mode of -1, changing = 1, rest = 0.
def cycle_index_start_finish(file_data):
    discharge_start = -1
    discharge_end = -1
    for index, mode in enumerate(file_data):
        if mode == -1:
            discharge_start = index + 4
            break

    for index in range(discharge_start, len(file_data)):
        if file_data[index] != -1:
            discharge_end = index
            break

    if discharge_end == -1:
        discharge_end = len(file_data)
    return discharge_start, discharge_end

first_discharge_start, first_discharge_end = cycle_index_start_finish(mode_data)

##for data in mode_data[start_index:]:

## The loop below uses range to transverse backwards within the data set.
def reverse_cycle_index_start_finish(file_data):
    discharge_start_last = -1
    discharge_end_last = -1
    for i in range(len(file_data) - 1, -1, -1):  # Traverse backward
        if file_data[i] == -1:
            discharge_end_last = i
            break

    for i in range(discharge_end_last, -1, -1):  # Find the start of the discharge
        if file_data[i] != -1:
            discharge_start_last = i + 1 + 4
            break

    if discharge_start_last == -1:  # Handle edge case where the discharge starts from index 0
        discharge_start_last = 0
    return discharge_start_last, discharge_end_last
last_discharge_start, last_discharge_end = reverse_cycle_index_start_finish(mode_data)

time_first_discharge_plot = time[first_discharge_start:first_discharge_end]
time_last_discharge_plot = time[last_discharge_start:last_discharge_end]
battery_voltage_first_plot = battery_voltage[first_discharge_start:first_discharge_end]
battery_voltage_last_plot = battery_voltage[last_discharge_start:last_discharge_end]
load_current_first_plot = load_current[first_discharge_start:first_discharge_end]
load_current_second_plot = load_current[last_discharge_start:last_discharge_end]

time_first_discharge_plot = time_first_discharge_plot - time_first_discharge_plot.iloc[0]
time_last_discharge_plot = time_last_discharge_plot - time_last_discharge_plot.iloc[0]


fig, ((ax1, ax3), (ax2, ax4)) = plt.subplots(2, 2, figsize=(8, 10))  # 2 rows, 2 column

# Plot on the first subplot
ax1.plot(time_first_discharge_plot, battery_voltage_first_plot, label='Battery Voltage (V)', color='blue', marker='*')
ax1.set_title("First Cycle: Battery Voltage Discharge vs Time")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Battery Voltage (V)")
ax1.legend()
ax1.grid(True)
ax1.set_ylim(math.floor(battery_voltage_first_plot.min()), math.ceil(battery_voltage_first_plot.max()))

# Plot on the second subplot
ax2.plot(time_last_discharge_plot, battery_voltage_last_plot, label='Battery Voltage (V)', color='green', marker='*')
ax2.set_title("Last Cycle: Battery Voltage Discharge vs Time")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Battery Voltage (V)")
ax2.legend()
ax2.grid(True)
ax2.set_ylim(math.floor(battery_voltage_last_plot.min()), math.ceil(battery_voltage_last_plot.max()))


ax3.plot(time_first_discharge_plot, load_current_first_plot, label='Load Current (A)', color='blue', marker='*')
ax3.set_title("First Cycle: Load Current vs Time")
ax3.set_xlabel("Time (s)")
ax3.set_ylabel("Load Current (A)")
ax3.legend()
ax3.grid(True)
ax3.set_ylim(math.floor(load_current_first_plot.min()), math.ceil(load_current_first_plot.max()))

ax4.plot(time_last_discharge_plot, load_current_second_plot, label='Load Current (A)', color='green', marker='*')
ax4.set_title("Last Cycle: Load Current vs Time")
ax4.set_xlabel("Time (s)")
ax4.set_ylabel("Load Current (A)")
ax4.legend()
ax4.grid(True)
ax4.set_ylim(math.floor(load_current_second_plot.min()), math.ceil(load_current_second_plot.max()))

# Adjust layout
plt.tight_layout()

# Show the plots
plt.show()

### End of question 1 ###

def peaks_height(signal):
    max_height = 0
    for val in signal:
        if val > max_height:
            max_height = val
    return max_height * 0.5

peak_distance = 100

voltage_peaks = sg.find_peaks(battery_voltage, height = peaks_height(battery_voltage), distance = peak_distance)


# Calculate the index range for the adjusted time window
start_index = int(len(time) * 0.1)  # Start at 10% of total data
end_index = int(len(time) * 0.15)    # Include only 10% of total data

# Slice the data to include only the 10% time window
time = time[start_index:end_index].reset_index(drop=True)
battery_voltage = battery_voltage[start_index:end_index].reset_index(drop=True)
load_voltage = load_voltage[start_index:end_index].reset_index(drop=True)
load_current = load_current[start_index:end_index].reset_index(drop=True)

# Create the plots
plt.figure(figsize=(14, 6))

# Plot 1: Time vs Battery Voltage
plt.subplot(1, 2, 1)
plt.plot(time, battery_voltage, label="Battery Voltage (V)", color='blue')
plt.xlabel("Time (s)")
plt.ylabel("Battery Voltage (V)")
plt.title("Time vs Battery Voltage")
plt.legend()

# Plot 2: Battery Voltage vs Load Voltage and Load Current
plt.subplot(1, 2, 2)
plt.plot(battery_voltage, load_voltage, label="Load Voltage (V)", color='green')
plt.plot(battery_voltage, load_current, label="Load Current (A)", color='red')
plt.xlabel("Battery Voltage (V)")
plt.ylabel("Load Voltage / Load Current")
plt.title("Battery Voltage vs Load Voltage and Current")
plt.legend()

plt.tight_layout()
plt.show()