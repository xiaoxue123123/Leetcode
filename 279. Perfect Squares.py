# def numSquares(n):
#     import math
#     square_nums = [i ** 2 for i in range(0, int(math.sqrt(n)) + 1)]
#     dp = [float('inf')] * (n + 1)
#     dp[0] = 0
#     for i in range(1, n + 1):
#         for sq in square_nums:
#             print('i',i,'sq',sq)
#             if i < sq:
#                 break
#             print('before dp',dp)
#             dp[i] = min(dp[i], dp[i - sq] + 1)
#             print('after dp',dp)
#     return dp[-1]


def numSquares(n):
    def is_divided_by(n, count):
        """
            return: true if "n" can be decomposed into "count" number of perfect square numbers.
            e.g. n=12, count=3:  true.
                 n=12, count=2:  false
        """
        if count == 1:
            return n in square_nums

        for k in square_nums:
            print('pre','k',k,'n-k',n-k,'count-1',count-1)
            if is_divided_by(n - k, count - 1):
                print('post','k',k, 'n-k', n - k, 'count-1', count - 1)
                return True
        return False

    square_nums = set([i * i for i in range(1, int(n ** 0.5) + 1)])

    for count in range(1, n + 1):
        if is_divided_by(n, count):
            return count