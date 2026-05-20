"""
Informatica Forense — Streamlit Presentation
=============================================
Multipage entry‑point using the modern st.navigation API (Streamlit ≥ 1.36).
"""

import streamlit as st

# ── Page configuration ──────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI & Ethical Hacking: The Mythos Paradigm",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Shared custom CSS (injected once for every page) ────────────────────────
st.markdown(
    """
    <style>
    /* ── Import Google Font ─────────────────────────────────────────────── */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap');

    /* ── Global overrides ───────────────────────────────────────────────── */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    code, pre {
        font-family: 'JetBrains Mono', monospace !important;
    }

    /* Headings */
    h1 { font-weight: 800 !important; letter-spacing: -0.02em; }
    h2 { font-weight: 700 !important; color: #B8B3FF !important; }
    h3 { font-weight: 600 !important; color: #9D97FF !important; }

    /* ── Sidebar polish ─────────────────────────────────────────────────── */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #12141D 0%, #1A1D28 100%);
        border-right: 1px solid rgba(108, 99, 255, 0.15);
    }
    section[data-testid="stSidebar"] .stMarkdown h1 {
        font-size: 1.15rem !important;
        color: #A9A3FF;
    }

    /* ── Metric cards ───────────────────────────────────────────────────── */
    [data-testid="stMetric"] {
        background: linear-gradient(135deg, rgba(108, 99, 255, 0.08) 0%, rgba(108, 99, 255, 0.02) 100%);
        border: 1px solid rgba(108, 99, 255, 0.18);
        border-radius: 12px;
        padding: 16px 20px;
    }
    [data-testid="stMetricLabel"] {
        color: #B0AAFF !important;
        font-weight: 500;
        text-transform: uppercase;
        font-size: 0.72rem !important;
        letter-spacing: 0.06em;
    }
    [data-testid="stMetricValue"] {
        font-weight: 700 !important;
    }

    /* ── Expander styling ───────────────────────────────────────────────── */
    details[data-testid="stExpander"] {
        border: 1px solid rgba(108, 99, 255, 0.15) !important;
        border-radius: 10px !important;
        background: rgba(108, 99, 255, 0.03);
    }
    details[data-testid="stExpander"] summary span {
        font-weight: 600 !important;
    }

    /* ── Dividers ───────────────────────────────────────────────────────── */
    hr {
        border: none;
        height: 1px;
        background: linear-gradient(90deg, transparent, rgba(108, 99, 255, 0.35), transparent);
        margin: 2rem 0;
    }

    /* ── Blockquotes (used for callouts) ────────────────────────────────── */
    blockquote {
        border-left: 3px solid #6C63FF !important;
        background: rgba(108, 99, 255, 0.06);
        padding: 12px 18px;
        border-radius: 0 8px 8px 0;
        font-style: italic;
    }

    /* ── Tabs styling ───────────────────────────────────────────────────── */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    .stTabs [data-baseweb="tab"] {
        border-radius: 8px 8px 0 0;
        padding: 8px 20px;
        font-weight: 500;
    }

    /* ── Source chip ─────────────────────────────────────────────────────── */
    .source-chip {
        display: inline-block;
        background: rgba(108, 99, 255, 0.12);
        color: #B8B3FF;
        padding: 3px 10px;
        border-radius: 999px;
        font-size: 0.72rem;
        font-weight: 500;
        margin: 2px 3px;
        letter-spacing: 0.02em;
    }

    /* ── Risk badge ──────────────────────────────────────────────────────── */
    .risk-critical { color: #FF6B6B; font-weight: 700; }
    .risk-high     { color: #FFA94D; font-weight: 700; }
    .risk-medium   { color: #FFD43B; font-weight: 600; }
    .risk-low      { color: #69DB7C; font-weight: 600; }

    /* ── Fade-in animation ──────────────────────────────────────────────── */
    @keyframes fadeSlideIn {
        from { opacity: 0; transform: translateY(12px); }
        to   { opacity: 1; transform: translateY(0); }
    }
    .stMainBlockContainer {
        animation: fadeSlideIn 0.45s ease-out;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ── Sidebar branding ────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("# 🛡️ Informatica Forense")
    st.caption("Analisi Accademica — Maggio 2026")
    st.markdown("---")

# ── Define pages ────────────────────────────────────────────────────────────
intro = st.Page("pages/01_intro.py", title="Introduzione", icon="📋")
capabilities = st.Page("pages/02_capabilities.py", title="Capacità di Mythos", icon="⚡")
ethical_hacking = st.Page("pages/03_ethical_hacking.py", title="Ethical Hacking", icon="🔓")
legal = st.Page("pages/04_legal.py", title="Aspetti Legali", icon="⚖️")
before_after = st.Page("pages/05_before_after.py", title="Prima / Dopo", icon="📊")
risk_matrix = st.Page("pages/06_risk_matrix.py", title="Matrice del Rischio", icon="🎯")
sources = st.Page("pages/07_sources.py", title="Fonti", icon="📚")

pg = st.navigation(
    {
        "Presentazione": [intro, capabilities],
        "Analisi": [ethical_hacking, legal, before_after],
        "Conclusioni": [risk_matrix, sources],
    }
)
pg.run()
