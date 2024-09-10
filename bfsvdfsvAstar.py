from bfs import BFS
from Astar import aStar
from dfs import DFS
from pyamaze import maze,agent,COLOR,textLabel

from timeit import default_timer as timer

# DFS CODE

# m = maze(20, 30)
# m.CreateMaze(loadMaze='maze1.csv')
# start_time = timer()
# dSearch, dfsPath, fwdPath = DFS(m)
# end_time = timer()


# l = textLabel(m, 'DFS Path Length', len(fwdPath) + 1)
# l = textLabel(m, 'DFS Search Length', len(dSearch) + 1)

# a = agent(m, footprints=True, color=COLOR.green, filled=True)
# b = agent(m, 1, 1, footprints=True, color=COLOR.red, filled=True, goal=(m.rows, m.cols))
# c = agent(m, footprints=True, color=COLOR.black)
# m.tracePath({a: dSearch}, delay=50)
# m.tracePath({b: dfsPath}, delay=100)
# m.tracePath({c: fwdPath}, delay=100)
 
# total_time = end_time - start_time
# l = textLabel(m, 'Maze Solving (DFS) - Time', total_time)

# m.run()


# # BFS CODE


# m=maze(20,30)
# m.CreateMaze(loadMaze='maze1.csv')
# start_time = timer()
# bSearch,bfsPath,fwdPath=BFS(m)
# end_time = timer()
# l=textLabel(m,'BFS Path Length',len(fwdPath)+1)
# l=textLabel(m,'BFS Search Length',len(bSearch)+1)

# a=agent(m,footprints=True,color=COLOR.green,filled=True)
# b=agent(m,1,1,footprints=True,color=COLOR.red,filled=True,goal=(m.rows,m.cols))
# c=agent(m,footprints=True,color=COLOR.black)
# m.tracePath({a:bSearch},delay=50)
# m.tracePath({b:bfsPath},delay=100)
# m.tracePath({c:fwdPath},delay=100)
# total_time = end_time - start_time
# l = textLabel(m, 'Maze Solving (BFS) - Time', total_time)
# m.run()


# A STAR CODE

m=maze(20,30)
m.CreateMaze(loadMaze='maze2.csv')
start_time = timer()
aSearch,aPath,fwdPath=aStar(m)
end_time = timer()
l=textLabel(m,'A-Star Path Length',len(fwdPath)+1)
l=textLabel(m,'A-Star Search Length',len(aSearch)+1)

a=agent(m,footprints=True,color=COLOR.green,filled=True)
b=agent(m,1,1,footprints=True,color=COLOR.red,filled=True,goal=(m.rows,m.cols))
c=agent(m,footprints=True,color=COLOR.black)
m.tracePath({a:aSearch},delay=50)
m.tracePath({b:aPath},delay=100)

m.tracePath({c:fwdPath},delay=100)
total_time = end_time - start_time
l = textLabel(m, 'Maze Solving (ASTAR) - Time', total_time)

m.run()
 