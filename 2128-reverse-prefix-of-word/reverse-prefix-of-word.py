class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word  # If ch is not found, return the word as is

        index = word.index(ch)  # Find the first occurrence of ch
        prefix_reversed = word[:index + 1][::-1]  # Reverse the prefix including ch
        return prefix_reversed + word[index + 1:]
#         word_list = list(word)  #word = "abcdefd", ch = "d" Output: "dcbaefd"  ["a", "b", "c", "d", "e", "f", "h"]
        
#         index = -1
#         for i in range(len(word_list)):
#             if word_list[i] == ch: 
#                 index = i
#                 break
        
#         if index == -1:
#             return word
        
#         left, right = 0, index
#         while left < right:
#             word_list[left], word_list[right] = word_list[right], word_list[left]
#             left += 1
#             right -= 1
        
#         return "".join(word_list)

# class Solution:
#     def reversePrefix(self, word: str, ch: str) -> str:
#         output = []
#         if ch not in word:
#             return word
#         for i in word:
#             if i == ch:
#                 output.append(ch)
#                 output.reverse()
#             else:
#                 output.append(i)
#         return ''.join(output)