# Handoff: Nawodya K.P.G.P: Q3 UCS, Q4 A*, Q5 CornersProblem

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
git checkout -b q3-q4-ucs-astar
```

## 3. Code to add
Replace the `"*** YOUR CODE HERE ***"` / `util.raiseNotDefined()` stub of each function below with this version. Do **not** rename anything.

### Q3: uniformCostSearch  (file: `search/search.py`)
```python
def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    # Same graph-search loop, but the fringe is a priority queue ordered by
    # g(n) = total path cost from the start, so the cheapest node is expanded first.
    fringe = util.PriorityQueue()
    fringe.push((problem.getStartState(), [], 0), 0)
    expanded = set()

    while not fringe.isEmpty():
        state, actions, cost = fringe.pop()

        # Goal test on pop: the first time a goal is popped it has the lowest cost
        if problem.isGoalState(state):
            return actions

        if state not in expanded:
            expanded.add(state)
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in expanded:
                    newCost = cost + stepCost
                    fringe.push((successor, actions + [action], newCost), newCost)

    return []
```

### Q4: aStarSearch  (file: `search/search.py`)
```python
def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    # Identical to UCS except the priority is f(n) = g(n) + h(n):
    # cost so far plus the heuristic estimate of the cost still to go.
    start = problem.getStartState()
    fringe = util.PriorityQueue()
    fringe.push((start, [], 0), heuristic(start, problem))
    expanded = set()

    while not fringe.isEmpty():
        state, actions, cost = fringe.pop()

        if problem.isGoalState(state):
            return actions

        if state not in expanded:
            expanded.add(state)
            for successor, action, stepCost in problem.getSuccessors(state):
                if successor not in expanded:
                    newCost = cost + stepCost
                    priority = newCost + heuristic(successor, problem)
                    fringe.push((successor, actions + [action], newCost), priority)

    return []
```

### Q5: CornersProblem methods (getStartState, isGoalState, getSuccessors)  (file: `search/searchAgents.py`)
```python
    def getStartState(self):
        """
        Returns the start state (in your state space, not the full Pacman state
        space)
        """
        "*** YOUR CODE HERE ***"
        # State = (position, visitedCorners). visitedCorners is a sorted tuple so the
        # state is small and hashable. If Pacman starts on a corner, it counts as visited.
        visited = tuple(c for c in self.corners if c == self.startingPosition)
        return (self.startingPosition, visited)

    def isGoalState(self, state: Any):
        """
        Returns whether this search state is a goal state of the problem.
        """
        "*** YOUR CODE HERE ***"
        # Goal: all four corners have been visited
        position, visited = state
        return len(visited) == len(self.corners)

    def getSuccessors(self, state: Any):
        """
        Returns successor states, the actions they require, and a cost of 1.

         As noted in search.py:
            For a given state, this should return a list of triples, (successor,
            action, stepCost), where 'successor' is a successor to the current
            state, 'action' is the action required to get there, and 'stepCost'
            is the incremental cost of expanding to that successor
        """

        successors = []
        position, visited = state
        for action in [Directions.NORTH, Directions.SOUTH, Directions.EAST, Directions.WEST]:
            # Add a successor state to the successor list if the action is legal
            # Here's a code snippet for figuring out whether a new position hits a wall:
            #   x,y = currentPosition
            #   dx, dy = Actions.directionToVector(action)
            #   nextx, nexty = int(x + dx), int(y + dy)
            #   hitsWall = self.walls[nextx][nexty]

            "*** YOUR CODE HERE ***"
            x, y = position
            dx, dy = Actions.directionToVector(action)
            nextx, nexty = int(x + dx), int(y + dy)
            if not self.walls[nextx][nexty]:
                nextPosition = (nextx, nexty)
                nextVisited = visited
                # Stepping onto a new corner marks it visited
                if nextPosition in self.corners and nextPosition not in visited:
                    nextVisited = tuple(sorted(visited + (nextPosition,)))
                successors.append(((nextPosition, nextVisited), action, 1))

        self._expanded += 1 # DO NOT CHANGE
        return successors
```

## 4. Test
```bash
python autograder.py -q q3
python autograder.py -q q4
python autograder.py -q q5
```

## 5. Suggested commits (small steps, ideally on different days)
1. `Implement UCS with util.PriorityQueue (Q3)`
2. `Implement A* with g + h priority (Q4)`
3. `Define CornersProblem state as (position, visitedCorners) (Q5)`
4. `Implement CornersProblem successors and goal test (Q5)`

Then `git push -u origin <branch>` and open a Pull Request into `main`. Ask another member to review it.

## 6. Viva notes: be able to say these without reading
- UCS = BFS with a PriorityQueue keyed on g(n), the path cost so far. Optimal for non-negative step costs.
- A* = UCS with priority g(n) + h(n). With nullHeuristic (h = 0), A* is exactly UCS.
- Goal tested on POP: the first goal popped has the lowest cost (UCS) / lowest f with a consistent h (A*).
- Corners state = (position, visitedCorners tuple). Small and hashable so it can go in the expanded set; it holds no walls or GameState.
- visitedCorners is sorted so the same set of corners always gives the same tuple, which avoids duplicate states.
- If Pacman starts on a corner, that corner counts as visited in the start state.
