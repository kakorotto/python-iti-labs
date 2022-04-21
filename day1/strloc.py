ini_string = 'Google'
 
# Character to find
c = "o"
# printing initial string and character
print ("initial string : ", ini_string, "\ncharacter to find : ", c)
 
# Using Naive Method
res = None
for i in range(0, len(ini_string)):
    if ini_string[i] == c:
        res = i + 1
        break
     
if res == None:
    print ("No such character available in string")
else:
    print ("Character {} is present at {}".format(c, str(res)))