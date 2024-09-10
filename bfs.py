from pyamaze import maze,agent,textLabel,COLOR
from collections import deque

from timeit import default_timer as timer

def BFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    frontier = deque()
    frontier.append(start)
    bfsPath = {}
    explored = [start]
    bSearch=[]

    while len(frontier)>0:
        currCell=frontier.popleft()
        if currCell==m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                elif d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                elif d=='S':
                    childCell=(currCell[0]+1,currCell[1])
                elif d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if childCell in explored:
                    continue
                frontier.append(childCell)
                explored.append(childCell)
                bfsPath[childCell] = currCell
                bSearch.append(childCell)
    fwdPath={}
    cell=m._goal
    while cell!=(m.rows,m.cols):
        fwdPath[bfsPath[cell]]=cell
        cell=bfsPath[cell]
    return bSearch,bfsPath,fwdPath

if __name__=='__main__':

    m=maze(12,10)
    m.CreateMaze(loopPercent=50,theme='light')
    start_time = timer()
    bSearch,bfsPath,fwdPath=BFS(m)
    end_time = timer()
    a=agent(m,footprints=True,color=COLOR.green,shape='square',filled=True)
    c=agent(m,1,1,footprints=True,color=COLOR.black,shape='square',filled=True,goal=(m.rows,m.cols))
    b=agent(m,footprints=True,color=COLOR.red,shape='square',filled=False)
    m.tracePath({a:bSearch},delay=100)
    m.tracePath({c:bfsPath},delay=100)
    m.tracePath({b:fwdPath},delay=100)
    
    total_time = end_time - start_time
    l = textLabel(m, 'Maze Solving (BFS) - Time', total_time)


    m.run()