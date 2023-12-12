import json
class FileHandler:
    def __init__(self, history_file, warehouse_file):
        self.waehouse_file=warehouse_file
        self.history_file=history_file
        self.waehouse_file, self.saldo=self.read_data_from_warehouse_file()
        self.history_file=self.read_data_from_history_file()

    def read_data_from_warehouse_file (self):
        with open(self.waehouse_file) as file:
            warehouse_temporary=json.loads(file.read())
            return warehouse_temporary.get("magazyn"), warehouse_temporary.get("saldo")

    def read_data_from_history_file(self):
        with open(self.history_file) as file:
            history_data=json.loads(file.read())
            return history_data

    def write_data_to_warehouse_file(self):
        with open(self.warehouse_file, mode="w+") as file:
            file.write(json.dumps({"saldo":self.saldo,"magazyn":self.warehouse}))

    def change_saldo (self, new_saldo):
        self.saldo+=int(new_saldo)

    def add_new_input_to_history (self, new_imput):
        self.history.append(new_imput)

    def write_data_to_history_file (self):
        with open (self.history_file, mode ="w+") as file:
            file.write(json.dumps(self.history))

    def wtire_data_to_histry_file_without_update(self,new_imput):
        with open (self.history_file,mode="a") as file:
            file.write(json.dumps(f",{new_imput}"))

file_handler=FileHandler(history_file="history.json", warehouse_file="warehose.json")

print(file_handler)



print("Witaj w programie Accountant.")

koniec_programu = False
history=[]
magazyn=[]
saldo = int(input("Podaj poczatkowe saldo: "))

while not koniec_programu:
    wybor_akcji = input("Podaj rodzaj akcji ktora chcesz wykonac: ")

    if wybor_akcji == "saldo":
        zmiana_na_koncie_firmy_wyrażona_w_groszach = int(input("Podaj zmiane na koncie firmy wyzrazona w groszach: "))
        komentarz_do_zmiany = input("Podaj komentarz do zmiany: ")

        history[zmiana_na_koncie_firmy_wyrażona_w_groszach] = komentarz_do_zmiany

        print(history)

    elif wybor_akcji == "zakup":

        nazwa_produktu = input("Podaj identyfikator produktu:")

        cena_jednostkowa = int(input("Podaj cene jednostkowa produktu:"))

        liczba_sztuk = int(input("Podaj liczbe sztuk produktu:"))

        saldo -= cena_jednostkowa*liczba_sztuk
        if saldo < 0:
            print("Jestes na minusie.")
            break

        if nazwa_produktu in magazyn:
            magazyn[nazwa_produktu] += liczba_sztuk
        else:
            magazyn[nazwa_produktu] = liczba_sztuk
        print(magazyn)

    elif wybor_akcji == "sprzedaz":
        nazwa_produktu = input("Podaj identyfikator produktu:")

        cena_jednostkowa = int(input("Podaj cene jednostkowa produktu:"))

        liczba_sztuk = int(input("Podaj liczbe sztuk produktu:"))

        if nazwa_produktu in magazyn and magazyn[nazwa_produktu] >= liczba_sztuk:
            saldo += cena_jednostkowa * liczba_sztuk
            magazyn[nazwa_produktu] -= liczba_sztuk
            print(magazyn)

        else:
            print("Nie masz wystarczajacej ilosci produktu.")
            break

    elif wybor_akcji == "magazyn":
            print(f' Stany magazynowe: {magazyn}')
            break

    elif wybor_akcji == "konto":
        print(f'Stan konta po wszystkich akcjach: {saldo}')
        break

    elif wybor_akcji == "przegad":
        pass

    else:
        koniec_programu = True
        print("Error. Nie ma takiej akcji. Program Accountant zakonczyl dzialanie.")


