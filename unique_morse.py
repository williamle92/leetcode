"""
International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

'a' maps to ".-",
'b' maps to "-...",
'c' maps to "-.-.", and so on.
For convenience, the full table for the 26 letters of the English alphabet is given below:

[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
Return the number of different transformations among all words we have.

 

Example 1:

Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".
Example 2:

Input: words = ["a"]
Output: 1
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 12
words[i] consists of lowercase English letters.
"""

def uniqueMorseRepresentations(words) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # Create an empty array
        c = []
        for w in words:
            # create an empty string where we will add upon the translated letter into morse
            # the string will be reset after every word
            val= ""
            for d in w:
                # Join all the values in the morse code into one string

                trans="".join(morse[ord(d) -ord('a')])
                val += trans
            # append it into a list
            c.append(val)
        print(c)
        # put that list in an set and return the length 
        return len(set(c))
print(uniqueMorseRepresentations(["gin","zen","gig","msg"]))


def uniqueMorse(words) -> int:
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        # Create an empty array
        c = []
        for word in words:
            c.append("".join(morse[ord(letter)-ord('a')] for letter in word))
        return len(set(c))

print(uniqueMorse(["gin","zen","gig","msg"]))