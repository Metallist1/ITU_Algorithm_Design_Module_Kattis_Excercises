import sys

T=input() #testcase number
for _ in range(int(T)):
    diffrences = "";
    firstword = input().strip();
    secondword = input().strip();
    for i, c in enumerate(firstword):
        if c != secondword[i]:
            diffrences=diffrences+"*"
        else:
            diffrences=diffrences+"."
    print (firstword)
    print (secondword)
    print (diffrences)
    print ("")