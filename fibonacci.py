def fibonacci(n):
  if n < 0:
    ValueErroe("Input 0 or greater only!")
  if n <= 1:
    return n
  list_fibs = [1,1]
  for i in range(2,n):
    fibs_add = list_fibs[i-1] + list_fibs[i-2]
    list_fibs.append(fibs_add)
  return list_fibs[-1]
  