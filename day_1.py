file = open("day_1_input.txt", "r")
content = file.read().split("\n")

sum = 0
for val in content:
    first = 0
    last = len(val) - 1
    while first <= last:
        v1 = val[first]
        v2 = val[last]
        print(v1, v2)
        if(not val[first].isalpha()):
            v1 = val[first]
        else:
            first += 1
        if(not val[last].isalpha()):
            v2 = val[last]
        else:
            last -= 1
        if(not v1.isalpha() and not v2.isalpha()):
            break
    if(not v1.isalpha() and not v2.isalpha()):
        newVal = v1+v2
    elif(not v1.isalpha() and v2.isalpha()):
        newVal = v1
    elif(v1.isalpha() and v2.isalpha()):
        newVal = v2
    sum += int(newVal)
print("SUM: ", sum)
