import sqlite3
import mysql.connector


def db():
    # connection = mysql.connector.connect(host="localhost", user="root", password="root@4321",
    #                                      database="gujranwalaemporium")
    # cursor = connection.cursor(prepared=True)

    connection = sqlite3.connect(database=r'marketing.db')
    cursor = connection.cursor()

    # client TABLE
    cursor.execute("CREATE TABLE IF NOT EXISTS client(client_cnic INTEGER PRIMARY KEY NOT NULL,client_name text,"
                "client_contact text,client_address text,kin_cnic INTEGER,kin_name text,kin_contact text,kin_address text)")
    connection.commit()

    # project TABLE
    cursor.execute("CREATE TABLE IF NOT EXISTS project(projectID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,projectTitle text,projectDescription text,"
        "projectCost INTEGER)")
    connection.commit()

    # property TABLE
    cursor.execute("CREATE TABLE IF NOT EXISTS property(propertyID INTEGER PRIMARY KEY NOT NULL,client_cnic INTEGER,projectID INTEGER, propertySize text,propertyPrice INTEGER,downPayment INTEGER,"
                "totalInstallments text,pricePerInstallment INTEGER,discount INTEGER,status text,propertyLocation text,propertyDescription text,installmentPlan text,possession INTEGER,"
                "FOREIGN KEY (client_cnic) REFERENCES client(client_cnic),FOREIGN KEY (projectID) REFERENCES project(projectID))")
    connection.commit()

    # bill TABLE
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS bill(billID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,propertyID INTEGER ,receiveDate date,dueDate date,installementNo INTEGER,installmentAmount INTEGER,"
        "receiveAmount INTEGER,paymentType INTEGER,balance INTEGER,status text)")
    connection.commit()

    # expense TABLE
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS expense(expenseID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,expenseDate date,expenseType text,expenseDescription text,"
        "expenseAmount INTEGER)")
    connection.commit()

    # # Drop Table
    # cursor.execute("DROP TABLE bill")
    # connection.commit()

db()