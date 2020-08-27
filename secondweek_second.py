# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Example 1:

# Input: S = "ab#c", T = "ad#c"
# Output: true
# Explanation: Both S and T become "ac"

# Example 2:

# Input: S = "ab##", T = "c#d#"
# Output: true
# Explanation: Both S and T become "".
# Example 3:

# Input: S = "a##c", T = "#a#c"
# Output: true
# Explanation: Both S and T become "c".
# Example 4:

# Input: S = "a#c", T = "b"
# Output: false
# Explanation: S becomes "c" while T becomes "b".
# Note:

# 1 <= S.length <= 200
# 1 <= T.length <= 200
# S and T only contain lowercase letters and '#' characters.




class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        S = list(S)
        T = list(T)
        
        counter_S = []
        counter_T = []
        
        for i in range(len(S)):
            if(S[i] == '#'):
                if(len(counter_S) == 0):
                    continue;
                else:
                    counter_S.pop()
            else:
                counter_S.append(S[i])
        for i in range(len(T)):
            if(T[i] == '#'):
                if(len(counter_T) == 0):
                    continue;
                else:
                    counter_T.pop()
            else:
                counter_T.append(T[i])
        if(counter_S == counter_T):
            return True
        else:
            return False
        