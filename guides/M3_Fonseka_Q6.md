# Handoff: Fonseka W.P.L: Q6 cornersHeuristic

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
git checkout -b q6-corners-heuristic
```

## 3. Code to add
Replace the `"*** YOUR CODE HERE ***"` / `util.raiseNotDefined()` stub of each function below with this version. Do **not** rename anything.

### Q6: cornersHeuristic (also add `import itertools` under `import util` at the top)  (file: `search/searchAgents.py`)
```python
def cornersHeuristic(state: Any, problem: CornersProblem):
    """
    A heuristic for the CornersProblem that you defined.

      state:   The current search state
               (a data structure you chose in your search problem)

      problem: The CornersProblem instance for this layout.

    This function should always return a number that is a lower bound on the
    shortest path from the state to a goal of the problem; i.e.  it should be
    admissible (as well as consistent).
    """
    corners = problem.corners # These are the corner coordinates
    walls = problem.walls # These are the walls of the maze, as a Grid (game.py)

    "*** YOUR CODE HERE ***"
    # Relaxed problem: ignore walls. The heuristic is the length of the shortest
    # tour that starts at Pacman's position and visits every unvisited corner,
    # measuring each leg with Manhattan distance.
    #   Admissible: Manhattan distance never exceeds the real maze distance, so every
    #   relaxed tour is no longer than the real tour in the same order; taking the
    #   minimum over all orders gives a lower bound on the true remaining cost.
    #   Consistent: one move changes Pacman's distance to the first corner by at
    #   most 1 (the step cost), so h drops by at most 1 per step.
    position, visited = state
    unvisited = [c for c in corners if c not in visited]
    if not unvisited:
        return 0

    best = None
    for order in itertools.permutations(unvisited):  # at most 4! = 24 orders
        total = 0
        current = position
        for corner in order:
            total += util.manhattanDistance(current, corner)
            current = corner
        if best is None or total < best:
            best = total
    return best
```

## 4. Test
```bash
python autograder.py -q q6
```

## 5. Suggested commits (small steps, ideally on different days)
1. `Add itertools import for corners heuristic`
2. `Implement corners heuristic as shortest Manhattan tour of unvisited corners (Q6)`
3. `Document admissibility and consistency of corners heuristic`

Then `git push -u origin <branch>` and open a Pull Request into `main`. Ask another member to review it.

## 6. Viva notes: be able to say these without reading
- Relaxed problem: ignore the walls. h = the shortest tour from Pacman through ALL unvisited corners, using Manhattan distance for each leg. We try every order (at most 4! = 24).
- Admissible: Manhattan distance <= real maze distance for every leg, so the relaxed tour in any order is <= the real tour in that order. The minimum over all orders is therefore <= the true optimal cost.
- Consistent: one step (cost 1) changes the distance to the first corner of a tour by at most 1, so h(n) <= 1 + h(n'). Reaching a corner removes it from the list, and h never goes up by more than it should.
- h = 0 at the goal (no unvisited corners) and is never negative.
- Result: 741 nodes expanded on mediumCorners (target <= 1200 for 8/8), path cost 106 (optimal).
- Why not just the farthest corner? It is admissible too, but looser, so it expands more nodes. The tour sum is tighter.
