n, m, k = list(map(int, input().split(" ")))
count = n * m

arr = {}

def merge(arr, item):
  i = 0
  curr = item
  while i <= len(arr):
    if i  == len(arr):
      arr.insert(i, curr)
      break
    new_arr = arr[i]
    if not curr[0] > new_arr[1] + 1 and not curr[1] < new_arr[0] - 1:
      del arr[i]
      new_arr[0] = min(curr[0], new_arr[0])
      new_arr[1] = max(curr[1], new_arr[1])
      curr = new_arr
    else:
      if curr[1] < arr[i][0] - 1:
        arr.insert(i, curr)
        break
      i += 1

for _ in range(k):
  r, c1, c2 = list(map(lambda x: int(x) - 1, input().split(" ")))
  if not r in arr:
    arr[r] = [[c1, c2]]
  else:
    merge(arr[r], [c1, c2])

for rows in list(arr.values()):
  for interval in rows:
    count -= interval[1] - interval[0] + 1

print(count)

# The city of Gridland is represented as an  matrix where the rows are numbered from  to  and the columns are numbered from  to .
#
# Gridland has a network of train tracks that always run in straight horizontal lines along a row. In other words, the start and end points of a train track are  and , where  represents the row number,  represents the starting column, and  represents the ending column of the train track.
#
# The mayor of Gridland is surveying the city to determine the number of locations where lampposts can be placed. A lamppost can be placed in any cell that is not occupied by a train track.
#
# Given a map of Gridland and its  train tracks, find and print the number of cells where the mayor can place lampposts.
#
# Note: A train track may (or may not) overlap other train tracks within the same row.
#
# Input Format
#
# The first line contains three space-separated integers describing the respective values of  (the number of rows), (the number of columns), and  (the number of train tracks).
# Each line  of the  subsequent lines contains three space-separated integers describing the respective values of , , and  that define a train track.
#
# Constraints
#
# Output Format
#
# Print a single integer denoting the number of cells where the mayor can install lampposts.
#
# Sample Input
#
# 4 4 3
# 2 2 3
# 3 1 4
# 4 4 4
# Sample Output
#
# 9
