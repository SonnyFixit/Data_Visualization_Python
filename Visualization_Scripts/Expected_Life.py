import pandas as pd
import matplotlib.pyplot as plt

# Specify the path to your CSV file
csv_file = 'Expected_Life_Length.csv'

# Wczytanie danych z pliku CSV lub innego źródła danych
data = pd.read_csv(csv_file)


countries = ['POL', 'CHE', 'FRA', 'DEU', 'CZE', 'DNK', 'HRV', 'BEL']

# Wybranie interesujących nas krajów
filtered_data = data[data['LOCATION'].isin(countries)]


filtered_data['TIME'] = filtered_data['TIME'].astype(int)


fig, ax = plt.subplots()

# Iteracja po krajach
for country in countries:
    country_data = filtered_data[filtered_data['LOCATION'] == country]
    ax.plot(country_data['TIME'], country_data['Value'], label=country)

  
    country_name = country_data['LOCATION'].unique()[0]

  
    last_value = country_data['Value'].iloc[-1]
    ax.annotate(f"{country_name}: {last_value}", (country_data['TIME'].iloc[-1], last_value))

# Dostosowanie układu wykresów
ax.set_xlabel('Year')
ax.set_ylabel('Life Expectancy')
ax.set_title('Life Expectancy by Country and Year')


# Wyświetlenie wykresów
plt.show()



