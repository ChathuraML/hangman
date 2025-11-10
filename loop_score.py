student_score = [150,142,185,171,149,24,68,89,59,199,65,78]

h_score = 0
for score in student_score:
    if score > h_score:
        h_score = score


print(h_score)

total = sum(student_score)

print(total)

sum_of_score = 0
for score in student_score:
    sum_of_score += score

print(f"Total is: {sum_of_score}")
print(f"Max score is: {max(student_score)}")