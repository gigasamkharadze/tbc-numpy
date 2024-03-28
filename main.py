import numpy as np

FIRST_NAMES = ['ვენერა', 'თინა', 'თეა', 'სოსო', 'მირანდა', 'ჟენია', 'ტატიანა',
               'ედუარდ', 'კლარა', 'სიმონ', 'ანზორ', 'სოფია', 'სოსო', 'ნელი',
               'ბონდო', 'ედუარდ', 'სონია', 'არჩილ', 'მარიამ', 'სოფია', 'ემა',
               'იზოლდა', 'ომარ', 'ტატიანა', 'ვიქტორ', 'კარინე', 'გუგული', 'კახა',
               'როზა', 'რუსუდან', 'სიმონ', 'ნელი', 'ბადრი', 'მადონა', 'ირინე',
               'მინდია', 'ნათია', 'გულნარა', 'კახა', 'ელზა', 'როინ', 'ნაირა', 'ლიანა',
               'ნინელი', 'მაყვალა', 'რეზო', 'ჟუჟუნა', 'ზინა', 'გოჩა', 'მურმან'
               ]

LAST_NAMES = ['ქუთათელაძე', 'მეგრელიშვილი', 'სალუქვაძე', 'ხარაიშვილი', 'შელია',
              'კევლიშვილი', 'ბუჩუკური', 'ტყებუჩავა', 'მიქაბერიძე', 'ურუშაძე',
              'ძიძიგური', 'გოგუაძე', 'ანთაძე', 'ვალიევა', 'როგავა', 'ნაკაშიძე', 'ღურწკაია',
              'გვაზავა', 'გვასალია', 'ზარანდია', 'სხირტლაძე', 'ბერაძე', 'ხვიჩია', 'ბასილაშვილი',
              'კაკაბაძე', 'მერებაშვილი', 'ნოზაძე', 'ხარაბაძე', 'მუსაევა', 'მამულაშვილი', 'ელიზბარაშვილი',
              'მამულაშვილი', 'ჯოჯუა', 'გულუა', 'ხალვაში', 'ხარატიშვილი', 'დუმბაძე', 'ბერიანიძე',
              'ჯოხაძე', 'სამხარაძე', 'ლიპარტელიანი', 'იობიძე', 'გაბაიძე', 'ხარაბაძე', 'ინასარიძე',
              'ბერაძე', 'შენგელია', 'ქობალია', 'მიქავა', 'რევაზიშვილი'
              ]

SUBJECTS = ['ქართული', 'მათემატიკა', 'ინგლისური', 'ბიოლოგია', 'ისტორია']


def generate_random_table(number_of_entries, min_grade_value, max_grade_value):
    """
    Generates a table with random grades for students
    """
    global FIRST_NAMES, LAST_NAMES, SUBJECTS

    shape = (number_of_entries, 5)
    grades = np.random.randint(min_grade_value, max_grade_value, shape)
    names = np.random.choice(FIRST_NAMES, shape[0])
    last_names = np.random.choice(LAST_NAMES, shape[0])
    full_names = np.array([f'{name} {last_name}' for name, last_name in zip(names, last_names)])

    table = np.column_stack((full_names, grades))
    table = np.vstack((['სრული სახელი'] + SUBJECTS, table))

    return table


def get_student_with_max_average_grade(table):
    """
    Returns the full name of the student with the highest average grade
    """
    grades = table[1:, 1:].astype(int)
    averages = np.mean(grades, axis=1)
    max_average_index = np.argmax(averages)

    return table[max_average_index + 1, 0]


def get_students_with_min_and_max_grades_in_math(table):
    """
    Returns the full names of 2 students with the lowest and highest grades in math
    """
    grades = table[1:, 1:].astype(int)
    math_grades = grades[:, 1]
    min_math_index = np.argmin(math_grades)
    max_math_index = np.argmax(math_grades)

    min_math_student = table[min_math_index + 1, 0]
    max_math_student = table[max_math_index + 1, 0]

    return max_math_student, min_math_student


def get_students_with_grade_more_than_average_in_english(table):
    """
    Returns the full names of students who have grades in English higher than the average grade
    """
    grades = table[1:, 1:].astype(int)
    english_grades = grades[:, 2]
    average_english_grade = np.mean(english_grades)

    students_with_grade_more_than_average = table[1:, 0][english_grades > average_english_grade]

    return students_with_grade_more_than_average


grade_table = generate_random_table(100, 1, 100)
print(grade_table)

student_with_max_average_grade = get_student_with_max_average_grade(grade_table)
print(f'Student with the highest average grade: {student_with_max_average_grade}')

max_student_math, min_student_math = get_students_with_min_and_max_grades_in_math(grade_table)
print(f'Student with the highest grade in math: {max_student_math}')
print(f'Student with the lowest grade in math: {min_student_math}')

students_better_than_average = get_students_with_grade_more_than_average_in_english(grade_table)
print('Students with grade in English higher than the average grade:')
for student in students_better_than_average:
    print(student)
