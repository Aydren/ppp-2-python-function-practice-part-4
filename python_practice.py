def max_nun(*nums):
    result = 0
    for i in nums:
        if i > result:
            result = i
        else:
            result = result
    return result


print(max_nun(5, 14, 11, 9, 18))


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


def num_within():
    print('hello')