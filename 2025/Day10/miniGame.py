import re
import sys
import tkinter as tk
from tkinter import ttk
from dataclasses import dataclass
from itertools import product
from typing import List, Tuple, Optional, Dict


@dataclass(frozen=True)
class Level:
    """One puzzle level parsed from the AoC-style line."""
    title: str
    targetPattern: str
    buttonWiring: List[Tuple[int, ...]]  # indices per button

    @property
    def lampCount(self) -> int:
        return len(self.targetPattern)


def parseLevelsFromText(text: str) -> List[Level]:
    """
    Parses AoC-style lines:
      [..##] (0,2) (1,3) {...}
    Returns one Level per non-empty line.
    """
    levels: List[Level] = []
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    for idx, line in enumerate(lines, start=1):
        m = re.search(r"\[([.#]+)\]", line)
        if not m:
            raise ValueError(f"Line {idx}: no target pattern found in brackets []")

        targetPattern = m.group(1)
        lampCount = len(targetPattern)

        buttonParts = re.findall(r"\(([^)]*)\)", line)
        if not buttonParts:
            raise ValueError(f"Line {idx}: no button definitions found in parentheses ()")

        wirings: List[Tuple[int, ...]] = []
        for part in buttonParts:
            part = part.strip()
            if part == "":
                wiring = tuple()
            else:
                nums = [int(x.strip()) for x in part.split(",") if x.strip() != ""]
                for n in nums:
                    if n < 0 or n >= lampCount:
                        raise ValueError(
                            f"Line {idx}: button index {n} out of range for lampCount={lampCount}"
                        )
                wiring = tuple(nums)
            wirings.append(wiring)

        levels.append(Level(title=f"Line {idx}", targetPattern=targetPattern, buttonWiring=wirings))

    return levels


def parseLevelsFromFile(path: str) -> List[Level]:
    with open(path, "r", encoding="utf-8") as f:
        return parseLevelsFromText(f.read())


def patternToMask(pattern: str) -> int:
    """Converts '.#' pattern into a bitmask (bit i = 1 means lamp i is ON)."""
    mask = 0
    for i, c in enumerate(pattern):
        if c == "#":
            mask |= (1 << i)
    return mask


def wiringToMask(wiring: Tuple[int, ...]) -> int:
    """Converts a wiring tuple into a toggle bitmask."""
    m = 0
    for i in wiring:
        m |= (1 << i)
    return m


def popcount(x: int) -> int:
    return x.bit_count()


def computeMinPossible(buttonMasks: List[int], targetMask: int) -> int:
    """
    Minimum number of buttons to press (parity / 0-1 per button).
    Uses brute force up to a safe threshold; falls back to meet-in-the-middle if larger.
    """
    k = len(buttonMasks)
    if k == 0:
        return 0 if targetMask == 0 else 0

    # Small k: brute force
    if k <= 24:
        best: Optional[int] = None
        for choice in range(1 << k):
            state = 0
            presses = 0
            c = choice
            i = 0
            while c:
                if c & 1:
                    state ^= buttonMasks[i]
                    presses += 1
                c >>= 1
                i += 1
            # handle remaining i if c became 0 early - no need
            if state == targetMask:
                if best is None or presses < best:
                    best = presses
                    if best == 0:
                        break
        return best if best is not None else 0

    # Larger k: meet-in-the-middle
    mid = k // 2
    left = buttonMasks[:mid]
    right = buttonMasks[mid:]

    def allStates(masks: List[int]) -> Dict[int, int]:
        """state -> min presses to reach that state."""
        states: Dict[int, int] = {0: 0}
        for mask in masks:
            newStates = dict(states)  # keep existing
            for st, p in states.items():
                st2 = st ^ mask
                p2 = p + 1
                old = newStates.get(st2)
                if old is None or p2 < old:
                    newStates[st2] = p2
            states = newStates
        return states

    leftStates = allStates(left)
    rightStates = allStates(right)

    best = None
    for stL, pL in leftStates.items():
        need = targetMask ^ stL
        pR = rightStates.get(need)
        if pR is None:
            continue
        total = pL + pR
        if best is None or total < best:
            best = total
            if best == 0:
                break

    return best if best is not None else 0


