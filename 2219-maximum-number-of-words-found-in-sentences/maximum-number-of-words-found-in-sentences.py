class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
   
        max_words = 0

        # Iterate through each sentence
        for sentence in sentences:
            # Count the number of spaces in the sentence
            space_count = 0
            for char in sentence:
                if char == " ":
                    space_count += 1
            # The number of words is spaces + 1
            word_count = space_count + 1
            # Update the maximum word count
            max_words = max(max_words, word_count)
        
        return max_words

