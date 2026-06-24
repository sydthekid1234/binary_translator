def make_greeting():
    message="Hello from the inside of the function"
    print(message)
#make_greeting()
#line 6 wont work because the variable only works inside of part of the code, not the whole code
#print(message)

school_name = "Lincoln High"
def print_school():
    print(school_name)
def change_school():
    school_name="Jefferson High"
    print(school_name)
#print_school()
#change_school()
#the school name variable stayed the same because it was changed locally not globally so it only counted for part of it
#print(school_name)

def add_score_fixed(current_total, points):
    return current_total + points
#this is better then using the global keyword because it is easier to debug and wont crash because of the computer not understanding it

student_data = {
    "Katherine": [85, 90, 92],
    "Amy": [78, 82, 80],
    "Dakota": [95, 98, 96]
}
def get_student_average(student_name, scores_dict):
    """Calculates and returns the average score for a specific student."""
    if student_name in scores_dict:
        scores = scores_dict[student_name]
        if len(scores) > 0:
            return sum(scores) / len(scores)
    return 0.0

def get_class_average(scores_dict):
    """Calculates the overall average across all students."""
    total_score = 0
    total_subjects = 0
    for scores in scores_dict.values():
        total_score += sum(scores)
        total_subjects += len(scores)
    if total_subjects > 0:
        return total_score / total_subjects
    return 0.0

def get_top_student(scores_dict):
    """Returns the name of the student with the highest average."""
    top_student = None
    highest_avg = -1.0
    
    for student in scores_dict:
        avg = get_student_average(student, scores_dict)
        if avg > highest_avg:
            highest_avg = avg
            top_student = student
    return top_student
print("Individual Student Averages")
for student in student_data:
    avg = get_student_average(student, student_data)
    print(f"{student}'s Average: {avg:.2f}")
class_avg = get_class_average(student_data)
print(f"\nOverall Class Average: {class_avg:.2f}")
top_student = get_top_student(student_data)
print(f"\nTop Student: {top_student}")