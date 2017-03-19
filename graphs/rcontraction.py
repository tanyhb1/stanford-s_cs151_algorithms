from random import choice
from math import log
def main():
    #run EdgeContraction for n^2 ln n times, saving the minimum cut it returns
    n = []
    edge = []
    a = []
    e = []
    minimum = 0
    with open('kargerMinCut.txt') as data:
        for line in data:
            for i in range(1, len(line.strip().split())):
                placeholder = [int(line.strip().split()[0]), int(line.strip().split()[i])]
                edge.append(placeholder)
            n.append(int(line.strip().split()[0]))
    for i in range(0, int((len(n)**2)*log(len(n)))):
        a = []
        e = []
        for item in n:
            a.append(item)
        for item in edge:
            e.append(item)
        print(i)
        length = len(EdgeContraction(a, e))//2
        print(i)
        if i == 0:
            minimum = length
        elif length < minimum:
            minimum = length
        print(minimum)

def EdgeContraction(n, edge):
    #while len(n) > 2
    #randomly select edge(u,v)
    #delete all the edges that contains (u,v) including self-loops, join the remaining edges of vertices u and v.
    #do this by removing the (u,v) edges and appending the edges that contain u and v?
    #when while-loop breaks, return no. of remaining edges.
    while len(n) > 2:
        
        #random edge, u = r_edge[0], v = r_edge[1]
        r_edge = choice(edge)
        #which of u,v will be the remaining one after merger
        survivor = choice(r_edge)
        #finding the one to be deleted
        if survivor == r_edge[0]:
            non_survivor = r_edge[1]
        else:
            non_survivor = r_edge[0]
        #remove the non_survivor from array n each iteration.
        print(n, non_survivor, survivor)
        if non_survivor in n:
            n.remove(non_survivor)

        storage = []
        #delete all the edges with u,v in them

        for i in range(0, len(edge)//2):
            #if 1st element of edge[i] contains u, and 2nd element contains v, or vice-versa, remove them from edge array
            if(edge[i][0] == survivor and edge[i][1] == non_survivor) or (edge[i][1] == survivor and edge[i][0] == non_survivor):
                edge.pop(i)
            #edges of vertices u and v
            elif(edge[i][0] == non_survivor or edge[i][0] == survivor):
                #if found, append to storage array then delete from edge array
                edge[i][0] = survivor
                storage.append(edge[i])
                edge.pop(i)
            elif(edge[i][1] == non_survivor or edge[i][1] == survivor):
                edge[i][1] = survivor
                storage.append(edge[i])
                edge.pop(i)
        for j in range(0, len(storage)//2):
            #changing first element in storage to surviving u,v; in essence merging u,v's edges into either u or v containing all of u,v's edges  
            edge.append(storage[j])
    return(edge)
if __name__ == "__main__":
    main()