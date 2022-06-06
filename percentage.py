if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    total = 0
    for key in student_marks.keys():
        if key == query_name:
            value = student_marks[key]
            for i in value: 
                total+=i
    
    avg = total/(len(value))
    print("{:.2f}".format(avg))