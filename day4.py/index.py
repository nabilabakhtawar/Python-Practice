#strings 
str1="Nabila Bakhtwar"
print(str1)
str2='my age is 22 '
print(str2)
str3='''I am a student of computer science '''
print(str3)
str4="this is a string \n we are creating it in python"
print(str4)
str5='this is a string \t we are creating it in python'
print(str5)

str6="Hello"
len1=len(str6)
print(len1)
str7="World"
len2=len(str7)
print(len2)

final_str=str6 + " " + str7
len3=len(final_str)
print(len3)
print(final_str)

#string indexing
str8="Hello World"
print(str8[0])
#string slicing
str9="Nabila Bakhtawar"
print(str9[1:4])
print(str9[7:17])
print(str9[7:len(str9)])
print(str9[7:])
print(str9[-9:-4])