class LampPuzzleApp(tk.Tk):
    """Tkinter GUI for a toggle-lamps puzzle, levels loaded dynamically from input file."""

    def __init__(self, levels: List[Level]) -> None:
        super().__init__()
        self.title("AoC Lamps Puzzle")
        self.resizable(False, False)

        if not levels:
            raise ValueError("No levels loaded.")
        self.levels = levels

        # Game state
        self.currentLevelIndex: int = 0
        self.stateMask: int = 0
        self.pressCount: int = 0

        # Level-derived
        self.targetMask: int = 0
        self.buttonMasks: List[int] = []
        self.buttonWirings: List[Tuple[int, ...]] = []
        self.minPossible: int = 0

        # UI state
        self.hardModeVar = tk.BooleanVar(value=False)
        self.hoverMask: int = 0  # which lamps are highlighted by hover

        self._buildUi()
        self._loadLevel(0)

    def _buildUi(self) -> None:
        outer = ttk.Frame(self, padding=12)
        outer.grid(row=0, column=0, sticky="nsew")

        # Top/status
        top = ttk.Frame(outer)
        top.grid(row=0, column=0, sticky="ew")
        top.columnconfigure(0, weight=1)

        self.levelLabel = ttk.Label(top, text="Level", font=("Segoe UI", 12, "bold"))
        self.levelLabel.grid(row=0, column=0, sticky="w")

        self.statusLabel = ttk.Label(top, text="", font=("Segoe UI", 10))
        self.statusLabel.grid(row=1, column=0, sticky="w", pady=(4, 0))

        rightTop = ttk.Frame(top)
        rightTop.grid(row=0, column=1, rowspan=2, sticky="e")

        self.hardModeCheck = ttk.Checkbutton(
            rightTop,
            text="Hard mode (unlock only if presses == minimum)",
            variable=self.hardModeVar,
            command=self._updateStatusAndButtons,
        )
        self.hardModeCheck.grid(row=0, column=0, sticky="e")

        # Lamps
        lampsFrame = ttk.LabelFrame(outer, text="Indicator Lights", padding=10)
        lampsFrame.grid(row=1, column=0, sticky="ew", pady=(10, 0))

        self.lampsCanvas = tk.Canvas(lampsFrame, width=560, height=120, highlightthickness=0)
        self.lampsCanvas.grid(row=0, column=0, sticky="ew")

        # Buttons
        buttonsFrame = ttk.LabelFrame(outer, text="Wiring Buttons", padding=10)
        buttonsFrame.grid(row=2, column=0, sticky="ew", pady=(10, 0))
        buttonsFrame.columnconfigure(0, weight=1)

        self.buttonsContainer = ttk.Frame(buttonsFrame)
        self.buttonsContainer.grid(row=0, column=0, sticky="ew")

        # Bottom controls
        bottom = ttk.Frame(outer)
        bottom.grid(row=3, column=0, sticky="ew", pady=(10, 0))
        bottom.columnconfigure(0, weight=1)

        self.resetButton = ttk.Button(bottom, text="Reset Level", command=self._resetLevel)
        self.resetButton.grid(row=0, column=0, sticky="w")

        self.nextButton = ttk.Button(bottom, text="Next Level", command=self._nextLevel, state="disabled")
        self.nextButton.grid(row=0, column=1, sticky="e")

    def _loadLevel(self, levelIndex: int) -> None:
        self.currentLevelIndex = levelIndex
        level = self.levels[levelIndex]

        self.stateMask = 0
        self.pressCount = 0
        self.hoverMask = 0

        self.targetMask = patternToMask(level.targetPattern)
        self.buttonWirings = level.buttonWiring
        self.buttonMasks = [wiringToMask(w) for w in self.buttonWirings]
        self.minPossible = computeMinPossible(self.buttonMasks, self.targetMask)

        self.levelLabel.config(text=f"Level {levelIndex + 1}/{len(self.levels)} — {level.title}")

        self._rebuildWiringButtons()
        self._drawLamps()
        self._updateStatusAndButtons()

    def _resetLevel(self) -> None:
        self._loadLevel(self.currentLevelIndex)

    def _nextLevel(self) -> None:
        if self.currentLevelIndex + 1 < len(self.levels):
            self._loadLevel(self.currentLevelIndex + 1)
        else:
            self.levelLabel.config(text="All levels completed")
            self.statusLabel.config(text=f"Finished! Last run: {self.pressCount} presses.", foreground="")
            self.nextButton.config(state="disabled")

    def _isSolved(self) -> bool:
        return self.stateMask == self.targetMask

    def _isOverBudget(self) -> bool:
        return self.hardModeVar.get() and (self.pressCount > self.minPossible)

    def _meetsUnlockCondition(self) -> bool:
        if not self._isSolved():
            return False
        if self.hardModeVar.get():
            return self.pressCount == self.minPossible
        return True

    def _updateStatusAndButtons(self) -> None:
        solved = self._isSolved()
        overBudget = self._isOverBudget()

        # Text
        if solved and self.hardModeVar.get() and self.pressCount != self.minPossible:
            text = f"Presses: {self.pressCount}    Minimum: {self.minPossible}    Solved, but not optimal."
        elif solved:
            text = f"Presses: {self.pressCount}    Minimum: {self.minPossible}    Solved!"
        elif overBudget:
            text = f"Presses: {self.pressCount}    Minimum: {self.minPossible}    Over budget — reset required."
        else:
            text = f"Presses: {self.pressCount}    Minimum: {self.minPossible}    Not solved yet."

        # Color
        if solved:
            self.statusLabel.config(foreground="green")
        elif overBudget:
            self.statusLabel.config(foreground="red")
        else:
            self.statusLabel.config(foreground="")

        self.statusLabel.config(text=text)

        # Next button
        isLast = self.currentLevelIndex == len(self.levels) - 1
        if self._meetsUnlockCondition() and not isLast:
            self.nextButton.config(state="normal")
        else:
            self.nextButton.config(state="disabled")

    def _pressButton(self, btnIndex: int) -> None:
        self.stateMask ^= self.buttonMasks[btnIndex]
        self.pressCount += 1
        self._drawLamps()
        self._updateStatusAndButtons()

    def _setHoverMask(self, mask: int) -> None:
        self.hoverMask = mask
        self._drawLamps()

    def _rebuildWiringButtons(self) -> None:
        for child in self.buttonsContainer.winfo_children():
            child.destroy()

        # 3-column layout
        cols = 3
        for c in range(cols):
            self.buttonsContainer.columnconfigure(c, weight=1)

        for i, wiring in enumerate(self.buttonWirings):
            label = f"({','.join(map(str, wiring))})"
            btn = ttk.Button(
                self.buttonsContainer,
                text=label,
                width=18,  # smaller
                command=lambda idx=i: self._pressButton(idx),
            )
            r = i // cols
            c = i % cols
            btn.grid(row=r, column=c, sticky="ew", padx=4, pady=4)

            hoverMask = self.buttonMasks[i]
            btn.bind("<Enter>", lambda _e, m=hoverMask: self._setHoverMask(m))
            btn.bind("<Leave>", lambda _e: self._setHoverMask(0))

    def _drawLamps(self) -> None:
        self.lampsCanvas.delete("all")

        level = self.levels[self.currentLevelIndex]
        n = level.lampCount

        padX = 18
        padY = 18
        spacing = 55
        r = 16

        # Lamps row
        for i in range(n):
            cx = padX + i * spacing + r
            cy = padY + r

            # outer ring
            self.lampsCanvas.create_oval(cx - r - 2, cy - r - 2, cx + r + 2, cy + r + 2)

            # fill
            isOn = bool(self.stateMask & (1 << i))
            fill = "#ffd54a" if isOn else "#3a3a3a"
            self.lampsCanvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill=fill, outline="")

            # hover outline
            if self.hoverMask & (1 << i):
                self.lampsCanvas.create_oval(
                    cx - r - 6, cy - r - 6, cx + r + 6, cy + r + 6,
                    outline="#4aa3ff", width=3
                )

            # index label
            self.lampsCanvas.create_text(cx, cy + r + 18, text=str(i), font=("Segoe UI", 9))

        # Target preview (kept here, not in header/status)
        previewY = 100
        self.lampsCanvas.create_text(10, previewY, text="Target:", anchor="w", font=("Segoe UI", 10, "bold"))
        for i in range(n):
            cx = 80 + i * 24
            cy = previewY
            rr = 7
            isOn = bool(self.targetMask & (1 << i))
            fill = "#ffd54a" if isOn else "#3a3a3a"
            self.lampsCanvas.create_oval(cx - rr, cy - rr, cx + rr, cy + rr, fill=fill, outline="")


def main() -> None:
    devMode = False
    # devMode = True
    if devMode:
        path = "example.txt"
    else:
        path = "input.txt"
    levels = parseLevelsFromFile(path)

    app = LampPuzzleApp(levels)
    app.mainloop()


if __name__ == "__main__":
    main()
