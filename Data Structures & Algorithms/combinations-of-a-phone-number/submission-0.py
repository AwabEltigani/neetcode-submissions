class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        phone_num = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        res = []
        if len(digits) == 0:
            return []
        

        def dfs(cur_digits,cur_str):
            print(cur_digits)
            if len(cur_digits) == 0:
                res.append(cur_str)
                return 

            cur_digit = cur_digits[0]
            digit_values = phone_num.get(cur_digit)

            for i in range(len(digit_values)):
                print(i)
                cur_str += digit_values[i]
                dfs(cur_digits[1:],cur_str)
                cur_str = cur_str[0:-1]
        dfs(digits,"")
        return res
