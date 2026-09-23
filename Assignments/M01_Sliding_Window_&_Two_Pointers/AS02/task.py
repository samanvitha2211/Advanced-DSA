def Check_Palindrome(n: int,s:str) -> bool:
   left = 0
   right = n - 1
   deleted = False

   while left < right:
      if s[left] != s[right]:
         if deleted:
               return False

         # Try deleting either the left or right character
         left_check = s[left + 1:right + 1]
         right_check = s[left:right]

         return left_check == left_check[::-1] or right_check == right_check[::-1]

      left += 1
      right -= 1

   return True
   


if __name__ == '__main__':
   n = int(input())
   s = input()
   print(Check_Palindrome(n,s))