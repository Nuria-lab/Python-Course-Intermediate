# lamda functions

#--multiplying by
numbers = [2, 5, 9]

numbers_square = map((lambda value: value*value), numbers)
print(list(numbers_square))

# or all on one line, with explicit list
print(list(map((lambda value: value*value), [0, -4, 100])))

#----
# mapping and doubling a list
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]

greeting_doubled=list(map(lambda value: 2* value, lst))
print(greeting_doubled)

#-----
#making it upper case
abbrevs = ["usa", "esp", "chn", "jpn", "mex", "can", "rus", "rsa", "jam"]

abbrevs_upper=list(map(lambda value: value.upper(), abbrevs))
print(abbrevs_upper)