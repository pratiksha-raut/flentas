string = int(input())
for i in range(string):
    string1 = input()
    string2 = input()
    if(string1 in string2) or (string1[::-1] in string2):
        print("YES")
    else:
        print("NO")
