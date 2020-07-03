import pandas as pd
from datetime import datetime, timedelta
from scipy import integrate, optimize
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
import warnings
warnings.filterwarnings('ignore')

# data preprocessing
data = pd.read_csv('owid-covid-data.csv')
country = 'Turkey'
country_data = data[data.location == country]
country_data = country_data[(country_data['total_cases'] > 0)]
country_data.head()

# population
pop_dict = {'United Kingdom': 67900000, 'Italy': 60500000, 'China': 1400050000, 'Turkey': 83200000}
pop = pop_dict[country]

# time interval
t_interval = np.arange(len(country_data))

# daily new cases
daily_new_cases = country_data['new_cases'].values

# SEIR model: susceptible, exposed, infected, recovered
# initial values
I0 = daily_new_cases[0]
E0 = 5 * I0
S0 = pop - I0 - E0
R0 = 0

print(I0)
print(E0)
print(S0)
