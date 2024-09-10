from pyamaze import maze,agent,textLabel,COLOR

from timeit import default_timer as timer

def DFS(m,start=None):
    if start is None:
        start=(m.rows,m.cols)
    explored=[start]
    frontier=[start]
    dfsPath={}
    dSearch=[]
    while len(frontier)>0:
        currCell=frontier.pop()
        dSearch.append(currCell)
        if currCell==m._goal:
            break
        poss=0
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d =='E':
                    child=(currCell[0],currCell[1]+1)
                if d =='W':
                    child=(currCell[0],currCell[1]-1)
                if d =='N':
                    child=(currCell[0]-1,currCell[1])
                if d =='S':
                    child=(currCell[0]+1,currCell[1])
                if child in explored:
                    continue
                poss+=1
                explored.append(child)
                frontier.append(child)
                dfsPath[child]=currCell
        if poss>1:
            m.markCells.append(currCell)
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[dfsPath[cell]]=cell
        cell=dfsPath[cell]
    return dSearch,dfsPath,fwdPath

if __name__=='__main__':
    m=maze(10,10) 
    m.CreateMaze(2,4) 
    start_time = timer()
 
    dSearch,dfsPath,fwdPath=DFS(m,(5,1)) 
    end_time = timer()

    a=agent(m,5,1,goal=(2,4),footprints=True,shape='square',color=COLOR.green)
    b=agent(m,2,4,goal=(5,1),footprints=True,filled=True)
    c=agent(m,5,1,footprints=True,color=COLOR.black)
    m.tracePath({a:dSearch},showMarked=True)
    m.tracePath({b:dfsPath})
    m.tracePath({c:fwdPath})
    
    total_time = end_time - start_time
    l = textLabel(m, 'Maze Solving (DFS) - Time', total_time)

    m.run()
 