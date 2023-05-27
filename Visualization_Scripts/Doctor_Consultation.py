import pandas as pd
import matplotlib.pyplot as plt

# Wczytanie danych z pliku CSV lub innego źródła danych
data = pd.read_csv("Medical_Data\Doctor_Consultations.csv")

# Wybranie interesującego nas wskaźnika
indicator = "DOCCONSULT"

# Filtrowanie danych dla wybranego wskaźnika i krajów
countries = ['POL', 'CHE', 'FRA', 'DEU', 'CZE', 'DNK', 'BEL']
filtered_data = data[(data["LOCATION"].isin(countries)) & (data["INDICATOR"] == indicator) & (data["TIME"].between(2010, 2020))]

# Przygotowanie danych do wykresu
years = filtered_data["TIME"].unique()
countries_data = []

for country in countries:
    country_data = []
    for year in years:
        value = filtered_data[(filtered_data["LOCATION"] == country) & (filtered_data["TIME"] == year)]["Value"]
        if value.empty:
            country_data.append(0)
        else:
            country_data.append(value.item())
    countries_data.append(country_data)

# Tworzenie wykresu liniowego
fig, ax = plt.subplots()

# Wykres liniowy dla każdego kraju
for i in range(len(countries)):
    ax.plot(years, countries_data[i], label=countries[i])

    # Dodanie etykiety z nazwą kraju dla każdej linii
    last_value = countries_data[i][-1]
    ax.annotate(countries[i], xy=(years[-1], last_value), xytext=(5, 0), textcoords='offset points')

# Dodanie legendy
ax.legend()

# Dodanie tytułu wykresu
plt.title("Liczba konsultacji lekarskich na mieszkańca")

# Dodanie opisów osi
plt.xlabel("Lata")
plt.ylabel("Liczba konsultacji")

# Wyświetlenie wykresu
plt.show()
