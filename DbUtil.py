from sqlalchemy import create_engine,text
from urllib.parse import quote_plus
import pandas as pd

class CreateMySqlInstance:
    def __init__(self):
        # password = quote_plus("MEMON@123") 
        password = "root"
        self.engine = create_engine(f"mysql+pymysql://root:{password}@localhost:3306/sprk_python")

    def getEngine(self):
        return self.engine
    

def read_all_courses():
    mysqlInstance = CreateMySqlInstance()
    engine = mysqlInstance.getEngine()
    query = "select * from course"

    dataframe = pd.read_sql(query,engine)
    return dataframe

def read_course_by_id(course_id):
    mysqlInstance = CreateMySqlInstance()
    engine = mysqlInstance.getEngine()
    query = f"select * from course where cid = {course_id}"

    dataframe = pd.read_sql(query,engine)
    return dataframe

# Insert (Create)
def insert_course(cnm, cdesc, cdur):
    mysqlInstance = CreateMySqlInstance()
    engine = mysqlInstance.getEngine()
    insert_query = text("insert into course(cname,cdescription,cduration) values(:cname,:cdescription,:cduration)")

    with engine.connect() as connection:
        result = connection.execute(insert_query,{"cname":cnm,"cdescription":cdesc,"cduration":cdur})
        connection.commit()
        print(f"Insert successfully, rows inserted are {result.rowcount}")


# Delete
def delete_course(course_id):
    mysqlInstance = CreateMySqlInstance()
    engine = mysqlInstance.getEngine()
    if read_course_by_id(course_id).empty:
        print(f"No Courses Found with id = {course_id}")
    else:
        # Delete Logic
        delete_query = text("delete from course where cid = :cou_id")

        with engine.connect() as connection:
            result = connection.execute(delete_query,{"cou_id":course_id})
            connection.commit()
            print(f"Deleted successfully, rows delete are {result.rowcount}")

# Update
def update_course(course_id,cnm, cdesc, cdur):
    mysqlInstance = CreateMySqlInstance()
    engine = mysqlInstance.getEngine()
  
    # Update Logic
    update_query = text("update course set cname = :course_name, cdescription = :cdescrip, cduration = :cdura  where cid = :cou_id")

    with engine.connect() as connection:
        result = connection.execute(update_query,{"course_name":cnm,"cdescrip":cdesc,"cdura":cdur, "cou_id":course_id})
        connection.commit()
        print(f"Update successfully, rows updated are {result.rowcount}")









