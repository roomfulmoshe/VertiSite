import pandas as pd

# Load the giant file
df = pd.read_csv("output/Universal_Demand_Map.csv")
print(f"Original rows: {len(df)}")

# Filter: Remove rows with zero or negligible demand
# Adjust the threshold (e.g., 0.001) based on your normalized data range
df_web = df[df["universal_demand"] > 0.001].copy()

# Optional: Round floats to 4 decimal places to save text space
df_web["universal_demand"] = df_web["universal_demand"].round(4)
df_web["distance_km"] = df_web["distance_km"].round(2)

print(f"Optimized rows: {len(df_web)}")
df_web.to_csv("output/Universal_Demand_Map_Web.csv", index=False)