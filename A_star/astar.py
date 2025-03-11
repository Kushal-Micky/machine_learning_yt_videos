from queue import PriorityQueue
H = {
    "Biratnagar":46,
    "Itahari": 39,
    "Dharan":41,
    "Rangeli":28,
    "Biratchowk":29,
    "Kanepokhari":17,
    "Urlabari": 6,
    "Damak":0,
}

G = {
    "Biratnagar": {"Itahari": 22, "Rangeli": 25, "Biratchowk":30},
    "Itahari": {"Biratnagar": 22, "Dharan": 20, "Biratchowk": 11},
    "Dharan": {"Itahari": 20},
    "Biratchowk": {"Itahari": 11, "Kanepokhari": 10, "Biratnagar": 30},
    "Rangeli": {"Biratnagar": 25, "Kanepokhari": 25, "Urlabari": 40},
    "Kanepokhari": {"Biratchowk": 10, "Rangeli": 25, "Urlabari": 12},
    "Urlabari": {"Kanepokhari": 12, "Rangeli": 40, "Damak": 6},
    "Damak": {"Urlabari": 6}
}

def astar(start ,G, H, goal):
    PQ = PriorityQueue()
    prev = dict()
    visited = set()
    PQ.put((0+H[start], (start,0)))
    prev[start] = ""
    while (PQ.empty()== False):
        OutStateFScore, (outState, outStateGScore) = PQ.get()
        visited.add (outState)
        if outState == goal:
            return True, prev, OutStateFScore
        for chimeki in G[outState]:
            if chimeki not in visited:
                chimekiGscore = outStateGScore + G[outState][chimeki]
                PQ.put((chimekiGscore+H[chimeki],(chimeki,chimekiGscore)))
                prev[chimeki] = outState
    return False,prev

def reconstruct_path(G, previous, goal):
    path = goal
    while previous[goal] != "":
        path = previous[goal] + "->" + path
        goal = previous[goal]
        return path

start ="Biratnagar"
goal = "Damak"
goalFound, previous, goalFScore = astar(start ,G , H, goal)
if(goalFound):
    print (reconstruct_path(G,previous,goal))
    print (goalFScore)
else:
    print ("NO SOLUTION !!")
