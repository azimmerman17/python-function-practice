# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(x, y, z):
  return max(x, y, z)

print(max_num(2,9,5))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def multi_list(list):
  product = 1
  for i in list:
    product = product * i
  return product

print(multi_list([2,3,2]))
# Write a Python function called rev_string() to reverse a string.
def rev_string(string):
  return string[::-1]

print(rev_string('string'))
# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(x,a,b):
  return x in range(a,b+1)
     
print(num_within(3,2,4))     
print(num_within(3,1,3))     
print(num_within(10,2,5))


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
triangle = [[1], [1,1]]
def pascal(n):
  if n < 1:
    print('invalid')
  elif n == 1:
    print(triangle[0])
  else:
    row_num = 2
    while len(triangle) < n:
      row= [1]
      prev_row = triangle[row_num - 1]
      print(prev_row)
      for i in range(row_num - 1):
        print(i)
        row.append(prev_row[i] + prev_row[i + 1])
        print(prev_row[i - 1], prev_row[i], row)
      row.append(1)
      
      triangle.append(row)
      row_num += 1
    
    for row in triangle:
      print(row)

pascal(6)
