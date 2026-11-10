import re
from dataclasses import dataclass
from typing import List, Tuple, Dict, Optional
import time

@dataclass(frozen=True)
class Level:
    targetPattern: str
    buttonWirings: List[Tuple[int, ...]]


def parseLevelsFromFile(filePath: str) -> List[Level]:
    with open(filePath, "r", encoding="utf-8") as f:
        text = f.read()

    levels: List[Level] = []
    for lineNo, line in enumerate(text.splitlines(), start=1):
        line = line.strip()
        if not line:
            continue

        m = re.search(r"\[([.#]+)\]", line)
        if not m:
            raise ValueError(f"Line {lineNo}: missing [pattern]")
        targetPattern = m.group(1)
        lampCount = len(targetPattern)

        buttonParts = re.findall(r"\(([^)]*)\)", line)
        if not buttonParts:
            raise ValueError(f"Line {lineNo}: missing (buttons)")

        buttonWirings: List[Tuple[int, ...]] = []
        for part in buttonParts:
            part = part.strip()
            if part == "":
                wiring = tuple()
            else:
                nums = tuple(int(x.strip()) for x in part.split(",") if x.strip() != "")
                for n in nums:
                    if n < 0 or n >= lampCount:
                        raise ValueError(f"Line {lineNo}: index {n} out of range 0..{lampCount-1}")
                wiring = nums
            buttonWirings.append(wiring)

        levels.append(Level(targetPattern=targetPattern, buttonWirings=buttonWirings))

    return levels


def patternToMask(pattern: str) -> int:
    mask = 0
    for i, c in enumerate(pattern):
        if c == "#":
            mask |= (1 << i)
    return mask


def wiringToMask(wiring: Tuple[int, ...]) -> int:
    m = 0
    for i in wiring:
        m |= (1 << i)
    return m


def minPressesBruteforce(buttonMasks: List[int], targetMask: int) -> int:
    k = len(buttonMasks)
    best: Optional[int] = None

    for choice in range(1 << k):
        state = 0
        presses = 0
        x = choice
        i = 0
        while x:
            if x & 1:
                state ^= buttonMasks[i]
                presses += 1
            x >>= 1
            i += 1

        # if x becomes 0 early, remaining bits are 0 anyway
        if state == targetMask:
            if best is None or presses < best:
                best = presses
                if best == 0:
                    break

    return best if best is not None else 0


def minPressesMitm(buttonMasks: List[int], targetMask: int) -> int:
    k = len(buttonMasks)
    mid = k // 2
    left = buttonMasks[:mid]
    right = buttonMasks[mid:]

    def allStates(masks: List[int]) -> Dict[int, int]:
        # state -> minimal presses to reach that state
        states: Dict[int, int] = {0: 0}
        for mask in masks:
            newStates = dict(states)
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

    best: Optional[int] = None
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


def minPresses(buttonMasks: List[int], targetMask: int, bruteLimitK: int = 24) -> Tuple[int, str]:
    k = len(buttonMasks)
    if k <= bruteLimitK:
        return minPressesBruteforce(buttonMasks, targetMask), "bruteforce"
    return minPressesMitm(buttonMasks, targetMask), "mitm"


def solve(filePath: str, selfTest: bool = True) -> None:
    levels = parseLevelsFromFile(filePath)

    total = 0
    maxK = 0
    usedMitm = 0

    for idx, lvl in enumerate(levels, start=1):
        targetMask = patternToMask(lvl.targetPattern)
        buttonMasks = [wiringToMask(w) for w in lvl.buttonWirings]
        k = len(buttonMasks)
        maxK = max(maxK, k)

        best, method = minPresses(buttonMasks, targetMask)
        total += best
        if method == "mitm":
            usedMitm += 1

        # Optional: prove MITM matches brute for small K (sanity check)
        if selfTest and k <= 22:
            bf = minPressesBruteforce(buttonMasks, targetMask)
            mt = minPressesMitm(buttonMasks, targetMask)
            assert bf == mt, f"Mismatch on line {idx}: bruteforce={bf}, mitm={mt}"

    print(f"Levels: {len(levels)}")
    print(f"Max buttons K: {maxK}")
    print(f"MITM used: {usedMitm} lines")
    print(f"Total minimum presses: {total}")


if __name__ == "__main__":
    import sys
    st = time.process_time()
    devMode = False
    devMode = True
    if devMode:
        path = "example.txt"
    else:
        path = "input.txt"
    solve(path, selfTest=True)
    et = time.process_time()
    print(f"\nZeit: {(et-st)*1000}ms")
