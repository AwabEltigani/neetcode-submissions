class Solution:
    def totalFruit(self, fruits: list[int]) -> int:

        l = 0
        r = 0
        n = len(fruits)
        current_baskets = {}
        cur_max = 0
        cur = 0

        while n > r:
            while n > r and (len(current_baskets) < 2 or fruits[r] in current_baskets):
                current_baskets[fruits[r]] = current_baskets.get(fruits[r],0) + 1
                r += 1
            print(current_baskets)
            if len(current_baskets) == 2:
                cur_max = max(cur_max,r - l)
            while l < r and len(current_baskets) >= 2:
                current_baskets[fruits[l]] = current_baskets.get(fruits[l]) - 1
                if current_baskets[fruits[l]] == 0:
                    del current_baskets[fruits[l]]
                l = l+1
        return max(cur_max,r-l)

        