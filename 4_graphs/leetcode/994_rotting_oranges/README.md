# [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/)

## Requirements

- Rotton oranges infect the oranges around it
- Determine when there will still be some fresh ones

## Solution 1 - Brute Force

- Iterate the grid several times with a transit stage for infecting neighbors
- Mark the grid for change, 3 to prevent over infecting and return changed and still_uninfected
- Iterate grid again to mark set 3s to 2s
- Repeat until no more changes happen
- It's impossible if the last infect stage returned still_uninfected

```
function infect():
  changed,has_uninfected=False,False
  for i in n:
    for j in m:
      if grid[i,j]==2:
        for neighbor in left,right,up,down:
          if neighbor==1:
            changed=True
            grid[neighbor]=3
        if grid[i,j]==1:
          has_uninfected=True
  return changed,has_uninfected

function update():
  for i in n:
    for j in m:
      if grid[i,j]==3:
        grid[i,j]==2

Loop:
  changed,has_uninfected=infect()
  if changed:
    minutes+=1
    update()
  elif has_uninfected:
    return -1
  else:
    return minutes
```

## Solution 2 - BFS

- Run level order bfs infected as q is added

```
def bfs():
  minutes=0
  q=all cells marked 2
  while q:
    count=length of q
    repeat count times:
      cell=q.popleft()
      for neighbor in left,right,up,down:
        if neighbor==1:
          neighbor=2
          q.append(neighbor)
  return minutes

minutes=bfs()
if any cell has a 1:
  return -1

return minutes
```
