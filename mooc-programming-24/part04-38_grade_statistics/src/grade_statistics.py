# -------------- The help functions : --------------- 
# 1/ function to calculate the point of the exercises :
def  Exercises_point(exercises : int):
    point = exercises // 10 
    return point 

# 2/ function to calculte the sum of the exam note + the point of the exercises :
def Points(exam_note , the_point_of_exercises : int):
    point = exam_note + the_point_of_exercises  
    return point 

# / function to  calculate the grade 0-5 ,result mean the result of the previous function (point):
def  Grade(result , exam_note : int) :
    if exam_note < 10 or result <= 14 :
        return 0
    elif result >= 15 and result <= 17 :
        return 1
    elif result >= 18 and result <= 20 :
        return 2
    elif result >= 21 and result <= 23 :
        return 3
    elif result >= 24 and result <= 27 :
        return 4
    elif result >= 28 and result <= 30 :
        return 5

# / function to calculate the average of points :
def Average_points(points , nbr_student_success):
    result = points / nbr_student_success 
    return result 

# / function to calculate the percentage of passager
def Pass_percentage(point , number_of_student):

    pass
def main():
    students_nbr = 0
    success_student = 0 
    while True:
        line = input("Exam points and exercises completed: ")
        students_nbr += 1
        if line == "":
            break
        parts = line.split()
        exam_points = int(parts[0])
        exercises_complated = int(parts[1]) 
    while True : 
        exrcs_point = Exercises_point(exercises_complated)
        the_point = Points(exam_points, exrcs_point)
        grades = Grade(the_point , exam_points) 
        print("Statistics:")
#15 87
# 10 55
# 11 40
# 4 17

main()    
