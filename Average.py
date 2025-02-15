jeremiahsgrades = [47, 59, 93, 70, 89]
torrancesgrades = [94, 72, 91, 67, 100]
marysgrades = [ 92, 44, 94, 83, 79]
bethsgrades = [77, 32, 27, 100, 92]
johnsgrades = [100, 100, 100, 99, 82]
larrysgrades = [44, 89, 77, 66, 100]
megansgrades = [50, 85, 75, 95, 95]


def average(grades):
    return sum(grades) / len(grades)

def lettergrade(numbergrade):
    if numbergrade >= 90:
        return "A"
    elif numbergrade >= 80:
        return "B"
    elif numbergrade >= 70:
        return "C"
    elif numbergrade >= 60:
        return "D"
    else:
        return "F"

grade = average(jeremiahsgrades)
letter_grade = lettergrade(grade)
print("Jeremiah's grade is a", average(jeremiahsgrades), letter_grade)

grade = average(torrancesgrades)
letter_grade =lettergrade(grade)
print("Torrance's grade is a", average(torrancesgrades), letter_grade)

grade = average(marysgrades)
letter_grade =lettergrade(grade)
print("Mary's grade is a", average(marysgrades), letter_grade)

grade = average(bethsgrades)
letter_grade =lettergrade(grade)
print("Beth's grade is a", average(bethsgrades), letter_grade)

grade = average(johnsgrades)
letter_grade =lettergrade(grade)
print("John's grade is a", average(johnsgrades), letter_grade)

grade = average(larrysgrades)
letter_grade=lettergrade(grade)
print("Larry's grade is a", average(larrysgrades), letter_grade)

grade = average(megansgrades)
letter_grade=lettergrade(grade)
print("Megan's grade is a", average(megansgrades), letter_grade)

