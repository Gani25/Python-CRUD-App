from DbUtil import insert_course

cname = input("Enter course name: ")
cdescription = input("Enter course description: ")
cduration = input("Enter course duration: ")

insert_course(cname, cdescription, cduration)