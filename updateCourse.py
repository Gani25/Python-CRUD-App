from DbUtil import update_course, read_course_by_id

cid = input("Enter course_id to be updated: ")

if read_course_by_id(cid).empty:
    print(f"No Courses Found with id = {cid}")
else:
    cname = input("Enter course name: ")
    cdescription = input("Enter course description: ")
    cduration = input("Enter course duration: ")

    update_course(cid, cname, cdescription, cduration)