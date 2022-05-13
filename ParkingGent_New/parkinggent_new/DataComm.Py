from calendar import day_abbr
from datetime import datetime
import pyodbc
import csv

# can you get database information inside of development studio?

""" 
Get the data from the Database
 """
def ReadData():
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQLExpress;DATABASE=Gent_Test;Trusted_Connection=yes;')

    cursor = connection.cursor()
    cursor.execute("SELECT * from Gent_Test.dbo.RawData")
    #while 1:
    #    row = cursor.fetchone()
    #    if not row:
    #        break
    #    print(row.data)
    DataDict = []
    ColumnNames = [column[0] for column in cursor.description]
    Data = cursor.fetchall()
    for data in Data:
        DataDict.append(dict(zip(ColumnNames,data)))
    PlaceData(DataDict)
    return


""" 
Place Data From the database
 """

def InsertData(data: dict):
    date_format = "%Y-%m-%dT%H:%M:%S%z" 
    if dict(data).get("lastupdate") is not None:
        date=datetime.strptime(dict(data).get("lastupdate"), date_format)
    else:
       date=datetime.now()
    
    connection = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=.\SQLExpress;DATABASE=Gent_Test;Trusted_Connection=yes;')

    cursor = connection.cursor()
    cursor.execute("Insert into Gent_test.dbo.RawData (Name,UpdateTime,TotalCapacity,Capacity,Occupation,Isopen) values (?,?,?,?,?,?)",(dict(data).get("name"),datetime.now(),dict(data).get("totalcapacity"),dict(data).get("availablecapacity"),dict(data).get("occupation"),dict(data).get("isopennow")))
    connection.commit()
    return

#create method to export data from sql to file
def PlaceData(data:dict):
    fieldnames = ["Id","Name","UpdateTime","TotalCapacity","Capacity","Occupation","IsOpen"]
    #find mode that does not give extra enter after each line
    with open("C:\\ProgramData\\data.csv","w") as f:
        writer = csv.DictWriter(f,fieldnames=fieldnames)

        writer.writeheader()
        writer.writerows(data)