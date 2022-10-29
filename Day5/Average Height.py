# Get average height without using len() and sum() functions.

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
#print(student_heights)

st_h = 0
total = 0
count = 0
for st_h in student_heights:
    count +=1
    total += st_h
print(round(total/count))