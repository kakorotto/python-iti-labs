def str_split(s):
    s1 = s[:len(s)//2]
    s2 = s[len(s)//2 if len(s)%2 == 0
                     else (((len(s)//2))+1):]
    print(s1,s2)

str_split("example")

str_split("Pola")