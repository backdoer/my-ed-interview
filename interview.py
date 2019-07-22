
import random
import time
from classes import Student, Assignment, Submission, Efficient_Submission
from functions import linear_search, create_dict_from_list

students = []
assignments = []
submissions = []
POSSIBLE_GRADES = ['A', 'B', 'C', 'D', 'E']

## generate data
for x in range(100):
	students.append(Student('Student %s' % x))

for x in range(20):
	assignments.append(Assignment('Assignment %s' % x))

for student in students:
	for assignment in assignments:
		submissions.append(Submission(student.id, assignment.id, random.choice(POSSIBLE_GRADES)))


with open('times.txt', 'w') as f:

	## Given option for generating report
	start = time.time()
	for assignment in assignments:
	    # f.write(assignment.name)
	    for student in students:
	        for submission in submissions:
	            if submission.student_id != student.id:
	                continue
	            if submission.assignment_id != assignment.id:
	                continue
	            # f.write(student.name, submission.grade)
	end = time.time()
	f.write('Given Option: %s seconds \n' % (end - start))


	## Option 2: first sort the list by assignments and only do a linear search on assignments when a new assignment comes along
	start = time.time()
	submissions.sort(key=lambda submission: submission.assignment_id)
	prev_assignment_id = None

	for submission in submissions:
		if submission.assignment_id != prev_assignment_id:
			current_assignment= linear_search(assignments, 'id', submission.assignment_id)
			# f.write(current_assignment.name)

		student = linear_search(students, 'id', submission.student_id)
		# f.write(student.name, submission.grade)

		prev_assignment_id = submission.assignment_id

	end = time.time()

	f.write('First Option: %s seconds \n' % (end - start))


	## Option 3: first convert arrays to dictionaries (with id and name) for quick look up, sort submissions by assignments, then only loop through the submissions
	start = time.time()

	## I'm including the list-to-dictionary conversions in the time because the problem assumes we start with an array
	students_dict = create_dict_from_list(students)
	assignments_dict = create_dict_from_list(assignments)
	prev_assignment_id = None

	submissions.sort(key=lambda submission: submission.assignment_id)
	for submission in submissions:
		if submission.assignment_id != prev_assignment_id:
			current_assignment = assignments_dict[submission.assignment_id]
			# f.write(current_assignment)	

		student = students_dict[submission.student_id]
		# f.write(student, submission.grade)

		prev_assignment_id = submission.assignment_id

	end = time.time()	
	f.write('Second Option: %s seconds \n' % (end - start))


	## Option 4: Have a submission class that holds objects instad of just ids

	efficient_submissions = []
	for student in students:
		for assignment in assignments:
			efficient_submissions.append(Efficient_Submission(student, assignment, random.choice(POSSIBLE_GRADES)))

	start = time.time()
	efficient_submissions.sort(key=lambda e_submission: e_submission.assignment.name)

	prev_assignment_id = None
	for e_submission in efficient_submissions:
		if e_submission.assignment.id != prev_assignment_id:
			current_assignment = e_submission.assignment
			# f.write(current_assignment.name)			
		student = e_submission.student
		prev_assignment_id = e_submission.assignment.id
		# f.write(student.name, e_submission.grade)

	end = time.time()	
	f.write('Third Option: %s seconds \n' % (end - start))


	## Option 5: Use this if you want to display each student and each assignment regardless of whether or not the stuent submitted anything (or in other words, a 0)
	## This loops through each student and assignment and displays them and then queries the submissions to find one; if one is not found, a 0 is displayed
	## I would say that in this case, it would be smart to put the submissions in a dictionary (or this would be easy if it were in a database in a relation table) with the key being a combination of the assignment and student ids

	start = time.time()

	## I'm including the list-to-dictionary conversion in the time because the problem assumes we start with an array
	submissions_dict = {}
	for submission in submissions:
		submissions_dict['%s-%s' % (str(submission.assignment_id), str(submission.student_id))] = submission.grade

	for assignment in assignments:
		# f.write(assignment.name)
		for student in students:
			try:
				grade = submissions_dict['%s-%s' % (assignment.id, student.id)]
			except:
				grade = 0	
			# f.write(student.name, grade)

	end = time.time()	
	f.write('Fourth Option: %s seconds \n' % (end - start))

