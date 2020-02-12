import mysql.connector, hashlib
from modules import menu

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="prova"
)

mycursor = mydb.cursor()
lstcursor = mydb.cursor()

def login():
	nome = str(input("Inserisci il tuo nome: "))
	passwd = hashlib.md5(str(input("Inserisci la password: ")).encode('utf-8')).hexdigest()

	sql = "SELECT username, password FROM users WHERE username = '{}' AND password = '{}'".format(nome, passwd)
	mycursor.execute(sql)
	myresults = mycursor.fetchall()

	#CONTINUA PROGRAMMA
	if myresults:
		print("Accesso eseguito ! Benvenuto", nome)
		exit() #TOGLIERE L'EXIT PER CONTINUARE IL PROGRAMMA !!!!
	#FINE DEL PROGRAMMA
	else:
		print("Username o Password incorretti, se non hai ancora creato un account vai su Registrati oppure nella lista per vedere se il tuo account esiste!")
		menu.continua()

def register():
	nome = str(input("Inserisci il tuo nome: "))
	password = hashlib.md5(str(input("Inserisci la password: ")).encode('utf-8')).hexdigest()

	sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
	utenti = (nome, password)

	mycursor.execute(sql, utenti)

	mydb.commit()

def list():
	lstcursor.execute("SELECT id, username FROM users")
	myresult = lstcursor.fetchall()
	for x in myresult:
  		print(x)
