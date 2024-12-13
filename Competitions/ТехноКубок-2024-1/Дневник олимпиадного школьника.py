class Student:
    def __init__(self, identifier, name, group_attendance, solved_problems):
        self.identifier = identifier
        self.name = name
        self.group_attendance = group_attendance
        self.solved_problems = solved_problems
        self.grade = None

    def calculate_grade(self, limits):
        s3, s4, s5 = 0, 0, 0
        total_solved = 0

        for day, group in enumerate(self.group_attendance):
            l3, l4, l5 = limits[group - 1][day]
            s3 += l3
            s4 += l4
            s5 += l5
            total_solved += sum(self.solved_problems[day])

        if total_solved >= s5:
            self.grade = 5
        elif total_solved >= s4:
            self.grade = 4
        elif total_solved >= s3:
            self.grade = 3
        else:
            self.grade = 2


def process_input():
    n, g, d = map(int, input().split())
    students = {}
    group_limits = [[] for _ in range(g)]
    for _ in range(n):
        data = input().split()
        student_id = int(data[0])
        name = data[1]
        groups = list(map(int, data[2:]))
        students[student_id] = Student(student_id, name, groups, [])
    for i in range(g):
        for _ in range(d):
            limits = list(map(int, input().split()))
            group_limits[i].append(limits)
        _ = input()

    for _ in range(n):
        solutions = input().split()
        student_id = int(solutions[0])
        solved = [problem == '+' for problem in solutions[1:]]
        students[student_id].solved_problems = [solved[i:i+14] for i in range(0, len(solved), 14)]

    return n, g, d, students, group_limits


def find_student(query, students):
    for student in students.values():
        if query == student.name:
            return student.identifier
        if len(query) == len(student.name):
            for i in range(len(query) - 1):
                if query[:i] + query[i + 1] + query[i] + query[i + 2:] == student.name:
                    return student.identifier
    return None


def process_queries(students):
    q = int(input())
    for _ in range(q):
        query = input()
        if query.isdigit():
            student_id = int(query)
            if student_id in students:
                print(students[student_id].grade)
            else:
                print("Not Found")
        else:
            student_id = find_student(query, students)
            if student_id:
                print(students[student_id].grade)
            else:
                print("Not Found")


def main():
    n, g, d, students, group_limits = process_input()

    # Расчет оценок для каждого студента
    for student in students.values():
        student.calculate_grade(group_limits)
    process_queries(students)


if __name__ == "__main__":
    main()
