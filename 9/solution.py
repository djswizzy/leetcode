class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        string = str(x)
        rev_list = [g for g in string]
        str_list = [g for g in string]
        rev_list.reverse()
        if str_list == rev_list:
            return True
        else:
            return False
