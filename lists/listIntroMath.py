students = ['Brooke', 'Coen', 'Blas', 'George']
exam1 = [85, 90, 80, 50]
exam2 = [ 95, 100, 100, 96]

print(students)
# print out Blas' name and his grade for exam 1
print(students[2], exam1[2])


students = ['Brooke', 'Coen', 'Blas', 'George']
exam1 = [85, 90, 80, 50]
exam2 = [ 95, 100, 100, 96]
print(students[2], exam1[2])


days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
print(days[1], "and", days[5])

nums = [2, 4, 6, 9, 10, 12, 14, 16, 18, 20]
print(nums[-1])

students = ['Brooke', 'Coen', 'Blas', 'George']
print('students[0]:', students[0])
print('students[1]:', students[1])
print('students[-1]:', students[-1])
print('students[-2]:', students[-2])
print('students[1:3]:', students[1:3])
print('students[:2]:', students[:2])
print('students[1:]:', students[1:])

students = ['Brooke', 'Coen', 'Blas', 'George']
print(students[2], students[-2])

exam1 = [85, 90, 80, 50]
print(exam1[2:])

students = ['Brooke', 'Coen', 'Blas', 'George']
for s in students:
    print( s, 'is a student')


students = ['Brooke', 'Coen', 'Blas', 'George']
exam1 = [85, 90, 80, 50]
exam2 = [ 95, 100, 100, 96]

for i, s in enumerate(students):
    avg = (exam1[i] + exam2[i]) / 2
    print( i, s, avg)


students = ['Brooke', 'Coen', 'Blas', 'George']
exam1 = [85, 90, 80, 50]
exam2 = [ 95, 100, 100, 96]
print( f'{"index":^6} {"student":10} {"Exam 1":7} {"Exam 2":7} {"Avg":5}')

for i, s in enumerate(students):
    avg = (exam1[i] + exam2[i]) / 2
    print( f'{i:^6d} {s:10} {exam1[i]:^7} {exam2[i]:^7} {avg:.2f}')




students = ['Brooke', 'Coen', 'Blas', 'George']
exam1 = [85, 90, 80, 50]
exam2 = [ 95, 100, 100, 96]
print( 'index, student, Exam 1, Exam 2, Average')

for i, s in enumerate(students):
    avg = (exam1[i] + exam2[i]) / 2
    print( i, s, exam1[i], exam2[i], avg)


nums = []
for i in range(20):
    n = i * 3
    nums.append(n)
print(nums)

nums = []
for i in range(10):
    n = i * 5 + 5
    nums.append(n)
print(nums)


n4s = []
n7s = []
for i in range(10):
    n4s.append(i*4+4)
    n7s.append(i*7+7)

print()

nprods = []
for i in range(5):
    n = n4s[i] * n7s[i]
    nprods.append(n)
print("multiples of 4:", n4s)
print("multiples of 7:",  n7s)
print("products:", nprods)
