def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print (f"Error. Can't divide {a} by zero.")
        return None
#print(safe_divide(7, 3))

def strict_grade(score):
    if score >= 90:
        return ("A")
    elif score > 79 and score < 90:
        return ("B")
    elif score > 69 and score < 80:
        return ("C")
    elif score > 59 and score < 70:
        return ("D")
    elif score < 60:
        return ("F")
#print(strict_grade(90))
def lenient_grade(score):
    if score >= 85:
        return ("A")
    elif score > 74 and score < 85:
        return ("B")
    elif score > 64 and score < 75:
        return ("C")
    elif score > 54 and score < 65:
        return ("D")
    elif score < 55:
        return ("F")
#print(lenient_grade(55))
def grade_report(scores, grading_func):
    if not scores:
        return "The scores list is empty. No report to generate."
    if not isinstance(scores, list):
        return "Please provide a valid list of scores."
    for score in scores:
        if not isinstance(score, (int, float)):
            print(f"all scores must be numbers.")
            continue
    report = {}
    for score in scores:
        report[score] = grading_func(score)
    return report
test_scores = [95,84,73,62,51]
print(grade_report([85, 90, 72], strict_grade))