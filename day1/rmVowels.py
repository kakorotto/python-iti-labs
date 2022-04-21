def rem_vowel(string):
    vowels = ['a','e','i','o','u']
    result = [letter for letter in string if letter.lower() not in vowels]
    result = ''.join(result)
    print(result)
 
# Driver program
string = "remove vowels program"
rem_vowel(string)
string = "Mobile"
rem_vowel(string)