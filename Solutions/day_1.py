import pandas as pd

file = open("day_1_input.txt", "r")
content = file.read().split("\n")

def sum_values_from_file(content):
    sum = 0
    for val in content:
        first = 0
        last = len(val) - 1
        while first <= last:
            v1 = val[first]
            v2 = val[last]
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

# solution answer :/
def extract_and_combine_numbers(content):
    numbs = 'one two three four five six seven eight nine'.split()
    print(pd.DataFrame(content)
        .replace({k:k+n+k for n,k in zip("123456789",numbs)},regex=True)
        .replace(regex=r"\D",value='')
        .map(lambda x:int(x[0]+x[-1]))
        .sum())


sum_values_from_file(content=content)
extract_and_combine_numbers(content=content)