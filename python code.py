class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        
      
        # Initialize an empty list to store the permutation
        permutation = []
      
        # Initialize a list to keep track of used numbers
        visited = [False] * (n + 1)
      
        # Iterate through the numbers from 1 to n
        for i in range(n):
            # Compute the factorial of (n-i-1) which helps in determining the blocks
            factorial = 1
            for j in range(1, n - i):
                factorial *= j
          
            # Iterate through the numbers to find the unused numbers
            for j in range(1, n + 1):
                if not visited[j]:
                    # If k is greater than the factorial, it means we need to move to the next block
                    if k > factorial:
                        k -= factorial
                    else:
                        # Found the right place for the number 'j' in the permutation
                        permutation.append(str(j))  # Add the number to the permutation
                        visited[j] = True  # Mark the number as visited
                        break  # Break since we have used one number in the permutation
      
        # Join the list of strings to form the final permutation string
        return ''.join(permutation)
