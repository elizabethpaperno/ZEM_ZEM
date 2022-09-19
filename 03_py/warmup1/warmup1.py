def sleep_in(weekday, vacation):
  return (not weekday or vacation)
  
 def monkey_trouble(a_smile, b_smile):
  return (a_smile and b_smile) or (not a_smile and not b_smile)

def sum_double(a, b):
  if (a == b):
    return (4*a)
  return (a + b)

def diff21(n):
  if (n > 21):
    return (2*(n-21))
  return (21-n)
  
def parrot_trouble(talking, hour):
  return (talking and (hour < 7 or hour > 20))

def makes10(a, b):
  return ((a == 10) or (b == 10) or (a + b == 10))

def near_hundred(n):
  return ( (abs(100-n) <= 10) or (abs(200-n) <= 10) )

def pos_neg(a, b, negative):
  if (not negative):
    return (a*b < 0)
  return (a < 0 and b < 0)
  
def not_string(str):
  if (str[0:3] == "not"):
    return (str)
  return ("not " + str)

def missing_char(str, n):
  return (str[0:n] + str[n+1:len(str)])

def front_back(str):
  if (len(str) > 2):
    return (str[len(str)-1] + str[1:len(str)-1] + str[0])
  elif (len(str) == 2):
    return (str[1] + str[0])
  return (str)

def front3(str):
  if (len(str) > 2):
    return (str[0:3] * 3)
  return (str*3)
//warmup 2
def string_times(str, n):
  return (str*n)

def front_times(str, n):
  if (len(str) > 2):
    return (str[0:3] * n)
  return (str*n)

def string_bits(str):
  new = ""
  for index in range(len(str)):
    if (index % 2 == 0):
      new += str[index]
  return (new)

def string_splosion(str):
  new = ""
  for index in range(len(str)+1):
    new += str[0:index]
  return (new)

def last2(str):
  last = str[len(str)-2:len(str)]
  count = 0
  for index in range(len(str)-2):
    if (str[index:index+2] == last):
      count+=1
  return count

