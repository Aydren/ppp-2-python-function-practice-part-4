""" 
after re reading the first question i realize i did the wrong thing
def max_nun(*nums):
    result = 0
    for i in nums:
        if i > result:
            result = i
        else:
            result = result
    return result 
"""
def max_nun(x, y, z):
    return max(x, y, z)

print(max_nun(5, 14, 11))


def mult_list(*nums):
    result = 1
    for i in nums:
        result = result * i
    return result

print(mult_list(2,2,5,5,10))

def rev_string(str):
    result = ''
    for i in str[::-1]:
        result = result + i
    return result

print(rev_string('hello world'))


def num_within(x, y, z):
    if x >= y and x <= z:
        return True
    else:
        return False

print(num_within(1,1,3))


## pascal was the only one i could not figure out
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)
      
pascal(0)
pascal(1)
pascal(3)