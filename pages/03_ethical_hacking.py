"""
Page 03 — Ethical Hacking
==========================
How agentic AI reshapes the ethical hacking framework.
"""

import streamlit as st

st.markdown("## 🔓 Conseguenze per l'Ethical Hacking")
st.markdown(
    """
    L'emergere di modelli «Mythos-class» ridefinisce radicalmente il framework
    dell'ethical hacking. Le attività tradizionalmente riservate a esperti con
    decenni di esperienza vengono ora automatizzate in minuti, sollevando
    questioni fondamentali sulla professione, i costi e la responsabilità.
    """
)

st.markdown("---")

# ── The Paradigm Shift ─────────────────────────────────────────────────────
st.markdown("### Il Cambio di Paradigma")

col_before, col_after = st.columns(2)

with col_before:
    st.markdown(
        """
        <div style="
            background: rgba(255, 107, 107, 0.06);
            border: 1px solid rgba(255, 107, 107, 0.2);
            border-radius: 12px;
            padding: 24px;
        ">
            <h3 style="color: #FF6B6B; margin-top: 0;">Prima di Mythos</h3>
            <ul style="color: #C0C0D0; font-size: 0.9rem; line-height: 1.8;">
                <li>Pentesting <strong>artigianale</strong>: $20K-$120K a ingaggio</li>
                <li>Bug bounty basati su <strong>scarsita di talento umano</strong></li>
                <li>Discovery rate: <strong>~75 zero-day</strong> exploitati globalmente (2024)</li>
                <li>SAST/DAST basati su <strong>firme e euristiche</strong></li>
                <li>Cicli di patch <strong>30/60/90 giorni</strong></li>
                <li>Nessus: accuracy reale del <strong>18.56%</strong></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

with col_after:
    st.markdown(
        """
        <div style="
            background: rgba(105, 219, 124, 0.06);
            border: 1px solid rgba(105, 219, 124, 0.2);
            border-radius: 12px;
            padding: 24px;
        ">
            <h3 style="color: #69DB7C; margin-top: 0;">Dopo Mythos</h3>
            <ul style="color: #C0C0D0; font-size: 0.9rem; line-height: 1.8;">
                <li>Discovery <strong>industrializzata</strong>: &lt;$2K in token di compute</li>
                <li>Migliaia di zero-day scoperti in <strong>settimane</strong></li>
                <li>Analisi semantica contextuale supera il pattern-matching</li>
                <li>SLA di patching collassano a <strong>2 ore</strong></li>
                <li>Pentesting tradizionale diventa <strong>obsoleto</strong> nel pricing</li>
                <li>Vantaggio difensore <strong>solo se equipaggiato con AI</strong></li>
            </ul>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("---")

# ── Impact on Pentest Industry ──────────────────────────────────────────────
st.markdown("### Impatto sull'Industria del Penetration Testing")

st.markdown(
    """
    > *"I modelli di prezzo tradizionali per il penetration testing, che
    > richiedono regolarmente tra $20.000 e $120.000 sulla base della
    > percepita scarsita di competenza umana, sono ora effettivamente
    > obsoleti."* — Forrester Research
    """
)

with st.expander("Dettaglio: Commoditizzazione della Discovery"):
    st.markdown(
        """
        | Parametro | Pre-Mythos | Post-Mythos |
        |---|---|---|
        | Costo per scoperta | $20K-$120K | <$2.000 in token |
        | Tempo per exploit complesso | Settimane-Mesi | Minuti-Ore |
        | Competenza richiesta | 10+ anni esperienza | Accesso al modello |
        | Volume output | Unita | Centinaia/Migliaia |

        La **validazione**, il **patch engineering**, e il **deployment**
        rimangono processi umani costosi — qui risiede il nuovo valore.
        """
    )

with st.expander("L'Open Source come Collo di Bottiglia"):
    st.markdown(
        """
        Forrester ha identificato i **maintainer open-source** come il
        nuovo collo di bottiglia critico:

        - Mythos scopre vulnerabilita decennali in **secondi**
        - I team di volontari non hanno la bandwidth per validare e patchare
        - Anthropic ha destinato **$4M** in donazioni dirette
        - Il backlog NVD era gia di **26.815 CVE non analizzate** prima di Mythos
        """
    )

st.markdown("---")

# ── Responsible Disclosure Strain ───────────────────────────────────────────
st.markdown("### Pressione sulla Responsible Disclosure")

st.warning(
    """
    **La responsible disclosure e sotto stress insostenibile.**
    Anthropic segue una policy di 135 giorni (90 + 45 di grace period),
    ma quando migliaia di vulnerabilita vengono divulgate simultaneamente,
    la capacita umana di ingegnerizzare, testare e deployare patch e
    ampiamente superata.
    """
)

# ── Key Questions ───────────────────────────────────────────────────────────
st.markdown("### Questioni Aperte per l'Ethical Hacking")

questions = [
    "Un pentest condotto da AI deve seguire le stesse Rules of Engagement di uno umano?",
    "Chi e responsabile quando un modello AI scopre e potenzialmente espone una vulnerabilita critica?",
    "La certificazione professionale (CEH, OSCP) mantiene rilevanza in un mondo di discovery automatizzata?",
    "Come si ridefinisce il concetto di scope nel pentesting quando un agente AI opera a velocita macchina?",
    "Il modello di bug bounty sopravvive quando la discovery ha costo marginale quasi zero?",
]

for i, q in enumerate(questions, 1):
    st.markdown(
        f"""
        <div style="
            background: rgba(108,99,255,0.05);
            border-left: 3px solid #6C63FF;
            padding: 12px 18px;
            margin-bottom: 10px;
            border-radius: 0 8px 8px 0;
        ">
            <span style="color:#6C63FF; font-weight:700; margin-right:8px;">{i}.</span>
            <span style="color:#D0D0E0; font-size:0.92rem;">{q}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
