
class Person:

    def __init__(self, first_name: str, last_name: str) -> None:
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Student(Person):

    def __init__(self, first_name: str, last_name: str, degree_course: str = None) -> None:
        super().__init__(first_name, last_name)
        self.degree_course = degree_course

    def __str__(self) -> str:
        return super().__str__() + (" is not registered to any course" if self.degree_course is None else f" is registered to {self.degree_course}")

def main() -> None:
    data = {}
    data['first_name'] = input("Insert first name: ")
    data['last_name'] = input("Insert last name: ")
    is_student = ""
    while is_student not in ['y', 'n']:
        if is_student == "":
            is_student = input("Are you a student? (y/n)")
        else:
            is_student = input('Please type "y" or "n": ')
        if is_student == 'y':
            data['degree_course'] = input("Please insert your degree course: ")
            object = Student(**data)
        elif is_student == 'n':
            object = Person(**data)
    print(object)

if __name__ == '__main__':
    main()

