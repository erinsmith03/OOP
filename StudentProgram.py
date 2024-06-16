import StudentClass as sc

idd=1001
name='John'
dob='02/28/2001'
classification='junior'


student1=sc.Student(idd,name,dob,classification)

student1.calc_age()

student1.register(f'Student age is: {student1.get_age()}')
print(f'The student can register between {student1.get_registration()}')

