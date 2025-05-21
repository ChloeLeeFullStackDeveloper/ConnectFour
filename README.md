# Connect Four: Human vs AI (Minimax + Alpha-Beta)

This is a simple terminal-based **Connect Four** game built for the CPSC 3750 AI course Assignment #2.

## 👤 Player vs 🤖 AI

- You play as **Player 1 (value 1)**.
- The AI plays as **Player 2 (value 2)** using **Minimax search** with **Alpha-Beta pruning** and a heuristic evaluation function.

---

## 🧠 AI Details

- Depth-limited Minimax search (depth = 4)
- Alpha-Beta pruning for efficiency
- Heuristic scoring:
  - Center column preference
  - Bonus for 2- or 3-in-a-row
  - Penalty for opponent's threats

---

## ▶️ How to Run

Make sure you have Python 3 installed. Then:

```bash
python3 connect4.py
```

---

## 🕹️ Controls

- On your turn, type a number from `0` to `6` to drop a piece in that column.
- Invalid or full column? Try again.
- First to get 4 in a row (horizontal, vertical, or diagonal) wins.

---

## ✅ Features

- Fully functioning Connect Four board (6x7)
- Turn-based player and AI moves
- Win, draw, and move validation detection
- Terminal UI with clear output

---

## 📸 Example Screenshots

<img src="screenshots/screenshot1.png" width="500">
<img src="screenshots/screenshot2.png" width="500">
<img src="screenshots/screenshot3.png" width="500">

---

## 👩‍💻 Author

**Eunsuk (Chloe) Lee**  
CPSC 3750 - Summer 2025  
Assignment #2: Game Playing with AI  
