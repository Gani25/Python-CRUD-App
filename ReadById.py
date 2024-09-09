from DbUtil import read_course_by_id

course_id = int(input("Enter course Id: "))
dataframe = read_course_by_id(course_id)
if dataframe.empty:
    print(f"No Courses Found with id = {course_id}")
else:
    print(dataframe)