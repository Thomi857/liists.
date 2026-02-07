words = ["abc","car","racecar","cool"]
def firstPalindrome( words):
        for word in words:
            if word == word[::-1]:
                return word
            else:
                 return ""
print(firstPalindrome(words))