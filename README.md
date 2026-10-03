# ♛ Ariana Chess Academy

A friendly, beginner-focused chess trainer that teaches the **perfect game** —
with a smiling cartoon coach who always shows you the best move.

## ✨ Features

- **Full FIDE rules** — castling, en passant, promotion, check, checkmate, stalemate
- **Automatic move suggestion** — a golden arrow appears every turn
- **Interactive board** — drag-and-drop or click-to-move
- **Python rules engine** — a mirrored server-side engine for tests and analysis
- **Beginner coaching** — Ariana explains each move in plain language
- **Move history + Undo** — experiment without fear

## 🚀 Run locally

```bash
git clone https://github.com/<your-username>/ariana-chess-academy.git
cd ariana-chess-academy
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
