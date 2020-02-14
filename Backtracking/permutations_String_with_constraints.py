# Backtracking based Python program to prall  
# permutations of a string that follow given  
# constra 
  
def isSafe(str, l, i, r): 
      
    # If previous character was 'A' and character  
    # is 'B', then do not proceed and cut down  
    # the recursion tree.  
    if (l != 0 and str[l - 1] == 'A' and str[i] == 'B'): 
        return False
          
    # This condition is explicitly required for  
    # cases when last two characters are "BA". We  
    # do not want them to swapped and become "AB"  
    if (r == l + 1 and str[i] == 'A' and str[l] == 'B'): 
        return False
      
    return True
      
def permute(str, l, r): 
      
    # We reach here only when permutation  
    # is valid  
    if (l == r): 
        print(*str, sep="", end=" ") 
        return
      
    # Fix all characters one by one  
    for i in range(l, r + 1): 
      
        # Fix str[i] only if it is a  
        # valid move.  
        if (isSafe(str, l, i, r)): 
            str[l], str[i] = str[i], str[l] 
            permute(str, l + 1, r)  
            str[l], str[i] = str[i], str[l] 
  
# Driver Code  
str = "ABC"
permute(list(str), 0, len(str) - 1)  