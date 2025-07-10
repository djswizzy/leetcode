class Solution:
    def romanToInt(self, s: str) -> int:
        rom_dict = {"IV":4,"IX":9,"XL":40,"XC":90,"CD":400,"CM":900,"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        total = 0
        for key in rom_dict:
            total += rom_dict[key]*s.count(key)
            s = s.replace(key,"")
            print(key,s.count(key),total,s)
        return total
