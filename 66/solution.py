class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits.reverse()
        carry = 1
        for i in range(len(digits)):
            val = digits[i] + carry
            digits[i] = val%10
            if i == len(digits)-1 and val >= 10:
                digits.append(1)
                break
            if val < 10:
                break
        digits.reverse()
        return digits
