"""
Page 02 — Capacità di Mythos
=============================
Technical capabilities of Claude Mythos Preview, with empirical benchmarks.
"""

import streamlit as st
import pandas as pd

st.markdown("## ⚡ Capacità Tecniche di Claude Mythos Preview")
st.markdown(
    """
    Claude Mythos Preview rappresenta un salto qualitativo dalla corrispondenza
    euristica di pattern alla **comprensione semantica profonda** del codice.
    Le evidenze empiriche fornite da Anthropic e validate da enti indipendenti
    dimostrano capacità offensive senza precedenti.
    """
)

st.markdown("---")

# ── Key metrics ─────────────────────────────────────────────────────────────
c1, c2, c3, c4 = st.columns(4)
c1.metric("Exploit Firefox JS Engine", "181", delta="vs 2 di Opus 4.6", delta_color="normal")
c2.metric("Vuln. OpenBSD scoperta", "27 anni", help="Vulnerabilità presente da 27 anni, mai rilevata da fuzzing o SAST.")
c3.metric("Vuln. FFmpeg scoperta", "16 anni", help="Linea di codice analizzata >5M volte da tool automatici senza alert.")
c4.metric("CTF Expert-Level (AISI)", "73%", help="Compiti che richiedono 10+ anni di esperienza umana.")

st.markdown("---")

# ── Exploit Capabilities ───────────────────────────────────────────────────
st.markdown("### Capacità di Exploit Documentate")

tab_browser, tab_rce, tab_tlo = st.tabs(
    ["🌐 Browser Exploit Chain", "💻 RCE FreeBSD", "🏢 TLO Corporate Range"]
)

with tab_browser:
    st.markdown(
        """
        **Exploit multi-fase per browser web**

        Mythos ha scritto autonomamente un exploit che concatena
        **4 vulnerabilità distinte**, utilizzando un sofisticato
        *JIT heap spray* per evadere sia il sandbox del renderer
        che quello del sistema operativo.

        ```
        ┌──────────────┐    ┌───────────────┐    ┌──────────────┐    ┌──────────────┐
        │  Vuln #1      │───▶│  Vuln #2       │───▶│  Vuln #3      │───▶│  Vuln #4      │
        │  (Entry Point)│    │  (JIT Spray)   │    │  (Renderer    │    │  (OS Sandbox  │
        │               │    │                │    │   Escape)     │    │   Escape)     │
        └──────────────┘    └───────────────┘    └──────────────┘    └──────────────┘
        ```
        """
    )

with tab_rce:
    st.markdown(
        """
        **Remote Code Execution — FreeBSD NFS Server**

        Il modello ha scritto un exploit RCE che concatena
        **20 gadget ROP** (*Return-Oriented Programming*) distribuiti
        su più pacchetti di rete, ottenendo accesso root
        **senza autenticazione**.

        | Parametro | Valore |
        |---|---|
        | Tipo di attacco | Remote Code Execution |
        | Vettore | NFS Protocol |
        | Gadget ROP concatenati | 20 |
        | Autenticazione richiesta | Nessuna |
        | Privilegio ottenuto | Root |
        """
    )

with tab_tlo:
    st.markdown(
        """
        **"The Last Ones" — Simulazione di Rete Aziendale (AISI UK)**

        Un range di attacco a 32 step che richiede ricognizione avanzata,
        escalation di privilegi e manipolazione di Active Directory.

        - ✅ **Primo modello** a risolvere l'intero range TLO
        - 🎯 Completato autonomamente in **3 tentativi su 10**
        - ⏱️ Compito stimato per un professionista: **14–20 ore**
        - 📈 Il successo scala logaritmicamente con il budget di token
        """
    )

st.markdown("---")

# ── Comparison chart ────────────────────────────────────────────────────────
st.markdown("### Confronto Prestazionale: Opus 4.6 vs Mythos Preview")

comparison_data = pd.DataFrame(
    {
        "Modello": ["Claude Opus 4.6", "Claude Mythos Preview"],
        "Exploit Firefox JS (su test identico)": [2, 181],
        "CTF Expert-Level (%)": [12, 73],
        "TLO Range Completato": [0, 3],
    }
)

st.dataframe(
    comparison_data,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Exploit Firefox JS (su test identico)": st.column_config.ProgressColumn(
            "Exploit Firefox JS Engine",
            min_value=0,
            max_value=200,
            format="%d exploit",
        ),
        "CTF Expert-Level (%)": st.column_config.ProgressColumn(
            "CTF Expert-Level",
            min_value=0,
            max_value=100,
            format="%d%%",
        ),
    },
)

st.markdown("---")

# ── Bar chart for visual impact ─────────────────────────────────────────────
st.markdown("### Exploit generati — Firefox 147 JS Engine")

chart_data = pd.DataFrame(
    {"Modello": ["Opus 4.6", "Mythos Preview"], "Exploit": [2, 181]}
).set_index("Modello")

st.bar_chart(chart_data, color="#6C63FF", height=320)

st.caption("Fonte: Anthropic System Card, Aprile 2026 — test condotti in condizioni identiche.")
