class StringManipulation:
    def reverse_string(self, string:str):
        # Returns the reverse of a string
        return string[-1::-1]
    
    def is_anagram(self, str1:str, str2:str):
        # Returns if two strings are anagrams
        # Two strings contain the same alphabets
        a = list(str1)
        b = list(str2)
        a.sort()
        b.sort()
        return a==b
    
    def find_in_string(self, String:str, key:str):
        pass

    def longest_palindrome(self, string:str):
        pass

    def helper_longest_plaindrome(self, string:str):
        pass

    def parenthesis_checker(self, string:str):
        # Returns true if the parenthesis is balanced
        arr = []
        opening = ['{', '[', '(']
        closing = ['}', ']', ')']
        
        for i in string:
            if len(arr) == 0:
                arr.append(i)
            elif arr[-1] in opening and i in closing:
                if opening.index(arr[-1]) == closing.index(i):
                    arr.pop()
                else:
                    arr.append(i)
            else:
                arr.append(i)
                
        if len(arr) == 0:
            return True
        return False




if __name__=="__main__":
    obj = StringManipulation()
    reverse = obj.reverse_string("hello")
    print(f"The reverse of the string is {reverse} .")
    is_anagram = "" if obj.is_anagram("hello", "ollleh") else " not"
    print(f"The strings provided are{is_anagram} anagrams of each other.")
    is_balanced = "balanced" if obj.parenthesis_checker("{()}}") else "not balanced"
    print(f"The given string is {is_balanced}")


