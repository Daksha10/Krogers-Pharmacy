import pandas as pd
import numpy as np
import openpyxl

# Define inventory policy parameters
s = 120  # Reorder point
S = 180  # Order-up-to level
Q = 60   # Order quantity
package_size = 10  # Package size
lead_time = 2  # Lead time

# Define Excel file name
file_path = "/Users/daksha/Documents/GitHub/Inventory-System/Matlab Package/Inventory1.xlsx";

# Load data from Excel file
df = pd.read_excel(file_path)

# Get daily demand input from the user
daily_demand = float(input("Enter the daily demand: "))

def simulate(df, s, S, Q, daily_demand):
    # Convert 'Inv Pos' column to numeric type
    df['Inv Pos'] = pd.to_numeric(df['Inv Pos'])

    df['Order qty'] = np.where((df['Inv Pos'] < s) & (df['Week Days'].str.match('Fri|Mon|Wed')),
                               np.ceil((S - df['Inv Pos']) / package_size) * package_size, 0)
    df['Qty rec'] = df['Order qty'].shift(lead_time)
    df['End Inv'] = df['Begg.Inv'] + df['Qty rec'] - daily_demand
    df['Shortage'] = np.where(df['End Inv'] < 0, np.abs(df['End Inv']), 0)
    df['Total Cost'] = df['Order qty'] + df['End Inv'] + df['Shortage']
    cost = df['Total Cost'].sum()

    return df, cost

def local_search(df, s, S, Q, daily_demand):
    # Initial total cost before optimization
    initial_cost = df['Total Cost'].sum()

    # Fixed Q
    while True:
        df, cost_s_S = simulate(df, s, S, Q, daily_demand)

        # Increase reorder point
        s_prime = s + 1
        S_prime = s_prime + Q
        df_s_prime_S_prime, cost_s_prime_S_prime = simulate(df, s_prime, S_prime, Q, daily_demand)

        if cost_s_prime_S_prime < cost_s_S:
            s = s_prime
            S = S_prime
        else:
            # Decrease reorder point
            s_prime = s - 1
            S_prime = s_prime + Q
            df_s_prime_S_prime, cost_s_prime_S_prime = simulate(df, s_prime, S_prime, Q, daily_demand)

            if cost_s_prime_S_prime < cost_s_S:
                s = s_prime
                S = S_prime
            else:
                break

    # Final total cost after optimization
    final_cost = df['Total Cost'].sum()

    # Determine effectiveness of the policy
    if initial_cost != 0:
        effectiveness = (initial_cost - final_cost) / initial_cost * 100
    else:
        effectiveness = 0

    return s, S, Q, effectiveness

# Run local search algorithm
s, S, Q, effectiveness = local_search(df, s, S, Q, daily_demand)

# Print optimized parameters and effectiveness
print("Optimized parameters:")
print(f"Reorder point (s): {s}")
print(f"Order-up-to level (S): {S}")
print(f"Order quantity (Q): {Q}")
print(f"Effectiveness of the policy: {effectiveness:.2f}%")

# Update inventory data in DataFrame
df['Order qty'] = np.where((df['Inv Pos'] < s) & (df['Week Days'].str.match('Fri|Mon|Wed')),
                           np.ceil((S - df['Inv Pos']) / package_size) * package_size, 0)
df['Qty rec'] = df['Order qty'].shift(lead_time)

# Update the next row with consecutive days' demand based on the previous day's demand
for i in range(len(df) - 1):
    df.loc[i + 1, 'Begg.Inv'] = df.loc[i, 'End Inv']
    df.loc[i + 1, 'Week Days'] = 'Next Day'  # Update with the appropriate day

# Save the updated data to the Excel file
df.to_excel(file_path, index=False)