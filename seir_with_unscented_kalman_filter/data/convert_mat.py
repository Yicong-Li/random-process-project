import pandas as pd
import scipy.io as sio
import numpy as np

# data preprocessing
data = pd.read_csv('owid-covid-data.csv')
country = 'United States'
country_data = data[data.location == country]
country_data = country_data[(country_data['total_cases'] > 0)]
country_data.head()

country_data['date'] = pd.to_datetime(country_data['date'], format='%Y-%m-%d')

I = country_data['new_cases']
date = country_data['date']
I0 = np.zeros(I.size)
d0 = np.zeros([I.size, 3])
for k in np.arange(I.size):
    I0[k] = I.iloc[k]
    d0[k, :] = [date.iloc[k].month, date.iloc[k].day, date.iloc[k].year]
sio.savemat(country+'.mat', {'I':I0, 'd':d0})
