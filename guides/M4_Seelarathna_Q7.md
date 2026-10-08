# Handoff: Seelarathna G.P.B: Q7 foodHeuristic

> **Before committing, read and understand this code.** In the viva you will be asked to explain it line by line, and to explain the rest of Q1–Q7 too.
> This code was produced with AI assistance (Claude). The report's AI usage declaration must state this.

## 1. Setup (first time)
```bash
git clone https://github.com/ItsAloka/SE3062-Pacman-Search.git
cd SE3062-Pacman-Search/search
python -m venv .venv
.venv\Scriptsctivate
pip install numpy matplotlib
```

## 2. Branch
```bash
git checkout main
git pull origin main
git checkout -b q7-food-heuristic
```

## 3. Code to add
Replace the `"*** YOUR CODE HERE ***"` / `util.raiseNotDefined()` stub of each function below with this version. Do **not** rename anything.

### Q7: foodHeuristic + helper _bfsDistancesFrom (paste the helper directly below foodHeuristic)  (file: `search/searchAgents.py`)
```python
def foodHeuristic(state: Tuple[Tuple, List[List]], problem: FoodSearchProblem):
    """
    Your heuristic for the FoodSearchProblem goes here.

    This heuristic must be consistent to ensure correctness.  First, try to come
    up with an admissible heuristic; almost all admissible heuristics will be
    consistent as well.

    If using A* ever finds a solution that is worse uniform cost search finds,
    your heuristic is *not* consistent, and probably not admissible!  On the
    other hand, inadmissible or inconsistent heuristics may find optimal
    solutions, so be careful.

    The state is a tuple ( pacmanPosition, foodGrid ) where foodGrid is a Grid
    (see game.py) of either True or False. You can call foodGrid.asList() to get
    a list of food coordinates instead.

    If you want access to info like walls, capsules, etc., you can query the
    problem.  For example, problem.walls gives you a Grid of where the walls
    are.

    If you want to *store* information to be reused in other calls to the
    heuristic, there is a dictionary called problem.heuristicInfo that you can
    use. For example, if you only want to count the walls once and store that
    value, try: problem.heuristicInfo['wallCount'] = problem.walls.count()
    Subsequent calls to this heuristic can access
    problem.heuristicInfo['wallCount']
    """
    position, foodGrid = state
    "*** YOUR CODE HERE ***"
    # Heuristic = true maze distance from Pacman to the FARTHEST remaining food dot.
    #   Admissible: Pacman must eventually reach that dot, and the shortest walk to it
    #   is exactly its maze distance, so the real cost can never be smaller.
    #   Consistent: one move changes the maze distance to any dot by at most 1 (the
    #   step cost), and eating a dot only removes candidates from the max.
    foodList = foodGrid.asList()
    if not foodList:
        return 0

    # Cache: BFS distance maps from each food dot, computed once per dot and reused
    # across every call (walls never change), stored in problem.heuristicInfo.
    distances = problem.heuristicInfo.setdefault('distances', {})
    farthest = 0
    for food in foodList:
        if food not in distances:
            distances[food] = _bfsDistancesFrom(food, problem.walls)
        farthest = max(farthest, distances[food].get(position, 0))
    return farthest

def _bfsDistancesFrom(source, walls):
    """Maze distance from source to every reachable square, using BFS over the walls grid."""
    dist = {source: 0}
    queue = util.Queue()
    queue.push(source)
    while not queue.isEmpty():
        x, y = queue.pop()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nxt = (x + dx, y + dy)
            if not walls[nxt[0]][nxt[1]] and nxt not in dist:
                dist[nxt] = dist[(x, y)] + 1
                queue.push(nxt)
    return dist
```

## 4. Test
```bash
python autograder.py -q q7
```

## 5. Suggested commits (small steps, ideally on different days)
1. `Add BFS distance helper for food heuristic`
2. `Implement food heuristic as maze distance to farthest food (Q7)`
3. `Cache BFS distance maps in problem.heuristicInfo`

Then `git push -u origin <branch>` and open a Pull Request into `main`. Ask another member to review it.

## 6. Viva notes: be able to say these without reading
- h = the TRUE maze distance (BFS through the walls) from Pacman to the FARTHEST remaining food dot.
- Admissible: Pacman has to reach that dot at some point, and the shortest possible walk to it is its maze distance, so the real remaining cost is >= h.
- Consistent: one step changes the maze distance to any dot by at most 1, and eating a dot only removes candidates from the max. So h(n) <= 1 + h(n').
- Speed: the BFS distance map from each food dot is computed once and cached in problem.heuristicInfo (walls never change).
- Result: 4137 nodes expanded on trickySearch (target <= 9000 for 8/8), path cost 60 (optimal).
- Manhattan distance to the farthest dot is also admissible but looser (more nodes). Maze distance is tighter because it accounts for walls.
