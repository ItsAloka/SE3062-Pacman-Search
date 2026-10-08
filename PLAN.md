# Team Plan: Search Algorithms in Pac-Man (SE3062)

## 1. Work split

Each member owns roughly the same amount of **effort**, though not the same number
of autograder marks. Q1–Q4 are short once the shared search loop exists. Q6 and Q7
are the hardest parts because their heuristics must be admissible and still
expand few nodes.

| Ref | Member | Code owned | File | Autograder marks | Report sections |
|---|---|---|---|---|---|
| M1 | Warnakulasinhage S.N.A (lead) | Q1 DFS, Q2 BFS: the shared graph-search loop | `search.py` | 8 | Q1–Q2, repo link, Git evidence, contribution table, final assembly and submission |
| M2 | Nawodya K.P.G.P | Q3 UCS, Q4 A*, Q5 CornersProblem | `search.py`, `searchAgents.py` | 16 | Q3–Q5 |
| M3 | Fonseka W.P.L | Q6 `cornersHeuristic` | `searchAgents.py` | 8 | Q6, including the admissibility/consistency argument |
| M4 | Seelarathna G.P.B | Q7 `foodHeuristic` | `searchAgents.py` | 8 | Q7, including the admissibility/consistency argument |

**Everyone** must:
- review at least one pull request from each other member, which also shows up as Git evidence
- be able to explain **all** of Q1–Q7 in the viva, since the viva is worth 40 of 100 marks per person
- record their own AI prompts, if they used any, for the AI usage declaration

## 2. Dependencies (who waits for whom)

```
M1: Q1 DFS ──► Q2 BFS ──┬──► M2: Q3 UCS ──► Q4 A* ──┬──► M3: Q6 corners heuristic
                        │                          │        ▲
                        └──► M2: Q5 CornersProblem ─┼────────┘
                                                   └──► M4: Q7 food heuristic
```

- **M1 is the critical path.** Q1 and Q2 should land in `main` within the first 2 days.
- Until A* exists, **M3 and M4 do not need to wait**. They can design their heuristic
  on paper (what it measures, and why it never overestimates) and test their ideas
  against small layouts by hand.
- M3 needs M2's Q5 state format, so **M2 should share the state shape early**, for
  example `(position, visitedCornersTuple)`.

## 3. Timeline (adjust once the deadline is confirmed)

| Phase | Goal | Done when |
|---|---|---|
| Day 1 | Everyone clones the repo, creates the venv, `python pacman.py` works | Each member has made one small commit, e.g. adding their name to the README |
| Days 1–2 | M1: Q1 + Q2 merged | `autograder.py -q q1` and `-q q2` pass |
| Days 2–4 | M2: Q3 + Q4 merged; Q5 started | q3 and q4 pass |
| Days 3–6 | M2: Q5 merged. M3/M4: heuristics implemented and tuned | q5 passes; q6 ≤ 1200 nodes; q7 ≤ 9000 nodes |
| Days 6–7 | Full run of `autograder.py`; screenshots; report drafts | Each owner's report section is written |
| Days 7–8 | **Viva prep session**: each owner explains their part to the other three | Everyone can answer the questions in section 6 |
| Final day | M1 assembles the report PDF and the code ZIP, then submits | `Group_XX_Report.pdf` + `Group_XX_Code.zip` uploaded |

## 4. Git workflow

1. Clone once: `git clone <repo-url>`
2. Create one branch per task: `git checkout -b q6-corners-heuristic`
3. Commit **small and often**, with clear messages:
   - good: `Implement BFS with util.Queue and visited set`
   - bad: `update`, `final`, `fix`
4. Before you push, run `git pull origin main` to stay current.
5. `git push -u origin <branch>`, then open a **pull request**. One other member reviews it and merges.
6. Spread commits over the whole period. Many commits on the last night score poorly.
7. Only `search.py` and `searchAgents.py` should change. Do not rename functions, classes or files.

## 5. Report checklist (10 marks)

For each of Q1–Q7, written by the owner:
- [ ] the code block that was edited or added
- [ ] an autograder screenshot for that question
- [ ] an explanation of at most 200 words: the logic, data structure, and heuristic design

End of the report (assembled by M1):
- [ ] public Git repository link
- [ ] commit-history and contribution-graph screenshots
- [ ] contribution table: names, student IDs, questions owned
- [ ] AI usage declaration with exact prompts, or "No AI tools were utilized."

Submission: `Group_XX_Report.pdf` and `Group_XX_Code.zip`, which contains **only**
`search.py` and `searchAgents.py`.

## 6. Viva prep: everyone must be able to answer

- How do DFS, BFS, UCS and A* differ? (Only the fringe changes: Stack, Queue, or PriorityQueue keyed on g or g+h.)
- Which of them are complete and which are optimal, and why? Why is DFS not optimal?
- Why use graph search with an expanded set? What goes wrong without it?
- Why is the goal checked when a node is **popped**, not when it is pushed?
- When does A* behave like UCS? (When h = 0.)
- What do admissible and consistent mean? Why does A* graph search need consistency to stay optimal?
- What is the CornersProblem state, and why must it be small and hashable?
- How does our corners heuristic work, and why does it never overestimate?
- How does our food heuristic work, and why does it never overestimate?
