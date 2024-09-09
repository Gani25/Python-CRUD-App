import DbUtil as db


mysqlInstance = db.CreateMySqlInstance()

print(mysqlInstance.getEngine())