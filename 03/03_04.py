# Extended master's theorem: T(n) = aT(n/b)+O(n**k(logn)**i)
# chr(920) = Θ; chr(8712) = ∈; chr(8776) = ≈;
import math

# Source: https://www.nayuki.io/res/master-theorem-solver-javascript/master-theorem-solver.js
def get_complexity(k,i):
  string = ''
  # For n**k
  if type(k)==int:
    if k==0 and i!=0: string += ''
    elif k==0 and i==0: string += '1'
    else: string += '(n)' if k==1 else '(n**'+str(k)+')'
  else: string += '(n**'+str(k)+')'
  # For logn ** i
  if i:
    if string: string += '*'
    string += '(log(n))' if i==1 else '(log(n)**'+str(i)+')'
  return string

# Source: https://www.nayuki.io/res/master-theorem-solver-javascript/master-theorem-solver.js
def master(a,b,k,i):
  error = 'Error in input- '
  flag = False
  if a<1: 
    flag = True
    error+='a must be non negative; '
  if b<=1: 
    flag = True
    error+='b must be greater than 1; '
  if k<0: 
    flag = True
    error+='k must be non negative; '
  if i<0: 
    flag = True
    error+='i must be non negative; '
  if flag: return error,''
  # Recurrence relation
  reccurence = 'T(n):= ' 
  if a==0: reccurence += '0'
  else: reccurence += ('' if a==1 else str(a)+'*') + 'T(n' + ('' if b==1 else '/'+str(b)) + ')'
  reccurence += ' + ' + chr(920) + '[' + get_complexity(k,i) + ']'
  # Complexity
  solution = 'T ' + chr(8712) + ' ' + chr(920) + '('
  p = math.log(a)/math.log(b)
  if p==k: solution += get_complexity(k,i+1)
  elif p<k: solution += get_complexity(k,i)
  else:
    if round(p) == p: solution += get_complexity(round(p),0)
    else: 
      solution += get_complexity('log_'+str(b)+'('+str(a)+')',0)
      solution += ' ' + chr(8776) + ' ' + chr(920) + '(' + get_complexity(round(p,4),0)
  solution += ')'
  return reccurence,solution

a = float(input("enter a: "))
b = float(input("enter b: "))
k = float(input("enter k: "))
i = float(input("enter i: "))

reccurence,solution = master(a,b,k,i)

print('\n\nreccurence relation:',reccurence)
print('\nsolution:',solution)
print()