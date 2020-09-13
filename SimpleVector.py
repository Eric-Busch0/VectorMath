"""
SimpleVector is a small module containing simple vector operations
to help save memory in your program, as well as to limit confusion.

By: Eric Busch
Date: 9/10/20
"""
from math import acos
from math import pi
global Error_Message 
Error_Message = "Vectors arent the same length or improper type"

def condition(a,b=None):
   if b is not None:
      return (len(a) == len(b)) and (type(a) == list or type(a) == tuple) and (type(b) == list or type(b) == tuple)   
   else:
       return (type(a) == list or type(a) == tuple)
  

def magnitude(a):
   global Error_Message
   if condition(a):
      inner = 0
      for i in a:
         inner += i**2
      return inner**0.5
   else:
      print(Error_Message)
      return None

def scale(a,k):
   """
   scale a vector a by a multiple of k
   """
   global Error_Message
   if condition(a):
      temp = [x for x in a]
      for i in range(0,len(a)):
         temp[i] *= k
      return temp
   else:
       print(Error_Message)

def add(a,b):
   """
   adds vector a to b
   """
   global Error_Message
   if condition(a,b):
      temp = []
      for i in range(0,len(a)):
         temp.append(a[i] + b[i])
      return temp
   else:
      print(Error_Message)
      return None
   

def sub(a,b):
   """
   subtracts b from a i.e a - b
   """
   if condition(a,b):
      temp = []
      for i in range(0,len(a)):
         temp.append(a[i] - b[i])
      return temp
   else:
      print(Error_Message)
      return None

def unit(a):
   """
   calculate the unit vector of a
   """
   global Error_Message
   if condition(a):
      temp = []
      mag = magnitude(a)
      for i in range(0,len(a)):
         temp.append(a[i]/mag)
      return temp
   else:
      print(Error_Message)
      return None

def calcVec(a,b):
   """
   takes two sets of points and creates vector from a to b
   """
   if condition(a,b):
      new_vector = []
      for i in range(0, len(a)):
         new_vector.append(b[i] - a[i])
      return new_vector
   else: 
      print(Error_Message)
      return None


def cross3(a,b):
   """
   Calculate the crossproduct of axb, where a and b have 3 components
   """
   global Error_Message
   if condition(a,b) and (len(a) == 3):
      i = (a[1]*b[2]) - (a[2]*b[1])
      j = (a[2]*b[0]) - (a[0]*b[2])
      k = (a[0]*b[1]) - (a[1]*b[0])
      return [i,j,k]
   else:
      print(Error_Message)
      return None

def dot(a,b): 
   """ 
   Calculate the dot product of a dot b
   """
   global Error_Message
   if condition(a,b):
      sum = 0
      for i in range(0,len(a)):
         sum += a[i]*b[i]
      return sum
   else:
      print(Error_Message)
      return None

def angle(a,b,u_type='deg'):
   """
   Calculate the angle between two vectors. u_type specifies if the answer is in degree or radian by spefcifing u_type = 'deg' or 'rad'
   degrees is the default type
   """
   global Error_Message
   if condition(a,b):
      a_dot_b = dot(a,b)
      mag_a = magnitude(a)
      mag_b = magnitude(b)

      ratio = a_dot_b/(mag_a*mag_b)
      if u_type.lower() == 'deg':
         return acos(ratio)*(180/pi)

      elif u_type.lower() == 'rad':
         return acos(ratio)
      else:
         return "Invalid unit type"
   else:
      print(Error_Message)
      return None