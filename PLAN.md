# Team Plan: Search Algorithms in Pac-Man

**Module:** SE3062 Intelligent Systems · **Group size:** 4 · **Weight:** 10% of final grade
**Deadline:** _TBD (fill in)_ · **Repo lead:** M1

---

## 0. TL;DR

- We edit **only two files**: `search/search.py` and `search/searchAgents.py`.
- Each member owns one part (section 2), works on **their own branch**, and opens a **pull request** into `main`.
- **Commit small and often, from your own GitHub account.** Git is marked individually (10 marks).
- **Everyone must understand all of Q1–Q7.** The viva is individual and worth 40 marks.
- If you use AI, **save your exact prompts**. The report must declare them.

---

## 1. How we are marked

| Component | Marks | Group or individual | What gets us full marks |
|---|---|---|---|
| Autograder Q1–Q7 | 40 | Group | Every question passes, and the node-count targets are met for Q6/Q7 |
| Report (PDF) | 10 | Group | Every section in section 6 is present, clear and well formatted |
| Git contribution | 10 | **Individual** | Frequent, meaningful commits spread over the whole period |
| Viva: algorithms | 20 | **Individual** | Explain DFS/BFS/UCS/A*, fringes and optimality instantly |
| Viva: our code | 20 | **Individual** | Explain any part of *our* code and defend the heuristics |

**Autograder breakdown:** Q1–Q4 = 4 marks each · Q5, Q6, Q7 = 8 marks each.

> The downloaded autograder also prints a **Q8** and uses its own "/3" scale.
> **Ignore Q8.** The lecturer converts the results to the marks above.

---

## 2. Who does what

| Ref | Member | Owns | Branch | Report sections |
|---|---|---|---|---|
| **M1** | Warnakulasinhage S.N.A (**lead**) | Q1 DFS, Q2 BFS | `q1-q2-dfs-bfs` | Q1, Q2 + repo link, Git evidence, contribution table, final assembly |
| **M2** | Nawodya K.P.G.P | Q3 UCS, Q4 A*, Q5 CornersProblem | `q3-q4-ucs-astar`, `q5-corners-problem` | Q3, Q4, Q5 |
| **M3** | Fonseka W.P.L | Q6 `cornersHeuristic` | `q6-corners-heuristic` | Q6 + admissibility argument |
| **M4** | Seelarathna G.P.B | Q7 `foodHeuristic` | `q7-food-heuristic` | Q7 + admissibility argument + AI declaration |

**Why this split is fair:** it balances effort rather than marks.
- Q3 and Q4 are small once M1's search loop exists, so M2 also takes Q5.
- Q6 and Q7 are the hardest tasks. Each needs a full person to design, test and tune a heuristic.
- M1 carries the coordination, repo and report work.

### Everyone also

- [ ] Reviews **at least one PR from each other member**: read it, run it, comment, approve.
- [ ] Writes their own report sections (section 6) with screenshots.
- [ ] Attends the viva prep session (section 7).
- [ ] Keeps a note of any AI prompts used.

---

## 3. Task cards

### M1: Q1 DFS and Q2 BFS (`search.py`)

**Goal:** implement `depthFirstSearch` and `breadthFirstSearch` as **graph search** (never expand the same state twice).

**Approach:** both use the same loop. Only the fringe changes.
1. Push `(startState, [])` onto the fringe. The list holds the actions taken so far.
2. Loop: pop a node. If it is a goal, return its actions.
3. If the state is not in `expanded`, add it, then push every successor with `actions + [action]`.
4. If the fringe empties, return `[]`.

- DFS uses `util.Stack()`. BFS uses `util.Queue()`.

**Test:**
```bash
python autograder.py -q q1
python autograder.py -q q2
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
```

**Done when:** q1 and q2 pass, and the PR is merged **by day 2**. Everyone else depends on this.

**Suggested commits:** `Implement DFS graph search with util.Stack` → `Implement BFS with util.Queue` → `Refactor shared search loop into helper` (optional) → `Add comments explaining fringe behaviour`.

---

### M2: Q3 UCS, Q4 A* (`search.py`) and Q5 CornersProblem (`searchAgents.py`)

**Q3, UCS:** use the same loop with `util.PriorityQueue()`. Store `(state, actions, g)` and push with priority `g` (total path cost so far, from `getSuccessors`).

**Q4, A\*:** like UCS, but the priority is `g + heuristic(nextState, problem)`.

