class Solution:
    def intToRoman(self, num: int) -> str:
        rom_dict = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL",10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
        output =''
        for key in rom_dict:
            while (num - key) > -1:
                output+=rom_dict[key]
                num = num - key
        return output
