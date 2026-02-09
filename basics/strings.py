#a string is immutable , meaning it cannot be changed

string = "tHis iS a sTriNg"

#len - it tells the number of characters in a string , if used in list or dict, then it tells number of items/pairs resp 

print(len(string)) 

#lower

print(string.lower()) #prints a copy of the original string but all the characters are lowercase

#upper

print(string.upper()) #just like lower but makes everything uppercase

#strip

print(string.strip()) #removes the leading and trailing whitespaces of a string and returns a copy of it

#find

print(string.find("r")) #returns the index of the first occurance of the character(or bunch of them)

#capitallise

print(string.capitalize()) #return a copy of string with only the first character of first word in upper case

#title

print(string.title()) #just like capitallise but it capitallises every first letter of every word

#startswith and endswith

print(string.startswith("tH")) #return True if the string starts with 'tH' which is True
print(string.endswith("Ng")) #RETURNS True if the string ends with the 'Ng' which is Also True

#count

print(string.count("s")) #returns the number of occurance of a character in a string

#replace

print(string.replace("s", "W")) #literally find and replace
#and there are many much more...