**Q5, CornersProblem:**
- Fill in `getStartState`, `isGoalState` and `getSuccessors`.
- State = `(position, visitedCorners)`, where `visitedCorners` is a **tuple** (hashable) of the corners reached so far.
- **Never** put the wall grid or the GameState in the state.
- **Share the final state format with M3 early.** Q6 depends on it.

**Test:**
```bash
python autograder.py -q q3
python autograder.py -q q4
python autograder.py -q q5
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
python pacman.py -l mediumCorners -p SearchAgent -a fn=bfs,prob=CornersProblem
```

**Done when:** q3, q4 and q5 pass, Q3/Q4 are merged **by day 4**, and Q5 is merged **by day 5**.

**Suggested commits:** `Implement UCS with util.PriorityQueue` → `Implement A* using g + h priority` → `Define CornersProblem state as (position, visitedCorners)` → `Implement CornersProblem getSuccessors` → `Implement CornersProblem goal test`.

---

### M3: Q6 cornersHeuristic (`searchAgents.py`)

**Goal:** an admissible, consistent heuristic for the corners problem.
- It must never be negative, and must return `0` at a goal state.

**Target on mediumCorners:**

| Nodes expanded | Marks |
|---|---|
| ≤ 1200 | **8/8** |
| ≤ 1600 | 6/8 |
| ≤ 2000 | 4/8 |
| > 2000 | 0/8 |

**A non-optimal path on any test means 0/8.**

**Things to explore:**
- Manhattan distance to the farthest unvisited corner, which is a start.
- Then something tighter: the cost of visiting **all** remaining corners in the best order, using Manhattan distances, which ignores walls and so never overestimates.
- Compare node counts as you go.

**Can start immediately:** design the heuristic on paper and write the admissibility argument while M2 builds Q5.

**Test:**
```bash
python autograder.py -q q6
python pacman.py -l mediumCorners -p AStarCornersAgent -z 0.5
```

**Done when:** q6 passes with ≤ 1200 nodes, merged **by day 6**.

**Suggested commits:** `Add basic farthest-corner Manhattan heuristic` → `Improve corners heuristic: ordered tour of remaining corners` → `Document admissibility reasoning in comments`.

---

### M4: Q7 foodHeuristic (`searchAgents.py`)

**Goal:** an admissible, consistent heuristic for eating all the food.
- State = `(position, foodGrid)`. Use `foodGrid.asList()` to list the remaining dots.

**Target on trickySearch:**

| Nodes expanded | Marks |
|---|---|
| ≤ 9000 | **8/8** |
| ≤ 12000 | 6/8 |
| ≤ 15000 | 4/8 |
| > 15000 | 2/8 |

**Things to explore:**
- Distance to the farthest food dot, first with Manhattan distance, then with the **real maze distance** (`mazeDistance(...)` is already provided).
- Cache distances in `problem.heuristicInfo` so they are not recomputed. This matters for speed.

**Can start immediately:** `FoodSearchProblem` already exists. Only A* (M2) is needed to run the autograder, and the design work can start now.

**Test:**
```bash
python autograder.py -q q7
python pacman.py -l trickySearch -p AStarFoodSearchAgent
```

**Done when:** q7 passes with ≤ 9000 nodes, merged **by day 6**.

**Suggested commits:** `Add Manhattan farthest-food heuristic` → `Use cached maze distance in food heuristic` → `Document admissibility reasoning in comments`.

---

## 4. Dependencies and timeline

```
M1  Q1 DFS ─► Q2 BFS ─┬─► M2  Q3 UCS ─► Q4 A* ─┬─► M3  Q6 corners heuristic
                      │                        │        ▲
                      └─► M2  Q5 CornersProblem ┼────────┘
                                               └─► M4  Q7 food heuristic
```

| Day | M1 | M2 | M3 | M4 |
|---|---|---|---|---|
| 1 | Set up repo, push scaffold, Q1 DFS | Setup, first commit, read `util.py` | Setup, first commit, design heuristic on paper | Setup, first commit, design heuristic on paper |
| 2 | **Q2 BFS → PR merged** | Start Q3 on top of M1's loop | Write admissibility argument | Write admissibility argument |
| 3–4 | Review PRs, start report template | **Q3 + Q4 → PR merged** | Implement against M2's state format | Implement Q7 (needs A*) |
| 5 | Q1/Q2 report sections + screenshots | **Q5 → PR merged** | Tune for ≤ 1200 nodes | Tune for ≤ 9000 nodes |
| 6 | Full autograder run | Q3–Q5 report sections | **Q6 → PR merged** | **Q7 → PR merged** |
| 7 | **Viva prep session (all)** | 〃 | 〃 | 〃 |
| 8 | Assemble PDF + ZIP, final check, **submit** | Proofread | Proofread | Proofread |

