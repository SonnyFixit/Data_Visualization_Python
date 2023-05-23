import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych z pliku CSV lub innego źródła danych
data = pd.read_csv("Computed_Tomography.csv")

# Wybranie interesujących nas krajów
countries = ["CZE", "DNK", "FRA", "DEU"]

# Wybranie wskaźnika
indicator = "CTEXAM"

# Tworzenie wykresów słupkowych
fig, axes = plt.subplots(nrows=1, ncols=len(countries), figsize=(12, 4))

# Iteracja po krajach
for i, country in enumerate(countries):
    # Filtrowanie danych dla konkretnego kraju i wskaźnika
    filtered_data = data[(data["LOCATION"] == country) & (data["INDICATOR"] == indicator)]
    
    # Przygotowanie danych do wykresu
    years = filtered_data["TIME"].tolist()
    values = filtered_data["Value"].tolist()
    
    # Tworzenie wykresu słupkowego
    axes[i].bar(years, values)
    
    # Dodanie nazwy kraju jako tytułu wykresu
    axes[i].set_title(country)
    
    # Dodanie opisów osi
    axes[i].set_xlabel("Lata")
    axes[i].set_ylabel("Liczba badań na 1000 mieszkańców")

# Dostosowanie układu wykresów
plt.tight_layout()

# Dodanie ogólnego tytułu dla wszystkich wykresów
fig.suptitle("Liczba badań tomografii komputerowej na 1000 mieszkańców w różnych krajach")

# Wyświetlenie wykresów
plt.show()
