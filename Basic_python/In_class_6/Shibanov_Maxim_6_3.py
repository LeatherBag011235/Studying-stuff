class Student:

    school_name = "ICEF"

    def __init__(self, name: str):
        self.name = name
        self.marks = {}
        self.add_marks()

    def add_marks(self):
        while True:
            add_more = input(f"Add more subjects for {self.name}? \nYes/No")
            if add_more == "Yes":
                pass
            elif add_more == "No":
                break
            else: 
                print("Please enter 'Yes' or 'No' to continue or quit")   
                continue

            subject = input(f'Enter the subject name for {self.name}')
            while True:
                try:
                    mark = float(input(f'Enter the mark for {self.name} on {subject}'))
                    if 0 <= mark <= 100:
                        break
                    else:
                        print("Please enter positive value between 0 and 100")

                except ValueError:
                    print("Pleas enter float value for a mark")

            self.marks[subject] = mark
                
    def get_avg(self):
        avg_grade = self.marks.values().sum() / len(self.marks.values())
        print(f"The average grade for {self.name} is {avg_grade}")

    def display_marks(self):
        for subject, mark in self.marks.items():
            print(f"{self.name} got {mark} for {subject} at {Student.school_name}")

std_1 = Student("Bob")
std_2 = Student("Bil")
std_3 = Student("Sam")

Student.school_name = "HSE ICEF"

std_1.display_marks()



                 