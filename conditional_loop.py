#for loop Statement in python
# Syntax:
#  for <Variable> in range(<number of times>):
#     <Statements>

# problem no.1
# (1^2+2^2+3^2+.................+9^2+10^2=what?)
# solve
sum = 0
for i in range(1,11) :
    sum = sum + (i*i)
    print("sum of first 10 squares is", sum)