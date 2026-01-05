#Order of Operations (PEMDAS)
# There are 2 ways to do this
# First Method
expression = 5 + 2 * 3**2
print(expression)
# Other Using eval() Function
#Avoid eval() unless absolutely necessary, because it can execute arbitrary code and is a security risk. Use it only for controlled, safe inputs.
print(eval("5+2*3**2"))
print(eval("(8-3)*2**2"))
print(eval("12/(2*3)+4"))
print(eval("(6+2)**2-5*3"))
print(eval("100/(5**2)+7"))
print(eval("(3+4)*(2**3-5)"))
print(eval("2**3+4*(6-2)"))
print(eval("(15-3)/(2+1)+5**2"))
print(eval("(10-2)**2/(3+1)"))
print(eval("(2**4+3**2)-(5*2)"))
print(eval("(3+5)*(2**3-4)+18/3"))
print(eval("(12/(2**2))+(3*(4+1))"))
print(eval("((2**3)**2-(3*4))+(18/3)"))
print(eval("(50-(3**2*2))/(4+1)"))
print(eval("(7*(2**3+4))-(36/(3*2))"))
print(eval("((5+3)*(2**2))-((4**2)/2)"))
print(eval("(100/(2**3))+((3**2)*(2+1))"))
print(eval("((2**5)-(3**3))+((4*3)-(2**2))"))
print(eval("(6*(2**3+5))-((3**2)+(4*2))"))
print(eval("((8**2)/(2**3))+((5*3)-(2**2))"))
