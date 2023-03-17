#1 arb_args - Takes in any number of arguments and prints them one at a time.
def arb_args(*args):
  for a in args:
    print(a)

arb_args('a', 'b', 'c', 2)
arb_args('a', 'c', 2)
#2 inner_func - Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.
def inner_func(x,y):
  def inner_sum(x,y):
    return x + y
  def inner_sub(x,y):
    return x - y
  print(inner_sum(x,y) + inner_sub(x,y))

inner_func(9, 4)

#3 lunch_lady - Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.
def lunch_lady(name, lunch='mystery meat' ):
  print(f'{name}, {lunch}') 

lunch_lady('Sam', 'pizza')
lunch_lady('Ross')
#4 sum_n_product - Accepts two integers and returns both the sum and the product.
def sum_n_product(x, y):
  return x + y, x * y

print(sum_n_product(4, 5)) 
#5 alias_arb_args - Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
alias_arb_args = arb_args

#6 arb_mean - Accepts any number of integers and prints their average.
def arb_mean(*args):
  sum = 0
  for a in args:
    sum += a
  return sum / len(args)

  print(arb_mean(3,4,5))
  print(arb_mean(3,4,5,6))

#7 arb_longest_string - Accepts any number of strings and returns the longest one.
def arb_longest_string(*args):
  string = ''
  for i in args:
    if len(i) > len(string):
      string = i
  print(string)

arb_longest_string('w','www','ww')