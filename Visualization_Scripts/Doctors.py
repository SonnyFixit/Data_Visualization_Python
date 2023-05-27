import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych z pliku CSV lub innego źródła danych
data = pd.read_csv("Medical_Data\Doctors.csv")

# Wybranie interesujących nas krajów
countries = ["HRC", "DNK"]

# Tworzenie wykresów punktowych
fig, axes = plt.subplots(nrows=len(countries), ncols=1, figsize=(10, 6*len(countries)), sharex=True)

# Iteracja po krajach
for i, country in enumerate(countries):
    # Filtrowanie danych dla konkretnego kraju
    filtered_data = data[data["LOCATION"] == country]
    
    # Przygotowanie danych do wykresu
    years = filtered_data["TIME"].tolist()
    values = filtered_data["Value"].tolist()
    
    # Tworzenie wykresu punktowego
    axes[i].scatter(years, values)
    
    # Dodanie nazwy kraju jako tytułu wykresu
    axes[i].set_title(country)
    axes[i].set_ylabel("Liczba lekarzy na 1000 obywateli")
    
# Dodanie wspólnego tytułu dla wszystkich wykresów
fig.suptitle("Liczba lekarzy na 1000 obywateli - Wykresy punktowe", fontsize=16)

# Ustawienie oznaczeń osi X jako lata dla ostatniego wiersza wykresów
axes[-1].set_xticks(years)

# Dostosowanie układu wykresów
plt.tight_layout()

# Wyświetlenie wykresów
plt.show()
