import pandas as pd
import matplotlib.pyplot as plt

# Incarca fisierul CSV
file_path = "data.csv"
data = pd.read_csv(file_path)

data = data.dropna()# Elimina liniile cu valori lipsa


coloane_de_interes = ["Durata", "Puls"]
data_filtrata = data[coloane_de_interes]

# Ploteaza toate valorile
def plot_all_values(data):
    plt.figure(figsize=(10, 6))
    
    plt.plot(data["Durata"], label="Durata", marker='o')
    plt.plot(data["Puls"], label="Puls", marker='x')
    plt.plot(data["MaxPuls"], label="MaxPuls", marker='x')
    plt.plot(data["Calorii"], label="Calorii", marker='^')
    
    plt.title("Grafic pentru toate coloanele")
    plt.xlabel("Index")
    plt.ylabel("Valori")
    plt.legend()
    plt.grid()
    plt.show()

# Ploteaza primele 6 valori
def plot_first_6_values(data):
    subset = data.head(6)
    plt.figure(figsize=(10, 6))
    
    plt.plot(subset["Durata"], label="Durata", marker='o')
    plt.plot(subset["Puls"], label="Puls", marker='x')
    plt.plot(subset["MaxPuls"], label="MaxPuls", marker='x')
    plt.plot(subset["Calorii"], label="Calorii", marker='^')
    
    plt.title("Primele 6 valori pentru toate coloanele")
    plt.xlabel("Index")
    plt.ylabel("Valori")
    plt.legend()
    plt.grid()
    plt.show()

# Ploteaza ultimele 12 valori
def plot_last_12_values(data):
    subset = data.tail(12)
    plt.figure(figsize=(10, 6))
    plt.plot(subset["Durata"], label="Durata", marker='o')
    plt.plot(subset["Puls"], label="Puls", marker='x')
    plt.title("Ultimele 12 valori pentru Durata si Puls")
    plt.xlabel("Index")
    plt.ylabel("Valori")
    plt.legend()
    plt.grid()
    plt.show()

# Apeleaza functiile de plotare
plot_all_values(data)
plot_first_6_values(data)
plot_last_12_values(data_filtrata)


#EXPLICATII

"""

file_path = "data.csv": Stochează calea către fișierul CSV în variabila file_path. Dacă fișierul se află într-un alt folder, trebuie să schimbi calea.
data = pd.read_csv(file_path): Încarcă datele din fișierul CSV în variabila data sub formă de DataFrame, care este o structură de date oferită de pandas.
data.dropna(): Elimină rândurile care conțin valori lipsă (NaN) din DataFrame.
coloane_de_interes = ["Durata", "Puls"]: Specifică coloanele pe care vrem să le analizăm: "Durata" și "Puls".
data_filtrata = data[coloane_de_interes]: Creează un subset de date care conține doar coloanele menționate mai sus, pentru a simplifica analiza
def plot_all_values(data):: Definește o funcție pentru a plota toate valorile din dataset.
plt.figure(figsize=(10, 6)): Creează o figură cu dimensiunea specificată (10 x 6 inch).
plt.plot(data["Durata"], label="Durata", marker='o'): Plotează valorile din coloana Durata cu un marker în formă de cerc ('o').
plt.plot(data["Puls"], label="Puls", marker='x'): Plotează valorile din coloana Puls cu un marker în formă de X ('x').
plt.title("Toate valorile pentru Durata si Puls"): Setează titlul graficului.
plt.xlabel("Index"): Adaugă o etichetă pe axa X (în acest caz, indexul rândurilor din dataset).
plt.ylabel("Valori"): Adaugă o etichetă pe axa Y.
plt.legend(): Adaugă o legendă pentru a indica ce reprezintă fiecare linie din grafic.
plt.grid(): Adaugă o grilă pe fundalul graficului.
plt.show(): Afișează graficul.
subset = data.head(6): Selectează primele 6 rânduri din dataset folosind metoda head(6).
subset = data.tail(12): Selectează ultimele 12 rânduri din dataset folosind metoda tail(12).
plot_all_values(data_filtrata): Apelează funcția pentru a plota toate valorile din subsetul filtrat de date.
plot_first_6_values(data_filtrata): Apelează funcția pentru a plota primele 6 valori.
plot_last_12_values(data_filtrata): Apelează funcția pentru a plota ultimele 12 valori.

"""
