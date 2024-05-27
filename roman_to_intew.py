class Solution:
    def romanToInt(self, s: str) -> int:
        def count_roman(s):
            count = 0
            mp = {}
            for char in s:
                if char in mp:
                    mp[char] += 1
                else:
                    mp[char] = 1
            return mp

        def merge(s):
            stiu = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
            sum = 0
            i = 0
            while i < len(s):
                if i + 1 < len(s) and stiu[s[i]] < stiu[s[i + 1]]:
                    sum += stiu[s[i + 1]] - stiu[s[i]]
                    i += 2
                else:
                    sum += stiu[s[i]]
                    i += 1
            return sum

        mp = count_roman(s)
        t = merge(s)
        return t

# Example usage
solution = Solution()
print(solution.romanToInt("III"))      # Output: 3
print(solution.romanToInt("LVIII"))    # Output: 58
print(solution.romanToInt("MCMXCIV"))  # Output: 1994
