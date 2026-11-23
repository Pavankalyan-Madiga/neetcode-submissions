class Solution:
    def reverse(self, x: int) -> int:

        revNum = 0

        if x < 0:
            sign = -1
        else:
            sign = 1

        x = abs(x)

        while x > 0:

            lastDigi = x % 10

            revNum = (revNum * 10) + lastDigi

            x = x // 10

        revNum = revNum * sign

        # 32-bit integer range check
        if revNum < -2**31 or revNum > 2**31 - 1:
            return 0

        return revNum