fo = open("input.txt", "r")
pw_range = fo.readline().strip().split("-")
fo.close()

pw_list = range(int(pw_range[0]),int(pw_range[1])+1)

criterion_one = [pw for pw in pw_list if len(str(pw))==6]
criterion_two = [pw for pw in criterion_one]

criterion_three = []
for pw in criterion_two:
    prev_char = None
    for char in str(pw):
        if char == prev_char:
            criterion_three.append(pw)
            break
        prev_char = char

criterion_four = []
for pw in criterion_three:
    prev_char = "0"
    valid = True
    for char in str(pw):
        if char < prev_char:
            valid = False
            break
        prev_char = char
    if valid == True:
        criterion_four.append(pw)

print(len(criterion_four))

    
