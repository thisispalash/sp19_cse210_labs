def partition(arr,low,high):
  i = low-1
  pivot = arr[high] # last elem as pivot
  for j in range(low,high):
    if arr[j]<=pivot:
      i+=1
      arr[i],arr[j] = arr[j],arr[i]
  arr[i+1],arr[high] = arr[high],arr[i+1]
  return i+1

def quicksort(arr, low, high):
  if low<high:
    index = partition(arr,low,high)
    quicksort(arr, low, index-1)
    quicksort(arr, index+1, high)
  return arr

if __name__ == '__main__':
  arr = [5,4,3,2,1]
  print(quicksort(arr,0,len(arr)-1))