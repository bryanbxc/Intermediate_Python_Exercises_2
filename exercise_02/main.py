import time as t

def fib(n):
   start = t.time()
   fib_array = [0] * (n+1) 
   fib_array[1] = 1
   for i in range(2, n+1): 
      fib_array[i] = fib_array[i-1] + fib_array[i-2] 
   end = t.time()
   execution_time = end - start
   return fib_array[n], execution_time
   
fib_value, execution_time = fib(34)
print("Fibonacci value: ", fib_value, end='\n')
print("Execution time: ", execution_time)
