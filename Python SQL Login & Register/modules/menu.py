from subprocess import call
import os
from modules import funzioni

def continua():
    aff = "Si"
    neg = "No"
    print("Vuoi continuare ? Scrivi Si o No")
    scelta = input()
    if scelta == aff:
        menu()
    if scelta == neg:
        print("Grazie e alla prossima !")
        exit()
    if scelta != neg:
        print("ERRORE Devi scrivere Si o No")
        continua()
    if scelta != aff:
        print("ERRORE Devi scrivere Si o No")
        continua()

def menu():
    print("Scegli un'opzione per poter accedere:\n\t1) Registrati\n\t2) Login\n\t3) List\n\t4) Esci")
    choice = input()

    if choice == "1":
        print("Registrati")
        funzioni.register()
        continua()

    if choice == "2":
        print("Login")
        funzioni.login()

    if choice == "3":
        print("Lista")
        funzioni.list()
        continua()

    if choice == "4":
        print("Uscendo...")
        exit()

# define clear function
def clear():
# check and make call for specific operating system
	input()
	_ = call('clear' if os.name =='posix' else 'cls')