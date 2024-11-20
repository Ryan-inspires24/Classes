class Student:
    def __init__(self, name):
     self.name= name
     self.grades = []   
     
    def add_grade(self,grade):
        self.grades.append(grade)
        return f'{grade} has been added to the list of grades'
            
    def average_grades(self):
        if len(self.grades) == 0 :
            return 'No grade was Calculated'
        else:
            avg = sum(self.grades)/len(self.grades)
            return f'The average of {self.name} is {avg}.'