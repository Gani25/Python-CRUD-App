from DbUtil import read_all_courses

dataframe = read_all_courses()
if dataframe.empty:
    print("No Courses Found")
else:
    print(dataframe)