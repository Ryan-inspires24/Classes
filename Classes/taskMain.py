from Task import *
task = Task('Finish OOP Exercises')
task.mark_done()
print(f'{task.description} : {task.get_status()}')