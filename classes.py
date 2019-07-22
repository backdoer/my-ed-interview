
## generate sequence of numbers
def sequence():
	x = 1
	while x:
		yield x
		x += 1

SEQUENCE = sequence()

class Student(object):
	def __init__(self, name):
		self.id= next(SEQUENCE)
		self.name = name

class Assignment(object):
	def __init__(self, name):
		self.id = next(SEQUENCE)
		self.name = name

class Submission(object):
	def __init__(self, student_id, assignment_id, grade):
		self.student_id = student_id
		self.assignment_id = assignment_id
		self.grade = grade

class Efficient_Submission(object):
	def __init__(self, student, assignment, grade):
		self.student = student
		self.assignment = assignment
		self.grade = grade