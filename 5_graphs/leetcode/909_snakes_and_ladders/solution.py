from typing import List


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        adj_list = []
        final = n * n

        def num_to_rc(num):
            num -= 1
            original_row = num // n
            col = num - original_row * n
            row = n - original_row - 1
            if original_row % 2 == 1:
                col = n - col - 1
            return row, col

        print(num_to_rc(12))

        def get_adj(num):
            adj = set()
            for dice in range(1, 7):
                end = num + dice
                if end > final:
                    return adj
                r, c = num_to_rc(end)
                bval = board[r][c]
                if bval > -1:
                    adj.add(bval)
                else:
                    adj.add(end)
            return adj

        def shortestpath(n):
            visited = {}
            q = [n]
            while q:
                v = q.pop(0)
                if v == final:
                    return visited[v]
                for w in get_adj(v):
                    if w not in visited:
                        visited[w] = visited[v] + 1
                        q.append(w)
            return -1

        return shortestpath(1)
