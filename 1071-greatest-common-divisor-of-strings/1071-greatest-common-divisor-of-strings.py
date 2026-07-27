class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        length = min(len(str1), len(str2))
        
        while length > 0:
            if len(str1) % length == 0 and len(str2) % length == 0:
                candidate = str1[:length]
                
                if candidate * (len(str1) // length) == str1 and \
                   candidate * (len(str2) // length) == str2:
                    return candidate
                    
            length -= 1
        
        return ""