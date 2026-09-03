class Solution:
    def uniformArray(self, num1: list[int]) -> bool:
        odd = [num for num in num1 if num %2!=0]
        even=[num for num in num1 if num %2==0]
        all_even =True
        all_odd=True
        if odd:
            min_odd = min(odd)
            for num in odd:
                if num <=min_odd:
                    all_even=False
                    break
        if even:
            if not odd:
                all_odd=False
            else:
                for num in even:
                    if num <=min_odd:
                        all_odd=False
                        break
        return all_even or all_odd