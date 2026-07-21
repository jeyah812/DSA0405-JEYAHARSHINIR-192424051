import numpy as np

house_data = np.loadtxt(
    "data/House_data.csv",
    delimiter=",",
    skiprows=1,
    usecols=(1,2,3,4,5)
)

houses_more_than_4 = house_data[house_data[:,0] > 4]

average_price = np.mean(houses_more_than_4[:,4])

print("Average Sale Price:", average_price)