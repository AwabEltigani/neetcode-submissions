class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []


        def generateAllparenthesis(num_of_open,num_of_close,cur_str):

            if len(cur_str) == n*2:
                print(cur_str)
                res.append(cur_str)
                return
            
            cur_str += "("
            if num_of_open < n:
                generateAllparenthesis(num_of_open + 1,num_of_close,cur_str)

            cur_str = cur_str[:-1]
            
            if num_of_open > num_of_close and num_of_close < n:
                cur_str += ")"
                generateAllparenthesis(num_of_open,num_of_close + 1,cur_str)


        generateAllparenthesis(1,0,"(")
        return res

            

        