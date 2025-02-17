class Student:

    def __init__(self, name: str, marks: list[float]):
        self.name = name
        self._marks = marks

    def _avg(self):
        return sum(self._marks) / len(self._marks)

    def get_report(self):
        print(f"Student {self.name} has {self._avg()} average mark")

std_1 = Student('Jofry', [1,2,3])
std_2 = Student('Jeimy', [10,20,30])
std_3 = Student('Cersi', [100,200,300])

std_1.get_report()
std_2.get_report()
std_3.get_report()
        