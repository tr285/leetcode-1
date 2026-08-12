class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        rt = 0
        num = 0
        sign = 1

        for ch in s:

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '+':
                rt += sign * num
                num = 0
                sign = 1

            elif ch == '-':
                rt += sign * num
                num = 0
                sign = -1

            elif ch == '(':
                stack.append(rt)
                stack.append(sign)

                rt = 0
                sign = 1

            elif ch == ')':
                rt += sign * num
                num = 0

                previous_sign = stack.pop()
                previous_result = stack.pop()

                rt = previous_result + previous_sign * rt

        rt += sign * num

        return rt