"""
Page 06 — Matrice del Rischio
==============================
Risk matrix with scenario analysis.
"""

import streamlit as st
import pandas as pd

st.markdown("## 🎯 Matrice del Rischio: Scenari e Impatto")
st.markdown(
    """
    Un'analisi degli scenari futuri piu probabili derivanti dalla
    proliferazione di modelli Mythos-class nel panorama della cybersecurity.
    """
)

st.markdown("---")

# ── Risk Matrix Table ───────────────────────────────────────────────────────
risk_data = pd.DataFrame(
    {
        "Scenario": [
            "Difensori Vincono (Ipotesi Glasswing)",
            "Corsa agli Armamenti Cyber (Parita Offesa/Difesa)",
            "Crackdown Regolamentare e Failure di Compliance",
            "Misuse da Attori Non-Statali",
        ],
        "Probabilita": ["Media", "Molto Alta", "Alta", "Alta"],
        "Impatto": ["Alto", "Critico", "Medio", "Critico"],
        "Livello Rischio": ["⚠️ Alto", "🔴 Critico", "🟡 Medio", "🔴 Critico"],
    }
)

st.dataframe(risk_data, use_container_width=True, hide_index=True, height=200)

st.markdown("---")

# ── Detailed scenarios ──────────────────────────────────────────────────────
st.markdown("### Analisi Dettagliata degli Scenari")

# Scenario 1
with st.expander("🟢 Difensori Vincono (Ipotesi Glasswing) — Probabilita: Media"):
    st.markdown(
        """
        **Conseguenza:** L'AI identifica e patcha le falle nelle infrastrutture
        legacy prima che gli avversari possano weaponizzarle, ribaltando il
        vantaggio asimmetrico a favore del difensore.

        **Mitigazione:** Investimento massiccio e continuativo in pipeline
        automatizzate di validazione e deployment per eguagliare la velocita
        di discovery della macchina.

        **Condizioni necessarie:**
        - Accesso democratizzato ai tool di discovery AI
        - Capacita di patch automatizzato end-to-end
        - Cooperazione internazionale effettiva
        """
    )

# Scenario 2
with st.expander("🔴 Corsa agli Armamenti Cyber — Probabilita: Molto Alta"):
    st.markdown(
        """
        **Conseguenza:** La rapida proliferazione di modelli open-weights o
        concorrenti (es. OpenAI Daybreak con GPT-5.5-Cyber) concede capacita
        equivalenti agli avversari. Il time-to-exploit scende a quasi zero.

        **Mitigazione:**
        - Implementazione di defense-in-depth estrema
        - Architetture zero-trust
        - Shift fondamentale dalla dipendenza dal patching statico

        **Evidenza attuale:** OpenAI Daybreak (Maggio 2026), GPT-5.5-Cyber
        score 82.7% su Terminal-Bench 2.0.
        """
    )

# Scenario 3
with st.expander("🟡 Crackdown Regolamentare — Probabilita: Alta"):
    st.markdown(
        """
        **Conseguenza:** L'EU AI Act e mandati globali equivalenti paralizzano
        l'adozione enterprise di automazione difensiva a causa di requisiti
        insormontabili di audit e human-in-the-loop.

        **Mitigazione:** Sviluppo di piattaforme di governance integrate che
        automatizzano il tracking di compliance e la provenienza delle
        decisioni senza sacrificare la velocita.

        **Rischio specifico:** Il paradosso compliance crea un gap operativo
        che gli attaccanti (non vincolati da regolamenti) possono sfruttare.
        """
    )

# Scenario 4
with st.expander("🔴 Misuse da Attori Non-Statali — Probabilita: Alta"):
    st.markdown(
        """
        **Conseguenza:** Un modello agentico jailbroken o leaked viene
        utilizzato da cybercriminali o gruppi terroristici per lanciare
        attacchi multi-fase altamente sofisticati a costo finanziario
        trascurabile.

        **Mitigazione:**
        - Safety interlock a livello hardware obbligatori
        - Trattati internazionali accelerati sulla proliferazione di modelli
        - Protocolli globali di condivisione threat intelligence

        **Nota:** A differenza della tecnologia nucleare, i modelli e il
        computing sono gia ampiamente distribuiti nei settori civili.
        """
    )

st.markdown("---")

# ── Summary ─────────────────────────────────────────────────────────────────
st.markdown("### Sintesi")

st.markdown(
    """
    <div style="
        background: linear-gradient(135deg, rgba(255,107,107,0.08), rgba(108,99,255,0.08));
        border: 1px solid rgba(108,99,255,0.2);
        border-radius: 12px;
        padding: 24px;
        text-align: center;
    ">
        <p style="color:#E0E0E0; font-size:1rem; line-height:1.7; max-width:700px; margin:0 auto;">
            Lo scenario piu probabile e la <strong style="color:#FF6B6B;">corsa agli armamenti
            cyber</strong>, dove la sicurezza globale dipende non dal restringere l'accesso
            all'intelligenza, ma dal <strong style="color:#69DB7C;">deployare automazione
            difensiva</strong> piu velocemente e comprensivamente delle controparti avversarie.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)
