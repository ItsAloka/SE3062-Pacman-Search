# SE3062 Intelligent Systems — Search Algorithms in Pac-Man

Group assignment: implement DFS, BFS, UCS and A* (`search/search.py`) and the
Corners problem + heuristics (`search/searchAgents.py`).

## Setup

```bash
cd search
python -m venv .venv          # Python 3.9–3.11
.venv/Scripts/activate        # Windows (Git Bash: source .venv/Scripts/activate)
pip install numpy matplotlib
python pacman.py              # sanity check: game window opens
```

## Run the autograder

```bash
python autograder.py -q q1    # q1 … q7
python autograder.py --no-graphics
```

## Work split

See [PLAN.md](PLAN.md) for the full plan, timeline and Git workflow.

| Ref | Member | Questions | File |
|---|---|---|---|
| M1 | Warnakulasinhage S.N.A (lead) | Q1 DFS, Q2 BFS | search.py |
| M2 | Nawodya K.P.G.P | Q3 UCS, Q4 A*, Q5 CornersProblem | search.py, searchAgents.py |
| M3 | Fonseka W.P.L | Q6 cornersHeuristic | searchAgents.py |
| M4 | Seelarathna G.P.B | Q7 foodHeuristic | searchAgents.py |

## Rules
- Do NOT rename files, functions or classes (autograder imports by name).
- Use `util.Stack`, `util.Queue`, `util.PriorityQueue` — not Python built-ins.
- Small commits with clear messages, from your own account.
