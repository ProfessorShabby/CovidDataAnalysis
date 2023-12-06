
# Import Python Modules
%pip install seaborn
import pandas as pd 
import numpy as np 
import seaborn as sns
import matplotlib.pyplot as plt 

# Import Covid19 dataset
Corona_Data = pd.read_csv(r'covid19_Confirmed_dataset.csv')

# Delete the useless columns
Corona_Data.drop(['Lat', 'Long'], axis = 1, inplace = True)
Corona_Data.head()

# Aggregating the rows by the country
Corona_Data_Agg = Corona_Data.groupby('Country/Region').sum()
Corona_Data_Agg.head()

# Visualizing data related to a country for example China. Visualization always helps for better understanding of our data.
Corona_Data_Agg.loc['China'].plot()


# Calculating a good measure.We need to find a good measure reperestend as a number, describing the spread of the virus in a country.
Corona_Data_Agg.loc['China'][:3].plot()

# Calculating the first derivative of the curve
Corona_Data_Agg.loc['China'].diff().plot()

# Find the maxmimum infection rate for China
Corona_Data_Agg.loc['China'].diff().max()
Countries_max_infected = []
for c in Countries:
    Countries_max_infected.append(Corona_Data_Agg.loc[c].diff().max())

# Find maximum infection rate for all of the countries.
Countries = list(Corona_Data_Agg.index)
Corona_Data_Agg
Countries_max_infected = []
for c in Countries:
    Countries_max_infected.append(Corona_Data_Agg.loc[c].diff().max())
Corona_Data_Agg['Countries_max_infected'] = Countries_max_infected
Corona_Data_Agg.head()

# Create a new dataframe with only needed column

New_Data = pd.DataFrame(Corona_Data_Agg['Countries_max_infected'])
New_Data.head()

# Importing the WorldHappinessReport.csv dataset
WH_Data = pd.read_csv(r'worldwide_happiness_report.csv')
WH_Data 

​# Drop the useless columns
WH_Data.drop(['Overall rank', 'Score','Generosity','Perceptions of corruption'], axis = 1, inplace = True)
WH_Data

# Changing the indices of the dataframe
WH_Data.set_index(['Country or region'], inplace = True)
WH_Data.head()

# Join two datasets
CoronaData = New_Data.join(WH_Data, how = 'inner')
CoronaData.head()

# Correlation matrix
CoronaData.corr()

# Plotting GDP vs maximum Infection rate
sns.scatterplot(x= "GDP per capita", y = "Countries_max_infected", data = CoronaData)
plt.yscale('log')
sns.regplot(x= CoronaData["GDP per capita"], y = np.log(CoronaData["Countries_max_infected"]), data = CoronaData)

​
# Plotting Social support vs maximum Infection rate
sns.scatterplot(x= "Social support", y = "Countries_max_infected", data = CoronaData)
plt.yscale('log')
sns.regplot(x= CoronaData["Social support"], y = np.log(CoronaData["Countries_max_infected"]), data = CoronaData)

# Plotting Healthy life expectancy vs maximum Infection rate
sns.scatterplot(x= "Healthy life expectancy", y = "Countries_max_infected", data = CoronaData)
plt.yscale('log')

sns.regplot(x= CoronaData["Healthy life expectancy"], y = np.log(CoronaData["Countries_max_infected"]), data = CoronaData)

# Plotting Freedom to make life choices vs maximum Infection rate
sns.scatterplot(x= "Freedom to make life choices", y = "Countries_max_infected", data = CoronaData)
plt.yscale('log')

sns.regplot(x= CoronaData["Freedom to make life choices"], y = np.log(CoronaData["Countries_max_infected"]), data = CoronaData)



