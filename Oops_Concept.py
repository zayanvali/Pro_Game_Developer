# def greet():
#     print("Hello, how are you")
#     print("My name is Jarvis")
#     name = input("May I know your name: ")
#     print("Hello {}, nice to meet you!".format(name))

# #Calling the function in order to execute
# greet()

class student():
    name = ""
    age = 12
    school_class = "Year 8"
    color = "Red"
    teacher = "Mr Williams"

    # constructor class
    def __init__(self):
        print("Making a new student")

    def change_details(self):
        print("Please enter your age: ")
        self.age = int(input())
        print("Please enter the name of the student: ")
        self.name = input()

    #Function to show the details
    def show_details(self):
        print("The details of students are: ")
        print(self.name)
        print(self.age)
        print(self.school_class)
        print(self.color)
        print(self.teacher_name)

John = student.show_details(self)
David = student.show_details()
