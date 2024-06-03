# Final Code Checking if an ICE Vehicle would generate less emissions in within 10,000 trials 

import numpy as np
import scipy.stats as stats

# Given data
battery_manufacture_mean = 12617.5
battery_manufacture_var = 0  # Assuming constant, no variance given

annual_ev_mean = 1384.178
annual_ev_var = 641.47

ice_manufacture_mean = 763
ice_manufacture_var = 0  # Assuming constant, no variance given

annual_ice_mean = 6095.08
annual_ice_var = 0  # Assuming constant, no variance given

# Simulation parameters
num_simulations = 100000
years = 3.31

# Simulate EV total emissions
ev_annual_emissions = np.random.normal(annual_ev_mean, np.sqrt(annual_ev_var), num_simulations)
ev_total_emissions = battery_manufacture_mean + ev_annual_emissions * years

# Simulate ICE total emissions
ice_total_emissions = ice_manufacture_mean + annual_ice_mean * years  # Assuming constant annual emissions

# Calculate the probability that EV emissions are less than ICE emissions
probability_ev_less_than_ice = np.mean(ev_total_emissions < ice_total_emissions)

probability_ev_less_than_ice
