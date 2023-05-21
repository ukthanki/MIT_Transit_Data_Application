import mysql.connector

def insertMBTARecord(mbtaList):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="MyNewPass",
    database="MBTAdb"
    )

    mycursor = mydb.cursor()
    #complete the following line to add all the fields from the table
    sql = "insert into mbta_buses ( id, longitude, latitude, bearing, current_stop_sequence, direction_id, speed, updated_at) values (%s, %s, %s, %s, %s, %s, %s, %s)"
    for mbtaDict in mbtaList:
        #complete the following line to add all the fields from the table
        val = (mbtaDict['id'], mbtaDict['longitude'], mbtaDict['latitude'], mbtaDict['bearing'], mbtaDict['current_stop_sequence'], mbtaDict['direction_id'], mbtaDict['speed'], mbtaDict['updated_at'])
        mycursor.execute(sql, val)

    mydb.commit()