if __name__ == '__main__':
    records=[]
    marks=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name,score])
        marks.append(score)
    marks.sort()
    records.sort()
    minimum = marks[0]
    second_minimum=0
    for i in marks:
        if i != minimum:
            second_minimum = i
            break
    for data in records:
        if data[1] == second_minimum:    # the data[0] will be name and data[1] will be score
            print(data[0])              
