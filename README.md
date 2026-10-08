# SE3062 Intelligent Systems — Search Algorithms in Pac-Man

Group assignment: implement DFS, BFS, UCS and A* (`search/search.py`) and the
Corners problem + heuristics (`search/searchAgents.py`).

> **This is the `full-project` reference branch.** It contains the complete,
> working solution for Q1–Q7. **Do not merge it into `main`.** Each member writes
> their own part on their own branch while looking at this one. The branch will
> be deleted afterwards.

## Status

| Question | Algorithm | Autograder | Result |
|---|---|---|---|
| Q1 | Depth First Search | ✅ pass | mediumMaze: cost 130, 146 nodes |
| Q2 | Breadth First Search | ✅ pass | mediumMaze: cost 68 (optimal), 269 nodes |
| Q3 | Uniform Cost Search | ✅ pass | |
| Q4 | A* Search | ✅ pass | |
| Q5 | Corners Problem | ✅ pass | |
| Q6 | Corners Heuristic | ✅ pass | mediumCorners: **741 nodes** (target ≤ 1200) |
| Q7 | Food Heuristic | ✅ pass | trickySearch: **4137 nodes** (target ≤ 9000) |

Q8 also appears in the autograder output. It is not part of this assignment, so ignore it.

## Files changed

Only these two files are part of the assignment and the submission ZIP:

| File | Function(s) | Q | Owner |
|---|---|---|---|
| `search/search.py` | `depthFirstSearch` | Q1 | M1 |
| | `breadthFirstSearch` | Q2 | M1 |
| | `uniformCostSearch` | Q3 | M2 |
| | `aStarSearch` | Q4 | M2 |
| `search/searchAgents.py` | `CornersProblem.getStartState / isGoalState / getSuccessors` | Q5 | M2 |
| | `cornersHeuristic` (+ `import itertools`) | Q6 | M3 |
| | `foodHeuristic` + `_bfsDistancesFrom` | Q7 | M4 |

Extras on this branch only, **not submitted**: `search/launcher.py` (the demo UI),
`launch.txt` (the run commands) and `guides/` (one guide per member).

## Setup

```bash
cd search
python -m venv .venv          # Python 3.9–3.11
source .venv/Scripts/activate # Git Bash   (PowerShell: .venv\Scripts\activate)
pip install numpy matplotlib
python pacman.py              # sanity check: game window opens
```

## Run it

```bash
cd search && python launcher.py      # demo UI: pick a question, watch Pac-Man, run the autograder
python autograder.py --no-graphics   # all questions (from inside search/)
python autograder.py -q q6           # one question
```

See [launch.txt](launch.txt) for every demo command.

## Work split

See [PLAN.md](PLAN.md) for the full plan, timeline and Git workflow. See [guides/](guides/) for each member's guide.

| Ref | Member | Questions | Type of work | File |
|---|---|---|---|---|
| M1 | Warnakulasinhage S.N.A (lead) | Q1 DFS, Q2 BFS | Search algorithms (Stack / Queue) | search.py |
| M2 | Nawodya K.P.G.P | Q3 UCS, Q4 A*, Q5 CornersProblem | Search algorithms (PriorityQueue) + problem design | search.py, searchAgents.py |
| M3 | Fonseka W.P.L | Q6 cornersHeuristic | Admissible heuristic | searchAgents.py |
| M4 | Seelarathna G.P.B | Q7 foodHeuristic | Admissible heuristic | searchAgents.py |

**Merge order into `main`:** M1 → M2 → M3 / M4. Each part builds on the previous one.

## Rules
- Do NOT rename files, functions or classes (autograder imports by name).
- Use `util.Stack`, `util.Queue`, `util.PriorityQueue` — not Python built-ins.
- Small commits with clear messages, from your own account.
- Submission ZIP = `search.py` + `searchAgents.py` only.
