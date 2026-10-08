# launcher.py
# -----------
# Demo UI for the SE3062 Pac-Man search assignment (not part of the submission).
# Pick a question, watch Pac-Man solve it in the game window, or run its autograder.
#
#   python launcher.py

import subprocess
import sys
import threading
import tkinter as tk
from tkinter import ttk, scrolledtext

# question -> (description, pacman.py arguments, autograder question)
DEMOS = {
    "Q1 - Depth First Search": (
        "DFS with util.Stack (LIFO). Goes deep first. Complete, NOT optimal.",
        ["-l", "mediumMaze", "-p", "SearchAgent", "-a", "fn=dfs"], "q1"),
    "Q2 - Breadth First Search": (
        "BFS with util.Queue (FIFO). Shallowest first. Optimal when every step costs 1.",
        ["-l", "mediumMaze", "-p", "SearchAgent", "-a", "fn=bfs"], "q2"),
    "Q3 - Uniform Cost Search": (
        "UCS with util.PriorityQueue keyed on g(n). Here, food is cheap and ghosts are expensive.",
        ["-l", "mediumDottedMaze", "-p", "StayEastSearchAgent"], "q3"),
    "Q4 - A* Search": (
        "A* with priority g(n) + h(n), using the Manhattan heuristic on bigMaze.",
        ["-l", "bigMaze", "-z", ".5", "-p", "SearchAgent", "-a", "fn=astar,heuristic=manhattanHeuristic"], "q4"),
    "Q5 - Corners Problem (BFS)": (
        "State = (position, visitedCorners). BFS finds the shortest path through all 4 corners.",
        ["-l", "mediumCorners", "-p", "SearchAgent", "-a", "fn=bfs,prob=CornersProblem"], "q5"),
    "Q6 - Corners Heuristic (A*)": (
        "Shortest Manhattan tour of the unvisited corners. Admissible, consistent; 741 nodes (target <= 1200).",
        ["-l", "mediumCorners", "-p", "AStarCornersAgent", "-z", "0.5"], "q6"),
    "Q7 - Food Heuristic (A*)": (
        "Maze distance to the farthest food dot. Admissible, consistent; 4137 nodes (target <= 9000).",
        ["-l", "trickySearch", "-p", "AStarFoodSearchAgent"], "q7"),
}


class Launcher(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("SE3062 - Pac-Man Search Demo")
        self.geometry("820x560")
        self.minsize(640, 420)

        top = ttk.Frame(self, padding=12)
        top.pack(fill="x")

        ttk.Label(top, text="Question:").grid(row=0, column=0, sticky="w")
        self.choice = tk.StringVar(value=list(DEMOS)[0])
        box = ttk.Combobox(top, textvariable=self.choice, values=list(DEMOS),
                           state="readonly", width=40)
        box.grid(row=0, column=1, sticky="w", padx=8)
        box.bind("<<ComboboxSelected>>", lambda e: self.showDescription())

        self.speed = tk.StringVar(value="0.05")
        ttk.Label(top, text="Frame time (s):").grid(row=0, column=2, sticky="e", padx=(16, 4))
        ttk.Entry(top, textvariable=self.speed, width=6).grid(row=0, column=3, sticky="w")

        self.description = ttk.Label(top, text="", wraplength=760, foreground="#06146E")
        self.description.grid(row=1, column=0, columnspan=4, sticky="w", pady=(10, 4))

        buttons = ttk.Frame(self, padding=(12, 0))
        buttons.pack(fill="x")
        ttk.Button(buttons, text="▶  Watch Pac-Man", command=self.runGame).pack(side="left")
        ttk.Button(buttons, text="✔  Autograder (this question)", command=self.runGrader).pack(side="left", padx=8)
        ttk.Button(buttons, text="✔✔  Autograder (all)", command=lambda: self.runGrader(all=True)).pack(side="left")
        ttk.Button(buttons, text="Clear", command=lambda: self.output.delete("1.0", "end")).pack(side="right")

        self.output = scrolledtext.ScrolledText(self, font=("Consolas", 10), wrap="word")
        self.output.pack(fill="both", expand=True, padx=12, pady=12)

        self.showDescription()

    def showDescription(self):
        self.description.config(text=DEMOS[self.choice.get()][0])

    def log(self, text):
        self.output.insert("end", text)
        self.output.see("end")

    def runAsync(self, args):
        self.log("\n$ python " + " ".join(args) + "\n")

        def worker():
            proc = subprocess.Popen([sys.executable] + args, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT, text=True)
            for line in proc.stdout:
                self.after(0, self.log, line)
            proc.wait()

        threading.Thread(target=worker, daemon=True).start()

    def runGame(self):
        _, gameArgs, _ = DEMOS[self.choice.get()]
        self.runAsync(["pacman.py"] + gameArgs + ["--frameTime", self.speed.get()])

    def runGrader(self, all=False):
        _, _, question = DEMOS[self.choice.get()]
        args = ["autograder.py", "--no-graphics"]
        if not all:
            args += ["-q", question]
        self.runAsync(args)


if __name__ == "__main__":
    Launcher().mainloop()
