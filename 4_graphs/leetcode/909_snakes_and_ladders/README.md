# 909. Snakes and Ladders

## Requirements

- Find the minimum number of moves to get the last index

## Solution

- Got completely destroyed by this question. The hardest thing to realize is that the last row is the bottom and that the column needs to be flipped on odd rows when converting the number to a row and column to find the next edge on the board.
- Make a function that converts number to to row and column
- Make a function to get adjacent which is [1,6] to represent dice rolls and fill with snakes and ladder values
- Perform bfs starting from 1 since the game has a 1-based index
- Keep track of distance map and return distance if possible
- It's impossible if there exists at least one node that has not been visited
