# filtering

#--- entry level way
def filter_numbers(numb_):
    odd_lst=[]
    for num in numb_:
        if num % 2 == 1 :
            odd_lst.append(num)
    return odd_lst


number_list=[0,54,87,86,1015,69,87]
print(filter_numbers(number_list))
#----

# using filter funct + lambda funct

lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

filter_testing=list(filter(lambda i:'w' in i,lst_check))
print(filter_testing)
            
#----
#testing words with an 'i' in it
lst = ["witch", "halloween", "pumpkin", "cat", "candy", "wagon", "moon"]

lst2=list(filter(lambda x : 'i' in x, lst))
print(lst2)

#comining map anf filter in one line
nums_ = [25, 5, 8, 7, 0, 74]
#chaining together filter and map:
# first, filter to keep only the even numbers
# double each of them
print(map(lambda x: x*2, filter(lambda y: y % 2 == 0, nums_)))

# same version using list comprehension
print([i*2 for i in nums_ if i % 2 == 0])
