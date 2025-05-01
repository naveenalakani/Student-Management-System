class StudentClass:
    classes = {}

    def __init__(self, name):
        self.name = name
        self.studentList = []
        StudentClass.classes[name] = self


class Student:
    student_Dictionary = {}
    school_name = 'XYZ'

    def __init__(self):
        self.roll_no = input('\nEnter the Student Roll Number: ')
        self.name = input('Enter the Student Name: ')
        self.phone_number = input('Enter the Student Phone Number: ')
        self.address = input('Enter the Student Address: ')
        student_class = input('Enter the Student Class [Ex: 1,2,3,...10]: ')

        if student_class in StudentClass.classes:
            StudentClass.classes[student_class].studentList.append(self)
        else:
            new_class = StudentClass(student_class)
            new_class.studentList.append(self)

        self.student_class = StudentClass.classes[student_class]
        Student.student_Dictionary[self.roll_no] = self
        print('\nStudent Added Successfully')
        self.getStudent()

    def getStudent(self):
        print('\n--- Student Details ---')
        print('Roll Number:', self.roll_no)
        print('Name:', self.name)
        print('Phone Number:', self.phone_number)
        print('Address:', self.address)
        print('School Name:', Student.school_name)
        print('Class:', self.student_class.name)

    def updateStudent(self):
        print('\nSelect option to update student details:')
        print('1) Change Name')
        print('2) Change Phone Number')
        print('3) Change Address')
        print('4) Change Class')
        option = input('Enter option: ')

        if option == '1':
            self.name = input('Enter the new name: ')
            print('Name updated successfully.')
        elif option == '2':
            self.phone_number = input('Enter the new phone number: ')
            print('Phone number updated successfully.')
        elif option == '3':
            self.address = input('Enter the new address: ')
            print('Address updated successfully.')
        elif option == '4':
            new_class = input('Enter the new class name: ')
            self.student_class.studentList.remove(self)
            if new_class in StudentClass.classes:
                self.student_class = StudentClass.classes[new_class]
            else:
                self.student_class = StudentClass(new_class)
            self.student_class.studentList.append(self)
            print('Class changed successfully.')
        else:
            print('Invalid option.')
        self.getStudent()

    @classmethod
    def updateSchoolName(cls, new_name):
        cls.school_name = new_name

    @classmethod
    def getTotalCount(cls):
        return len(cls.student_Dictionary)


def main():
    while True:
        print(f'\n___ Welcome to {Student.school_name} School ___')
        print('1) Get Student Details')
        print('2) Add New Student')
        print('3) Remove Student')
        print('4) Update Student')
        print('5) Update School Name')
        print('6) Get Student Count')
        print('7) Get All Students')
        print('8) Get Students from Particular Class')
        print('9) Exit')

        option = input('Choose an option: ')

        if option == '1':
            roll_no = input('Enter Roll Number: ')
            student = Student.student_Dictionary.get(roll_no)
            if student:
                student.getStudent()
            else:
                print('Student not found.')
        elif option == '2':
            Student()
        elif option == '3':
            roll_no = input('Enter Roll Number to delete: ')
            student = Student.student_Dictionary.pop(roll_no, None)
            if student:
                student.student_class.studentList.remove(student)
                print('Student deleted successfully.')
            else:
                print('No student found.')
        elif option == '4':
            roll_no = input('Enter Roll Number to update: ')
            student = Student.student_Dictionary.get(roll_no)
            if student:
                student.updateStudent()
            else:
                print('Student not found.')
        elif option == '5':
            new_name = input('Enter new school name: ')
            Student.updateSchoolName(new_name)
            print('School name updated.')
        elif option == '6':
            print('Total students:', Student.getTotalCount())
        elif option == '7':
            if Student.student_Dictionary:
                for idx, student in enumerate(Student.student_Dictionary.values(), start=1):
                    print(f'\nStudent {idx}:')
                    student.getStudent()
            else:
                print('No students found.')
        elif option == '8':
            class_name = input('Enter the class name to get students: ')
            student_class = StudentClass.classes.get(class_name)
            if student_class and student_class.studentList:
                print(f'\nStudents in class {class_name}:')
                for student in student_class.studentList:
                    student.getStudent()
            else:
                print(f'No students found in class {class_name}.')
        elif option == '9':
            print('Goodbye!')
            break
        else:
            print('Invalid option.')


if __name__ == '__main__':
    option = 'y'
    while option.lower() == 'y':
        main()
        option = input('\nDo you want to Continue [y/n]?: ')

