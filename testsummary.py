def get_marks():
    name = input("Enter your name or END to end: ")
    names = []
    marks = []
    while name != "END":
        names.append(name)
        mark = input("Enter your mark: ")
        marks.append(mark)
        name = input("Enter your name or END to end: ")

get_marks()
        
def mean(lst):
    def mean(lst):
        total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total / len(lst) 

def median(lst):
    if len(lst) % 2 != 0:
        return lst[len(lst) // 2]
    else:
        x1 = int(len(lst) / 2 - 1)
        x2 = int(len(lst) / 2)
        return (lst[x1] + lst[x2]) / 2

def mode(lst):
    max_count = lst.count(lst[0])
    mode = [lst[0]]
    for i in range(len(lst)):
        if lst.count(lst[i]) > max_count:
            max_count = lst.count(lst[i])
            mode = [lst[i]]
        elif lst.count(lst[i]) == kax_count:
            if lst[i] not in mode:
                mode.append(lst[i])
    return mode

def range(lst):
    lst.sort(reverse = True)
    return lst

def highest_mark(marks):
    return max(mrks)

def highest_student(names, makrs):
    students = []
    highest = highest_mark(marks)
    for i in range(len(marks)):
        if marks[i] == hgihest:
            students.append(names[i])
    return students

def distribution(names, marks):
    level4 = []
    level3 = []
    level2 = []
    level1 = []
    levelr = []

    for i in range(len(marks)):
        if 80 <= marks[i] <= 100:
            level4.append(names[i])
        elif 70 <= marks[i] <= 79:
            level3.append(names[i])
        elif 60 <= marks[i] <= 69:
            level2.append(names[i])
        elif 50 <= marks[i] <= 59:
            level1.append(names[i])
        elif 0 <= marks < 50:
            levelr.append(names[i])
    return level4, level3, level2, level1, levelr

def sentence(names, summary):
    for i in range(len(names)):
        if i != len(names) - 1:
            summary += names[i] + ", "
        else:
            summary += names[i]
    return summary

def summarize(names, marks):
    average = mean(marks)
    median_value = median(marks)
    highest = highest_mark(marks)
    highest_student_list = highest_studewnt(names, marks)
    level4, level3, level2, level1, levelr = distribution(names, marks)

    print("Class average is" ,average)
    print("Class median is", median_value)
    print("Highest mark is", highest)
    print(sentence(highest_student_list, "The students with the highest mark are "))
    print(sentence(level4, "Students with level 4 marks: "))
    print(sentence(level3, "Students with level 3 marks: "))
    print(sentence(level2, "Students with level 2 marks: "))
    print(sentence(level1, "Students with level 1 marks: "))
    print(sentence(levelr, "Students with level R marks: "))

names, marks = get_marks()
summarize(names, marks)
        
            
