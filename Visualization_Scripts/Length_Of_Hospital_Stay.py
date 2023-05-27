import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych z pliku CSV lub innego źródła danych
data = pd.read_csv("Medical_Data\Length_Of_Hospital_Stay.csv")

# Wybranie interesujących nas krajów
countries = ["FRA", "BEL", "CZE"]

# Tworzenie wykresów liniowych
fig, axes = plt.subplots(nrows=len(countries), ncols=1, figsize=(8, 6))

# Iteracja po krajach
for i, country in enumerate(countries):
    # Filtrowanie danych dla konkretnego kraju
    country_data = data[data["LOCATION"] == country]
    
    # Przygotowanie danych do wykresu
    years = country_data["TIME"].tolist()
    values = country_data["Value"].tolist()
    
    # Tworzenie wykresu liniowego
    axes[i].plot(years, values, marker='o')
    
    # Dodanie nazwy kraju jako tytułu wykresu
    axes[i].set_title(country)
    
    # Dodanie opisów osi
    axes[i].set_xlabel("Rok")
    axes[i].set_ylabel("Wartość")
    
# Ustawienie ogólnego tytułu dla wszystkich wykresów
fig.suptitle("Średnia ilość dni pobytu w szpitalu")

# Dostosowanie układu wykresów
plt.tight_layout()

# Wyświetlenie wykresów
plt.show()
