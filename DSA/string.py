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



if __name__=="__main__":
    obj = StringManipulation()
    reverse = obj.reverse_string("hello")
    print(f"The reverse of the string is {reverse} .")
    is_anagram = "" if obj.is_anagram("hello", "ollleh") else " not"
    print(f"The strings provided are{is_anagram} anagrams of each other.")


