#Anthony Elia - N01515607

import random

#Class constructor for students with an assortment of functions to 
#get values or append and complete student dictionaries
class Student:
    def __init__(self, student_id, student_name, student_age, school_name):
        self.student_id = student_id
        self.student_name = student_name
        self.student_age = student_age
        self.school_name = school_name
        self.profile = {
            "id": self.student_id,
            "Name": self.student_name,
            "Age": self.student_age,
            "School Name": self.school_name,
        }

    def completed_courses(self, **course_and_grade):    
        completed_courses = {"Completed Courses": {}}
        for k,v in course_and_grade.items():
            completed_courses["Completed Courses"][k] = v
        self.profile.update(completed_courses)
        return completed_courses

    def ongoing_courses(self, **course_incomplete):
        incomplete_courses = {"Ongoing Courses": {}}
        for k,v in course_incomplete.items():
            incomplete_courses["Ongoing Courses"][k] = v
        self.profile.update(incomplete_courses)
        return incomplete_courses

    def get_student_profile(self):
        return self.profile
    
    def get_student_id(self):
        return self.student_id

    def get_student_completed(self):
        return self.profile.get("Completed Courses")

    def get_student_ongoing(self):
        return self.profile.get("Ongoing Courses")
    
    def get_student_average(self):
        gradesTotal = 0
        gradesList = list(self.profile["Completed Courses"].values())
        for i in range(len(self.profile["Completed Courses"])):
            gradesTotal += gradesList[i]
        grade_avg = gradesTotal / len(self.profile["Completed Courses"])
        print(f"\n{self.student_name} has a {round(grade_avg)}% average")

    def get_student_course(self, course):
        completed_courses_key_list = list(self.profile["Completed Courses"].keys())
        for i in range (len(self.profile["Completed Courses"])):
            if course.capitalize() == completed_courses_key_list[i]:
                class_name = completed_courses_key_list[i]
                class_grade = self.profile["Completed Courses"][course.capitalize()]
                print(f"\n{self.student_name} has a {class_grade} in {class_name}")
        else:
            print("Invalid course request")

#Declaring an assortment of student objects
#Can easily can add more students when necessary
continuous = True
student_list = []
student_1 = Student(random.randint(1000,1999), "John Doe", random.randint(14,18), "Python Secondary")
student_1.completed_courses(Calculus=(random.randint(0,100)), English=random.randint(0,100), Biology=random.randint(0,100), Algebra=random.randint(0,100))
student_1.ongoing_courses(Physics = "N/A", Chemistry = "N/A", History = "N/A", Art = "N/A")
student_list.append(student_1)
student_2 = Student(random.randint(1000,1999), "Felix Langyel", random.randint(14,18), "Northwood Heights Secondary")
student_2.completed_courses(Calculus=random.randint(0,100), English=random.randint(0,100), Biology=random.randint(0,100), Algebra=random.randint(0,100))
student_2.ongoing_courses(Physics = "N/A", Chemistry = "N/A", History = "N/A", Dance = "N/A")
student_list.append(student_2)
student_3 = Student(random.randint(1000,1999), "Tyler Steinkamp", random.randint(14,18), "Albatross Secondary")
student_3.completed_courses(Calculus=random.randint(0,100), English=random.randint(0,100), Biology=random.randint(0,100), Algebra=random.randint(0,100))
student_3.ongoing_courses(Physics = "N/A", Chemistry = "N/A", History = "N/A", Acting = "N/A")
student_list.append(student_3)
student_4 = Student(random.randint(1000,1999), "Sebastian Fors", random.randint(14,18), "Pearlview Heights Secondary")
student_4.completed_courses(Calculus=random.randint(0,100), English=random.randint(0,100), Biology=random.randint(0,100), Algebra=random.randint(0,100))
student_4.ongoing_courses(Physics = "N/A", Chemistry = "N/A", History = "N/A", Music = "N/A")
student_list.append(student_4)
student_5 = Student(random.randint(1000,1999), "Kai Cenat", random.randint(14,18), "Panther Point Secondary" )
student_5.completed_courses(Calculus=random.randint(0,100), English=random.randint(0,100), Biology=random.randint(0,100), Algebra=random.randint(0,100))
student_5.ongoing_courses(Physics = "N/A", Chemistry = "N/A", History = "N/A", Art = "N/A")
student_list.append(student_5)
student_6 = Student(random.randint(1000,1999), "Anthony Elia", random.randint(14,18), "Panther Point Secondary" )
student_6.completed_courses(Calculus=random.randint(0,100), English=random.randint(0,100), Biology=random.randint(0,100), Algebra=random.randint(0,100))
student_6.ongoing_courses(Physics = "N/A", Chemistry = "N/A", History = "N/A", Art = "N/A")
student_list.append(student_6)

#While loop that will allow users to interact with the stored student information
print(f"Welcome to the Student Database!")
while continuous == True:  
    print(f"\n1. View all students' info")
    print(f"\n2. View all information on a specific student")
    print(f"\n3. View all ongoing grades of specific student")
    print(f"\n4. View all completed grades of specific student")
    print(f"\n5. View average completed grades of student")
    print(f"\n6. View specific grade of specific student")
    user_reply = int(input("\nPlease enter the corresponding option number of your desired action: "))
    
    if user_reply == 1:
        for i in range(len(student_list)):
            print("\n", student_list[i].get_student_profile())
    elif user_reply == 2:
        user_id_choice = int(input("Please enter the student's id: "))
        for i in range(len(student_list)):
            if user_id_choice == student_list[i].get_student_id():
                print(student_list[i].get_student_profile())
        else:
                print("Invalid student id")
    elif user_reply == 3:
        user_id_choice = int(input("Please enter the student's id: "))
        for i in range(len(student_list)):
            if user_id_choice == student_list[i].get_student_id():
                print(student_list[i].get_student_ongoing())
        else:
           print("Invalid student id")
    elif user_reply == 4:
        user_id_choice = int(input("Please enter the student's id: "))
        for i in range(len(student_list)):
            if user_id_choice == student_list[i].get_student_id():
                print(student_list[i].get_student_completed())
        else:
            print("Invalid student id")
    elif user_reply == 5:
        user_id_choice = int(input("Please enter the student's id: "))
        for i in range(len(student_list)):
            if user_id_choice == student_list[i].get_student_id():
                student_list[i].get_student_average()
        else:
            print("Invalid student id")
    elif user_reply == 6:
        id_valid = False
        user_id_choice = int(input("Please enter the student's id: "))
        user_course_choice = input("Please enter the student's course: ")
        for i in range(len(student_list)):
            if user_id_choice == student_list[i].get_student_id():
                student_list[i].get_student_course(user_course_choice)
                id_valid = True
        #Because this else if statement has an added input element needs a flag
        #to distinguish between which part of the request failed
        #the id or the course input.
        if id_valid != True:
            print("Invalid student id")


    else:
        print("\n Invalid request")

    user_query_again = input("\nWould you like to perform another database request? (y/n) ")
    if user_query_again.lower() == "n":
        continuous = False
