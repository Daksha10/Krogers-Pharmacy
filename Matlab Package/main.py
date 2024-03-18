import pandas as pd
import numpy as np

# Define inventory policy parameters
s = 120  # Reorder point
S = 180  # Order-up-to level
Q = 60  # Order quantity
package_size = 10  # Package size
lead_time = 2  # Lead time

# Define Excel file name
file_name = 'Inventory1.xlsx'

# Load data from Excel file
df = pd.read_excel(file_name)
print(df.columns)

def simulate(df, s, S, Q):
    # Convert Inv Pos column to numeric type
    df['Inv Pos'] = pd.to_numeric(df['Inv Pos'])

    df['Order qty'] = np.where((df['Inv Pos'] < s) & (df['Week Days'].str.match('Fri|Mon|Wed')), np.ceil((S - df['Inv Pos']) / package_size) * package_size, 0)
    df['Qty rec'] = df['Order qty'].shift(lead_time)
    df['End Inv'] = df['Begg.Inv'] + df['Qty rec'] - df['Demand']
    df['Shortage'] = np.where(df['End Inv'] < 0, np.abs(df['End Inv']), 0)
    df['Total Cost'] = df['Order qty'] + df['End Inv'] + df['Shortage']
    cost = df['Total Cost'].sum()

    return df, cost

def local_search(df, s, S, Q):
    # Fixed Q
    while True:
        df, cost_s_S = simulate(df, s, S, Q)

        # Increase reorder point
        s_prime = s + 1
        S_prime = s_prime + Q
        df_s_prime_S_prime, cost_s_prime_S_prime = simulate(df, s_prime, S_prime, Q)

        if cost_s_prime_S_prime < cost_s_S:
            s = s_prime
            S = S_prime
        else:
            # Decrease reorder point
            s_prime = s - 1
            S_prime = s_prime + Q
            df_s_prime_S_prime, cost_s_prime_S_prime = simulate(df, s_prime, S_prime, Q)

            if cost_s_prime_S_prime < cost_s_S:
                s = s_prime
                S = S_prime
            else:
                break

    # Variable Q
    while True:
        r = min(df['End Inv'].sum(), df['Shortage'].sum())

        # Increase order-up-to level
        S_prime = S + r
        Q_prime = S_prime - s
        df_s_S_prime, cost_s_S_prime = simulate(df, s, S_prime, Q_prime)

        if cost_s_S_prime < cost_s_S:
            S = S_prime
            Q = Q_prime
        else:
            # Decrease order-up-to level
            s_prime = s - r
            Q_prime = S - s_prime
            df_s_prime_S_prime, cost_s_prime_S_prime = simulate(df, s_prime, S, Q_prime)

            if cost_s_prime_S_prime < cost_s_S:
                s = s_prime
                Q = Q_prime
            else:
                break

    return s, S, Q

# Run local search algorithm
s, S, Q = local_search(df, s, S, Q)

# Update inventory data in Excel file
df['Order qty'] = np.where((df['Inv Pos'] < s) & (df['Day'].str.match('Fri|Mon|Wed')), np.ceil((S - df['Inv Pos']) / package_size) * package_size, 0)
df['Qty rec'] = df['Order qty'].shift(lead_time)
df.to_excel(file_name, index=False)