MLE

import numpy as np

# List of averages from the provided data
data = [
    139, 149, 149, 150, 152, 153, 154, 154, 154, 154, 154, 155, 156, 156, 157, 157, 158,
    158, 158, 158, 158, 158, 158, 158, 159, 159, 159, 159, 160, 160, 160, 160, 161, 161,
    162, 162, 162, 163, 163, 163, 163, 164, 164, 164, 164, 164, 164, 164, 165, 165, 165,
    165, 165, 166, 166, 166, 166, 166, 166, 166, 167, 167, 167, 167, 167, 168, 168, 168,
    168, 168, 168, 168, 168, 168, 169, 169, 169, 169, 169, 169, 169, 169, 169, 170, 170,
    170, 170, 170, 170, 170, 170, 170, 171, 171, 171, 171, 171, 171, 171, 171, 171, 172,
    172, 172, 172, 173, 173, 173, 173, 173, 173, 173, 173, 174, 174, 174, 175, 175, 175,
    175, 175, 176, 176, 176, 176, 176, 176, 176, 176, 176, 176, 177, 177, 177, 177, 177,
    177, 178, 178, 178, 178, 178, 178, 178, 178, 178, 179, 179, 179, 179, 179, 179, 179,
    179, 180, 180, 180, 180, 180, 180, 180, 180, 181, 182, 182, 182, 182, 183, 183, 183,
    183, 183, 183, 183, 184, 184, 185, 185, 185, 185, 185, 185, 185, 186, 186, 186, 186,
    186, 186, 186, 186, 186, 186, 187, 188, 188, 188, 188, 188, 188, 188, 188, 188, 189,
    189, 190, 190, 190, 190, 190, 190, 190, 190, 191, 191, 191, 191, 191, 192, 192, 192,
    192, 192, 192, 192, 192, 193, 193, 193, 193, 193, 193, 193, 194, 194, 194, 195, 195,
    195, 196, 196, 196, 196, 197, 197, 198, 198, 198, 198, 198, 198, 199, 200, 200, 200,
    200, 200, 200, 200, 200, 201, 201, 201, 202, 202, 202, 202, 203, 203, 203, 203, 204,
    204, 204, 204, 205, 205, 205, 206, 206, 206, 206, 207, 207, 207, 208, 208, 208, 208,
    208, 208, 208, 208, 209, 209, 209, 209, 209, 210, 210, 211, 211, 211, 213, 213, 213,
    213, 214, 215, 215, 215, 217, 217, 217, 218, 218, 219, 219, 220, 220, 221, 221, 221,
    223, 223, 223, 223, 223, 226, 227, 228, 230, 230, 230, 232, 233, 236, 237, 238, 238,
    239, 240, 241, 242, 243, 243, 243, 273, 279, 279, 281, 286, 286, 322
]

# Convert data to numpy array
data = np.array(data)

# Calculate the MLE for mean and variance
mle_mean = np.mean(data)
mle_variance = np.var(data, ddof=0)

print("MLE Mean:", mle_mean)
print("MLE Variance:", mle_variance)