if __name__ == "__main__":
    students = []
    for _ in range(int(input())):
        name = input()
        score = int(input())
        students.append([name, score])
        
    unique_scores = sorted(set(score for name, score in students))
    second_lowest_score = unique_scores[1]
    second_lowest_student = [name for name, score in students if score == second_lowest_score]
    second_lowest_student.sort()
    for name in second_lowest_student:
        print(name)
    