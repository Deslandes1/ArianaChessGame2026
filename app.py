"""
Ariana Chess Academy — Streamlit entry point.
Embeds the full interactive chess board and shows Python-side coaching metrics.
"""

from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

from chess_engine import ChessEngine
from ariana_avatar import get_ariana_svg

# ─────────────────────────────────────────────────────────────
# Page configuration
# ─────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Ariana Chess Academy",
    page_icon="♛",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────────────────────
# Custom CSS for a polished, dark-themed Streamlit shell
# ─────────────────────────────────────────────────────────────
st.markdown(
    """
    <style>
        .stApp {
            background: radial-gradient(circle at 50% 0%, #16203a 0%, #0a0e1a 60%);
        }
        [data-testid="stSidebar"] {
            background: linear-gradient(180deg, #0f1830 0%, #0a0e1a 100%);
            border-right: 1px solid #2a3550;
        }
        [data-testid="stSidebar"] h1, [data-testid="stSidebar"] h2,
        [data-testid="stSidebar"] h3, [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] li, [data-testid="stSidebar"] span {
            color: #d0e0ff !important;
        }
        .ariana-sidebar-card {
            background: linear-gradient(135deg, #1b2440 0%, #262e4e 100%);
            border: 1px solid #2a3550;
            border-left: 4px solid #ffd93b;
            border-radius: 12px;
            padding: 14px 16px;
            margin: 10px 0 16px 0;
        }
        .ariana-sidebar-card h3 {
            color: #ffd93b !important;
            font-size: 1rem;
            margin: 0 0 6px 0;
        }
        .ariana-sidebar-card p {
            color: #cfe0ff !important;
            font-size: .85rem;
            line-height: 1.4;
            margin: 0;
        }
        .metric-pill {
            display: inline-block;
            background: rgba(58,160,255,.15);
            border: 1px solid #3aa0ff;
            color: #d0e0ff;
            padding: 4px 12px;
            border-radius: 20px;
            font-size: .78rem;
            margin: 3px 4px 3px 0;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# ─────────────────────────────────────────────────────────────
# Sidebar — Ariana intro + game info
# ─────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(
        f"""
        <div style="text-align:center; margin-bottom: 6px;">
            <div style="width:120px; height:120px; margin: 0 auto;
                        filter: drop-shadow(0 8px 20px rgba(58,160,255,.5));">
                {get_ariana_svg()}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("## ♛ Ariana Chess Academy")
    st.markdown(
        "<p style='color:#a0b0d0; font-size:.88rem; margin-top:-6px;'>"
        "Learn chess the perfect way — with a coach who always shows you the best move."
        "</p>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="ariana-sidebar-card">
            <h3>💡 How to play</h3>
            <p>
                1. Tap any of your pieces to see its legal moves.<br>
                2. Follow the <b>golden arrow</b> — that is Ariana's suggested move.<br>
                3. Drag the piece to its destination, or click <b>▶ Play This Move</b>.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 🎯 Features")
    st.markdown(
        '<span class="metric-pill">Full FIDE Rules</span>'
        '<span class="metric-pill">Auto-Suggest Arrow</span>'
        '<span class="metric-pill">Checkmate & Draw</span>'
        '<span class="metric-pill">Undo & History</span>'
        '<span class="metric-pill">Beginner Coach</span>',
        unsafe_allow_html=True,
    )

    st.markdown("---")

    # Python-side engine demo — shows the same position evaluation
    with st.expander("🧠 Python engine preview", expanded=False):
        st.caption(
            "The board runs client-side for instant response. "
            "Below is the Python rules engine that mirrors the same logic — useful for tests and server-side analysis."
        )
        engine = ChessEngine()
        st.code(engine.ascii_board(), language="text")
        st.write(f"**Turn:** {'White' if engine.turn == 'w' else 'Black'}")
        st.write(f"**Legal moves available:** {len(engine.all_legal_moves())}")

    st.markdown("---")
    st.markdown(
        "<p style='font-size:.75rem; color:#6d7a96; text-align:center;'>"
        "Built by Gesner Deslandes<br>Technology Coordinator<br>"
        "📞 (509)-57385663<br>✉️ deslandes78@gmail.com</p>",
        unsafe_allow_html=True,
    )

# ─────────────────────────────────────────────────────────────
# Main area — embed the interactive chess game
# ─────────────────────────────────────────────────────────────
html_path = Path(__file__).parent / "static" / "chess_game.html"

if not html_path.exists():
    st.error(
        "❌ **Missing file:** `static/chess_game.html`\n\n"
        "Please copy the full HTML from the previous response into "
        "`static/chess_game.html` (create the `static/` folder if needed)."
    )
    st.stop()

html_content = html_path.read_text(encoding="utf-8")

# Inject the game. Height ~1150px covers header + board + panels + history.
components.html(html_content, height=1150, scrolling=True)

# ─────────────────────────────────────────────────────────────
# Footer
# ─────────────────────────────────────────────────────────────
st.markdown(
    """
    <div style="text-align:center; padding: 18px 0 6px 0;
                color:#6d7a96; font-size:.78rem;">
        ♛ Ariana Chess Academy — practice responsibly, play beautifully.
    </div>
    """,
    unsafe_allow_html=True,
)
