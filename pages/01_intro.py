"""
Page 01 — Introduzione
=======================
Landing page presenting the thesis and the scope of the analysis.
"""

import streamlit as st

# ── Hero section ────────────────────────────────────────────────────────────
st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, rgba(108,99,255,0.15) 0%, rgba(108,99,255,0.03) 100%);
        border: 1px solid rgba(108,99,255,0.2);
        border-radius: 16px;
        padding: 48px 40px;
        margin-bottom: 2rem;
        text-align: center;
    ">
        <p style="font-size:3.2rem; margin:0;">🛡️</p>
        <h1 style="
            font-size: 2.2rem;
            background: linear-gradient(135deg, #B8B3FF, #6C63FF);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin: 12px 0 8px;
        ">L'Epoca dell'Agentic Vulnerability Discovery</h1>
        <p style="color: #9994CC; font-size: 1.05rem; max-width: 720px; margin: 0 auto;">
            Un'analisi accademica delle conseguenze di Claude Mythos Preview
            nel framework dell'ethical hacking e degli aspetti legali correlati.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Abstract ────────────────────────────────────────────────────────────────
st.markdown("## Abstract")
st.markdown(
    """
    Il 7 Aprile 2026, Anthropic ha pubblicamente riconosciuto l'esistenza di
    **Claude Mythos Preview** — un modello di frontiera in grado di scoprire
    autonomamente migliaia di vulnerabilità zero-day in sistemi critici,
    operando a *velocità macchina*. Questa capacità ha invalidato le assunzioni
    fondamentali della gestione tradizionale delle vulnerabilità.

    > *"Le capacità dell'intelligenza artificiale hanno superato una soglia
    > che richiede cambiamenti profondi nel modo in cui l'infrastruttura
    > digitale viene protetta."* — Anthony Grieco, Cisco CSTO
    """
)

st.markdown("---")

# ── Scope of Analysis ──────────────────────────────────────────────────────
st.markdown("## Ambito dell'Analisi")

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(
        """
        <div style="
            background: rgba(108,99,255,0.06);
            border: 1px solid rgba(108,99,255,0.15);
            border-radius: 12px;
            padding: 24px;
            height: 200px;
        ">
            <p style="font-size:1.8rem; margin:0;">🔓</p>
            <h3 style="margin:8px 0 6px; font-size:1rem;">Ethical Hacking</h3>
            <p style="color:#B0B0C0; font-size:0.88rem; line-height:1.5;">
                Come cambia il paradigma del penetration testing e della
                responsible disclosure quando un LLM supera gli esperti umani.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col2:
    st.markdown(
        """
        <div style="
            background: rgba(108,99,255,0.06);
            border: 1px solid rgba(108,99,255,0.15);
            border-radius: 12px;
            padding: 24px;
            height: 200px;
        ">
            <p style="font-size:1.8rem; margin:0;">⚖️</p>
            <h3 style="margin:8px 0 6px; font-size:1rem;">Aspetti Legali</h3>
            <p style="color:#B0B0C0; font-size:0.88rem; line-height:1.5;">
                L'EU AI Act, le obbligazioni di compliance, le sanzioni,
                e il paradosso tra velocità dell'AI e governance umana.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with col3:
    st.markdown(
        """
        <div style="
            background: rgba(108,99,255,0.06);
            border: 1px solid rgba(108,99,255,0.15);
            border-radius: 12px;
            padding: 24px;
            height: 200px;
        ">
            <p style="font-size:1.8rem; margin:0;">🌐</p>
            <h3 style="margin:8px 0 6px; font-size:1rem;">Dual-Use & Geopolitica</h3>
            <p style="color:#B0B0C0; font-size:0.88rem; line-height:1.5;">
                La natura intrinsecamente dual-use dei modelli linguistici
                e le implicazioni per la sovranità digitale nazionale.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# ── Timeline ────────────────────────────────────────────────────────────────
st.markdown("## Cronologia degli Eventi Chiave")

events = [
    ("Marzo 2026", "Leak CMS", "Fortune pubblica documenti interni su un tier «Capybara» con capacità offensive senza precedenti."),
    ("7 Apr 2026", "Lancio Mythos", "Anthropic annuncia Claude Mythos Preview e il progetto Glasswing con 11 partner industriali."),
    ("10 Apr 2026", "Shock di Mercato", "CRWD −7%, PANW −6%, ZS −4.5% — poi rimbalzo aggressivo nelle settimane successive."),
    ("13 Apr 2026", "Valutazione AISI", "UK AI Security Institute conferma: Mythos completa attacchi expert-level nel 73% dei casi."),
    ("15 Apr 2026", "Crisi NVD", "NIST implementa policy di triage: solo le CVE in CISA KEV ricevono arricchimento immediato."),
    ("Maggio 2026", "OpenAI Daybreak", "OpenAI lancia GPT-5.5-Cyber per red-teaming autonomo — inizia la corsa agli armamenti AI."),
]

for date, title, desc in events:
    st.markdown(
        f"""
        <div style="
            display: flex;
            gap: 16px;
            margin-bottom: 14px;
            align-items: flex-start;
        ">
            <div style="
                min-width: 110px;
                background: rgba(108,99,255,0.12);
                color: #B8B3FF;
                padding: 4px 12px;
                border-radius: 8px;
                font-size: 0.78rem;
                font-weight: 600;
                text-align: center;
                margin-top: 2px;
            ">{date}</div>
            <div>
                <strong style="color:#E0E0E0;">{title}</strong>
                <p style="color:#A0A0B8; font-size:0.88rem; margin:2px 0 0;">{desc}</p>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
