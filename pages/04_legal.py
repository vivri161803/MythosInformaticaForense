"""
Page 04 — Aspetti Legali
=========================
Legal analysis: EU AI Act, dual-use regulation, compliance paradox.
"""

import streamlit as st

st.markdown("## ⚖️ Aspetti Legali e Regolamentari")
st.markdown(
    """
    La capacita di Claude Mythos Preview di scoprire e sfruttare autonomamente
    vulnerabilita lo colloca al centro del dibattito contemporaneo sulle
    tecnologie dual-use, l'etica e la sicurezza nazionale.
    """
)

st.markdown("---")

# ── EU AI Act ───────────────────────────────────────────────────────────────
st.markdown("### L'EU AI Act e i Modelli Mythos-Class")

st.info(
    """
    **Data critica: 2 Agosto 2026** — L'EU AI Act entra nelle fasi di
    enforcement stringente. Mythos e i suoi derivati agentic qualificano
    inequivocabilmente come sistemi **«ad alto rischio»**.
    """
)

st.markdown(
    """
    Sotto l'EU AI Act, le organizzazioni che deployano modelli con il
    profilo di capacita di Mythos sono soggette a mandati legali stringenti:
    """
)

obligations = {
    "Audit Trail Automatizzati": "Mantenimento di registri completi e automatizzati di tutte le decisioni e le azioni del modello.",
    "Supervisione Human-in-the-Loop": "Obbligo di supervisione umana rigorosa su tutte le operazioni critiche del sistema AI.",
    "Incident Reporting Obbligatorio": "Notifica obbligatoria di qualsiasi incidente di sicurezza o malfunzionamento alle autorita competenti.",
    "Sanzioni Finanziarie": "Penalita fino al **3% del fatturato globale** per non-conformita.",
}

for title, desc in obligations.items():
    with st.expander(f"📋 {title}"):
        st.markdown(desc)

st.markdown("---")

# ── The Compliance Paradox ──────────────────────────────────────────────────
st.markdown("### Il Paradosso della Compliance")

col1, col2 = st.columns(2)

with col1:
    st.markdown(
        """
        <div style="
            background: rgba(255, 169, 77, 0.08);
            border: 1px solid rgba(255, 169, 77, 0.25);
            border-radius: 12px;
            padding: 24px;
            text-align: center;
        ">
            <p style="font-size:2.5rem; margin:0;">⚡</p>
            <h3 style="color:#FFA94D; margin:8px 0;">Velocita dell'AI</h3>
            <p style="color:#C0C0D0; font-size:0.88rem;">
                Discovery a velocita macchina.<br/>
                Migliaia di vulnerabilita in ore.<br/>
                SLA di patching a 2 ore.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div style="
            background: rgba(108, 99, 255, 0.08);
            border: 1px solid rgba(108, 99, 255, 0.25);
            border-radius: 12px;
            padding: 24px;
            text-align: center;
        ">
            <p style="font-size:2.5rem; margin:0;">👤</p>
            <h3 style="color:#B8B3FF; margin:8px 0;">Governance Umana</h3>
            <p style="color:#C0C0D0; font-size:0.88rem;">
                Audit trail obbligatori.<br/>
                Human-in-the-loop mandatorio.<br/>
                Review regolamentari periodiche.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div style="
        text-align: center;
        padding: 16px;
        color: #FFA94D;
        font-weight: 600;
        font-size: 0.95rem;
    ">
        ⚠️ I CISO devono colmare il gap paradossale tra velocita di discovery
        dell'AI e governance umana legalmente imposta.
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("---")

# ── Dual-Use Problem ───────────────────────────────────────────────────────
st.markdown("### Il Problema Dual-Use")

st.markdown(
    """
    A differenza della tecnologia nucleare, i modelli avanzati e la
    potenza di calcolo sono ampiamente distribuiti nei settori civili.
    L'architettura stessa di un LLM lo rende **intrinsecamente dual-use**:

    > *La stessa comprensione semantica necessaria per scrivere una patch
    > robusta e necessaria per sfruttare un memory leak.*

    **Posizioni dei Think-Tank:**
    """
)

think_tanks = [
    ("Brookings Institution", "I modelli avanzati e il computing sono diffusi nel settore civile, creando rischi immediati per infrastrutture critiche, sistemi finanziari e protocolli di biosicurezza."),
    ("CSIS", "L'unica risposta praticabile e una defense-in-depth estrema, abbandonando la prevenzione assoluta in favore di resilienza architetturale."),
    ("RAND Corporation", "La democratizzazione dei sistemi agentici abbassa drasticamente la barriera d'ingresso per attori non-statali malevoli."),
]

for org, position in think_tanks:
    st.markdown(
        f"""
        <div style="
            display: flex; gap: 14px; margin-bottom: 12px; align-items: flex-start;
        ">
            <div style="
                min-width: 160px;
                background: rgba(108,99,255,0.12);
                color: #B8B3FF;
                padding: 6px 14px;
                border-radius: 8px;
                font-size: 0.78rem;
                font-weight: 600;
                text-align: center;
            ">{org}</div>
            <p style="color:#C0C0D0; font-size:0.88rem; margin:0;">{position}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# ── Project Glasswing Governance ────────────────────────────────────────────
st.markdown("### La Governance di Project Glasswing")

st.markdown(
    """
    Anthropic ha eseguito una strategia di **contenimento** bloccando
    il modello dietro un consorzio ristretto di 11 partner. Tuttavia:
    """
)

tab_pro, tab_contro = st.tabs(["✅ Argomenti a Favore", "❌ Critiche"])

with tab_pro:
    st.markdown(
        """
        - Head-start difensivo per i maintainer di infrastrutture critiche
        - $100M in crediti di utilizzo per partner
        - $4M in donazioni dirette alla sicurezza open-source
        - Policy revisionata per permettere disclosure responsabile a terzi
        """
    )

with tab_contro:
    st.markdown(
        """
        - **Asimmetria informativa** pericolosa: «cartello di sicurezza privato»
        - PMI e progetti open-source non-partner restano esposti
        - Il contenimento a lungo termine e considerato una **fallacia teorica**
        - OpenAI Daybreak (GPT-5.5-Cyber) dimostra la proliferazione inevitabile
        """
    )

st.markdown("---")

# ── US regulatory landscape ────────────────────────────────────────────────
st.markdown("### Framework Regolamentari Internazionali")

c1, c2, c3 = st.columns(3)

with c1:
    st.metric("EU AI Act", "Ago 2026", help="Enforcement stringente dal 2 Agosto 2026")
    st.caption("Sanzioni fino al 3% del fatturato globale")

with c2:
    st.metric("US — CAISI", "Volontario", help="Center for AI Standards and Innovation")
    st.caption("Review di sicurezza pre-deployment per modelli non rilasciati")

with c3:
    st.metric("Five Eyes", "Coordinato", help="CISA + NSA + partner Five Eyes")
    st.caption("Guidance per adozione di AI agentici nei servizi")
