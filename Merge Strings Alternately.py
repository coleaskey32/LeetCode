#Merge Strings Alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = ""
        index1 = index2 = 0
        wordToAppend = 1

        while (index1 != len(word1) and index2 != len(word2)):

            if(word1 != "" and wordToAppend == 1):
                ans += word1[index1]
                index1 += 1
                wordToAppend = 2
            else:
                ans += word2[index2]
                index2 += 1
                wordToAppend = 1
        

        while(index1 != len(word1)):
            ans += word1[index1]
            index1 += 1
        while(index2 != len(word2)):
            ans += word2[index2]
            index2 += 1
        
        return ans



# Create an instance of the Solution class
solution = Solution()

# Example usage
word1 = "ab"
word2 = "pqrs"
merge_string_alternately = solution.mergeAlternately(word1, word2)
print(merge_string_alternately)
