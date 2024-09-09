from DbUtil import *

isActive = True

while isActive:

    print("Press\n1. Insert\n2. Update\n3. Delete\n4. Read By Id\n5. Read All\n6. Exit\n")
    choice = int(input())
    
    if choice == 1:
        cname = input("Enter course name: ")
        cdescription = input("Enter course description: ")
        cduration = input("Enter course duration: ")
        insert_course(cname, cdescription, cduration)
    
    elif choice == 2:
        cid = input("Enter course_id to be updated: ")

        if read_course_by_id(cid).empty:
            print(f"No Courses Found with id = {cid}")
        else:
            cname = input("Enter course name: ")
            cdescription = input("Enter course description: ")
            cduration = input("Enter course duration: ")

            update_course(cid, cname, cdescription, cduration)        

    elif choice == 3:
        cid = input("Enter course id to be deleted: ")
        delete_course(cid)

    elif choice == 4:
        course_id = int(input("Enter course Id: "))
        dataframe = read_course_by_id(course_id)
        if dataframe.empty:
            print(f"No Courses Found with id = {course_id}")
        else:
            print(dataframe)

    elif choice == 5:
        dataframe = read_all_courses()
        if dataframe.empty:
            print("No Courses Found")
        else:
            print(dataframe)
    elif choice == 6:
        print("Thanks for using CRUD APP")
        isActive = False
    else:
        print("Please select correct choice..")