**If someone is blocked for more than a day, say so in the group chat.** Don't wait silently.

---

## 5. Setup and Git workflow

### First-time setup (everyone, Windows)
```bash
git clone <REPO-URL>
cd CampusIaAssignment/search
python -m venv .venv
.venv\Scripts\activate          # Git Bash: source .venv/Scripts/activate
pip install numpy matplotlib
python pacman.py                # a game window should open
python autograder.py --no-graphics
```

### Every working session
```bash
git checkout main
git pull origin main                  # get the latest work
git checkout -b <your-branch>         # first time only; afterwards: git checkout <your-branch>
# ... edit, test ...
git add search/search.py              # or search/searchAgents.py
git commit -m "Implement BFS with util.Queue"
git push -u origin <your-branch>
```
Then open a **Pull Request** on GitHub. Another member reviews it and merges it.

### Rules
- ✅ Small commits with descriptive messages, spread over many days
- ✅ Commit from **your own** account, with your git `user.name` / `user.email` set
- ✅ Use `util.Stack`, `util.Queue`, `util.PriorityQueue`
- ❌ Don't rename any file, function or class. The autograder imports them by name, and a rename means 0 for that question.
- ❌ Don't push straight to `main`, and don't force-push
- ❌ No commit messages like `update`, `fix` or `final`

---

## 6. Report: who writes what

**For each question Q1–Q7 (written by its owner):**
1. The code block we edited or added
2. A screenshot of that question's autograder output
3. An explanation of **at most 200 words**: the logic, the data structure, and (for Q6/Q7) the heuristic design and why it is admissible

**End of the report (M1 assembles; M4 collects the AI declarations):**
- [ ] Public Git repository link
- [ ] Screenshots of the commit history and contributors graph
- [ ] Contribution table: name, **student ID**, questions owned
- [ ] AI usage declaration: tool name and **exact prompts**, or "No AI tools were utilized."

| Ref | Name | Student ID | Contribution |
|---|---|---|---|
| M1 | Warnakulasinhage S.N.A | _(report only)_ | Q1, Q2, repo, report assembly |
| M2 | Nawodya K.P.G.P | _(report only)_ | Q3, Q4, Q5 |
| M3 | Fonseka W.P.L | _(report only)_ | Q6 |
| M4 | Seelarathna G.P.B | _(report only)_ | Q7, AI declaration |

> Student IDs go **only in the PDF**, not in this public repo.

### Submission (M1, once per group)
- `Group_XX_Report.pdf`
- `Group_XX_Code.zip` containing **only** `search.py` and `searchAgents.py`

---

## 7. Viva preparation

**The format:** a strict 6 minutes for the whole team, with rapid-fire questions to each person.
**You can be asked about any question, not just your own.**

**Prep session (day 7):** each owner spends 10 minutes walking the others through their code. Then everyone quizzes each other with these questions:

**Algorithms**
- [ ] How do DFS, BFS, UCS and A* differ? *(The fringe: Stack / Queue / PQ by g / PQ by g+h.)*
- [ ] Which are complete? Which are optimal, and under what conditions?
- [ ] Why is DFS not optimal? Why is BFS optimal only when every step costs the same?
- [ ] Why use graph search (an expanded set)? What happens without it?
- [ ] Why do we test for the goal when a node is **popped**, not when it is pushed?
- [ ] When does A* become UCS? *(When h = 0.)* When does it become greedy search?

**Heuristics**
- [ ] What do *admissible* and *consistent* mean? Give the definitions.
- [ ] Why does A* graph search need consistency to stay optimal?
- [ ] Explain our corners heuristic, and prove that it never overestimates.
- [ ] Explain our food heuristic, and prove that it never overestimates.
- [ ] Why does a tighter heuristic expand fewer nodes?

**Our code**
- [ ] What is the CornersProblem state, and why must it be small and hashable?
- [ ] Where in our code is the expanded set, and where is the path stored?
- [ ] What does `getSuccessors` return?

---

## 8. Definition of done (final check before submitting)

- [ ] `python autograder.py --no-graphics` → Q1–Q7 all pass
- [ ] Q6 ≤ 1200 nodes, Q7 ≤ 9000 nodes
- [ ] All PRs merged; `main` is the final version
- [ ] Every member has commits on several different days
- [ ] Report has every section in section 6 and is exported to PDF
- [ ] ZIP contains only the two `.py` files
- [ ] Every member has done the viva prep checklist
