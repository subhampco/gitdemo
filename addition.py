#earlier this addition file is running on python2.7 now we are shifting on python3
#commenting below line
#print 'Adding Two Numbers 10 and 20 :',10+20
print('How to color the git console?')
print('git config --global color.ui auto')
print('credential helper cache feature it means remember my credential')
print('git config --global credential.helper cache')
#creating with python3 in mind
#print('Adding two numbers 10 and 20: ',10+20)
#going to use function concept in addition as per client requirement to improve the modularity of the code
def addTwoNum(x,y):
  return x+y
#there is a typo in print function fixing it by using comma
print("Adding two Number 10 and 20: ",addTwoNum(10,20))
#adding multiplication feature
#adding function for product by sumesh
def product(x,y):
  return x*y

print("Two Number product 10 * 20 is: ",product(10,20))
