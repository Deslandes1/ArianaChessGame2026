# ♛ Ariana Chess Academy

A friendly, beginner-focused chess trainer that teaches the **perfect game** — with a smiling cartoon coach who always shows you the best move.

![Ariana](https://img.shields.io/badge/Ariana-Chess%20Academy-3aa0ff?style=for-the-badge&logo=chess)
![Python](https://img.shields.io/badge/Python-3.10%2B-3776ab?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.32%2B-ff4b4b?style=for-the-badge&logo=streamlit)

## ✨ Features

- **Full FIDE rules** — castling, en passant, promotion, check, checkmate, stalemate
- **Automatic move suggestion** — a golden arrow appears every turn
- **Interactive board** — drag-and-drop or click-to-move
- **Python rules engine** — a mirrored server-side engine for tests and analysis
- **Beginner coaching** — Ariana explains each move in plain language
- **Move history + Undo** — experiment without fear

## 📁 Project structure

```
ariana-chess-academy/
├── app.py                     # Streamlit entry point
├── chess_engine.py            # Pure-Python chess rules engine
├── ariana_avatar.py           # Ariana's SVG avatar
├── static/
│   └── chess_game.html        # Interactive board (HTML/JS)
├── requirements.txt
├── README.md
├── .gitignore
└── .streamlit/
    └── config.toml
```

## 🚀 Run locally

```bash
git clone https://github.com/<your-username>/ariana-chess-academy.git
cd ariana-chess-academy
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

Then open <http://localhost:8501>.

## ☁️ Deploy on Streamlit Cloud

1. Push this repository to GitHub.
2. Go to <https://share.streamlit.io> and sign in with GitHub.
3. Click **New app**.
4. Choose:
   - **Repository:** `<your-username>/ariana-chess-academy`
   - **Branch:** `main`
   - **Main file path:** `app.py`
5. Click **Deploy**. First build takes ~1 minute.

## 🧪 Test the Python engine

```bash
python chess_engine.py
```

You should see the starting board, then a Scholar's-mate sequence ending in `Checkmate: True`.

## 📞 Contact

**Gesner Deslandes** — Technology Coordinator
📞 (509)-57385663 · ✉️ deslandes78@gmail.com

## 📄 License

MIT — free to use for education.
