Usage:
	1. Go to the T-Square Assignment>Download All
	2. Minimally download at least Grade File, Feedback Comments, Student Submission Attachments
	3. Use the grading scheme below
	4. Provide the following arguments to the script:
		--dir The directory of the archive (unzipped downloaded from T-Square)
		--points The total point value of the homework
Grading Scheme:
	In the comments.txt of each student:
		Any string of the form "-digits" will be counted as a deduction
		E.X. -5 will incur a 5 point deduction
		Additionally the special string "-All" will cause all points to be deducted

Function:
	This script will read through the comments of each folder identifying point deductions, calculating total score then adding the final score to the grades.csv file.
