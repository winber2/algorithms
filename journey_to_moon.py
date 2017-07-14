# The member states of the UN are planning to send  people to the Moon. But there is a problem. In line with their principles of global unity, they want to pair astronauts of  different countries.
#
# There are  trained astronauts numbered from  to . But those in charge of the mission did not receive information about the citizenship of each astronaut. The only information they have is that some particular pairs of astronauts belong to the same country.
#
# Your task is to compute in how many ways they can pick a pair of astronauts belonging to different countries. Assume that you are provided enough pairs to let you identify the groups of astronauts even though you might not know their country directly. For instance, if  are astronauts from the same country; it is sufficient to mention that  and  are pairs of astronauts from the same country without providing information about a third pair .
#
# Input Format
#
# The first line contains two integers,  and , separated by a single space.  lines follow. Each line contains integers separated by a single space  and  such that
#
#
# and  and  are astronauts from the same country.
#
# Constraints
#
# Output Format
#
# An integer that denotes the number of permissible ways to choose a pair of astronauts.
#
# Sample Input 0
#
# 5 3
# 0 1
# 2 3
# 0 4
# Sample Output 0
#
# 6
# Explanation 0
#
# Persons numbered ,  and  belong to the same country, and those numbered  and  belong to the same country, but different from the previous one. All in all, the UN has  ways of choosing a pair:
#
# persons  and
# persons  and
# persons  and
# persons  and
# persons  and
# persons  and
# Sample Input 1
#
# 4 1
# 0 2
# Sample Output 1
#
# 5
# Explanation 1
#
# Persons numbered  and  belong to the same country, and persons  and  don't share countries with anyone else, so they belong to unique countries on their own. All in all, the UN has  ways of choosing a pair:
#
# persons  and
# persons  and
# persons  and
# persons  and
# persons  and

n, p = map(int, input().split())
total = n * (n - 1) // 2
sets = []
for _ in range(p):
  a1, a2 = map(int, input().split())
  ids = []
  for idx, currSet in enumerate(sets):
    if a1 in currSet or a2 in currSet:
      ids.append(idx)
  if len(ids) == 0:
    sets.append({a1, a2})
  else:
    newSet = {a1, a2}
    ids.reverse()
    for i in ids:
      newSet.update(sets[i])
      del sets[i]
    sets.append(newSet)
for currSet in sets:
  k = len(currSet)
  total -= k * (k - 1) // 2

print(total)
