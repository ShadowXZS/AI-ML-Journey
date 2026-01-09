#Pause Challenge Replicating Max Function with For Loop
student_scores = [150, 142, 185, 120, 171, 184 , 149 , 24 , 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]

max_score = student_scores[0]
# This is a Better Way to Do it than in the Course 
for score in student_scores :
    if max_score <= score :
        max_score = score 
print(max_score)

# Minimum Function in the Same Way 

min_score = student_scores[0]

for score in student_scores:
    if min_score >= score :
        min_score = score 
print(min_score)