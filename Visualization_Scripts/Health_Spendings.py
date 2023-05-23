import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Wczytanie danych z pliku CSV lub innego źródła danych
data = pd.read_csv("Health_Spendings.csv")

# Wybranie interesujących nas krajów
countries = ['POL', 'CHE', 'FRA', 'DEU', 'CZE', 'DNK', 'HRV', 'BEL']

# Filtrowanie danych dla wybranych krajów
filtered_data = data[data["LOCATION"].isin(countries)]

# Przeliczenie wydatków na euro (założenie: dane już są w euro)
euro_data = filtered_data.copy()
euro_data["Value"] = euro_data["Value"]

# Tworzenie tabeli przestawnej (pivot table) dla mapy cieplnej
pivot_data = euro_data.pivot(index="TIME", columns="LOCATION", values="Value")

# Tworzenie mapy cieplnej
sns.heatmap(pivot_data, cmap="YlGnBu")

# Odwrócenie osi Y
plt.gca().invert_yaxis()

# Dodanie tytułu wykresu
plt.title("Healthcare spendings in choosen countries")

# Wyświetlenie wykresu
plt.show()
