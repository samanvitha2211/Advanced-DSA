def pairInSortedRotated(arr, target):
   n = len(arr)

    # Find the smallest element (rotation point)
   min_index = 0
   for i in range(1, n):
      if arr[i] < arr[min_index]:
         min_index = i

    
   l = min_index
   r = (min_index - 1 + n) % n

   while l != r:
      current_sum = arr[l] + arr[r]

      if current_sum == target:
         return True
      elif current_sum < target:
         l = (l + 1) % n
      else:
         r = (r - 1 + n) % n

   return False  
  


if __name__ == '__main__':
   arr = list(map(int, input().split()))
   target = int(input())
   print(pairInSortedRotated(arr,target))