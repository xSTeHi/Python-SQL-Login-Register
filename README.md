# Python-SQL-Login-Register
Login &amp; Register in Python 3x, Base program for who want to create a Login &amp; Register System

# HOW TO START ?
It's simple but..
Before ALL you need to donwload mysql.connector...Find some guides on Internet Ex: (https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html)

1) You need to have XAMPP activated and Run Apache and SQL, now go to your Browser and write 127.0.0.1/phpmyadmin

2) Now create a Database (Ex: test), a Table=users with id (AUTO INCREMENT AND PRIMARY KEY, ARE IMPORTANT !!), username (255), password (255)

3) Now check my script and edit the connection: (You will find this script into "modules/funzioni.py"
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="", #Edit if you have it
    database="prova" #Edit with your Database's name
)

4) Check all scripts and edit the SQL strings in case if you have insert different variable names in the Database
5) Ok perfect now Run the program and Enjoy my Login & Register with Python ! :D
