class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
    
    # Morse code mapping for all letters
        morse_code = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", 
            ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", 
            ".--", "-..-", "-.--", "--.."
        ]
        
        # Store transformations in a list
        transformations = []
        
        # Loop through each word in the input list
        for word in words:
            transformation = ""
            
            for char in word:
                # Calculate the index by subtracting 'a' from the character without using ord
                index = 0
                for letter in "abcdefghijklmnopqrstuvwxyz":
                    if char == letter:
                        break
                    index += 1
                # Add the corresponding Morse code
                transformation += morse_code[index]
            # Add the transformation to the list if not already present
            if transformation not in transformations:
                transformations.append(transformation)
        
        # Return the count of unique transformations
        return len(transformations)







        # m = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # a = "abcdefghijklmnopqrstuvwxyz"
        # p = []
        # ans = []
        # for q in words:
        #     b = ""
        #     for i in q:
        #         b += m[a.index(i)]
        #     p.append(b)
        # for q in p:
        #     if q not in ans:
        #         ans.append(q)
        # return len(ans)