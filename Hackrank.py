
test1 = [
    "abba",
    "cadc",
    "cakcefn",
    "cakcedc",
]

test2 = [
    "abba",
    "cadc",
    "cakcefn",
    "cakcedcqw",
    "abba",
    "cadc",
    "cakceasdasdfnc",

]

def display(matrix):
    for element in matrix:
        if len(matrix) == len((element)) and element[0] == element[-1]:
            print(element)

display(test1)
display(test2)