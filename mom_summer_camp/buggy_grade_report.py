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
    report = {}
    for score in scores:
        report[score] = grading_func(score)
    return report
test_scores = [95,84,73,62,51]
print(grade_report(test_scores, strict_grade))