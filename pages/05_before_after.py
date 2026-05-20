"""
Page 05 — Prima / Dopo
=======================
Before/After comparison of the zero-day landscape with data visualizations.
"""

import streamlit as st
import pandas as pd

st.markdown("## 📊 Prima / Dopo: Il Panorama Zero-Day")
st.markdown(
    """
    Un confronto diretto tra il panorama della sicurezza informatica
    prima e dopo l'introduzione di Claude Mythos Preview.
    """
)

st.markdown("---")

# ── Comparison Table ────────────────────────────────────────────────────────
st.markdown("### Tabella Comparativa")

comparison = pd.DataFrame(
    {
        "Metrica": [
            "Tasso di Discovery Zero-Day",
            "Tempo di Patch (Difensore)",
            "Tooling e Complessita",
            "Vantaggio Attaccante/Difensore",
            "Costo di Discovery",
            "Infrastruttura di Disclosure",
        ],
        "PRIMA (2020-2025)": [
            "Artigianale e scarso; ~75 zero-day exploitati nel 2024",
            "Cicli prevedibili; SLA 30/60/90 giorni",
            "Euristico e basato su firme (es. Nessus 18.56% accuracy)",
            "Vantaggio asimmetrico attaccante",
            "$20K-$120K per pentest manuale",
            "NVD/CVE gestivano volumi umani (backlog ~26k)",
        ],
        "DOPO (Aprile 2026+)": [
            "Industrializzato; migliaia in settimane su tutti i major OS",
            "Finestra collassata; SLA a 2 ore richiesti",
            "Agentico e semantico (ROP chains, JIT heap sprays)",
            "Vantaggio difensore SOLO se equipaggiato con AI",
            "<$2.000 in token di compute",
            "Failure sistemico del tracking CVE tradizionale",
        ],
    }
)

st.dataframe(comparison, use_container_width=True, hide_index=True, height=280)

st.markdown("---")

# ── Key Metrics Before/After ────────────────────────────────────────────────
st.markdown("### Metriche Chiave a Confronto")

m1, m2, m3 = st.columns(3)

with m1:
    st.metric(
        "Costo Medio Data Breach",
        "$4.44M",
        help="IBM X-Force 2025 — media globale",
    )
    st.caption("USA: $10.22M | Healthcare: $7.42M")

with m2:
    st.metric(
        "Ciclo Medio di Breach",
        "241 giorni",
        help="181 giorni per detection + 60 per containment",
    )
    st.caption("Pre-Mythos — IBM X-Force 2025")

with m3:
    st.metric(
        "CVE Giornaliere (NVD)",
        "135.93",
        delta="+263% in 5 anni",
        delta_color="inverse",
    )
    st.caption("Backlog: 26.815 CVE non analizzate")

st.markdown("---")

# ── Scanner Accuracy ────────────────────────────────────────────────────────
st.markdown("### Accuracy degli Scanner Tradizionali (Pre-Mythos)")

scanner_data = pd.DataFrame(
    {
        "Scanner": ["Nessus (Tenable)", "Qualys VM", "Nuclei (ProjectDiscovery)", "Nexpose (Rapid7)"],
        "Disponibilita Dichiarata (%)": [55.09, 48.0, 42.0, 38.0],
        "Accuracy Reale (%)": [18.56, 23.0, 17.0, 15.0],
    }
)

st.dataframe(
    scanner_data,
    use_container_width=True,
    hide_index=True,
    column_config={
        "Disponibilita Dichiarata (%)": st.column_config.ProgressColumn(
            "Disponibilita Dichiarata",
            min_value=0,
            max_value=100,
            format="%.1f%%",
        ),
        "Accuracy Reale (%)": st.column_config.ProgressColumn(
            "Accuracy Reale",
            min_value=0,
            max_value=100,
            format="%.1f%%",
        ),
    },
)

st.caption("Fonte: Pentest-Tools benchmark analysis, 2024")

st.markdown("---")

# ── NVD Crisis ──────────────────────────────────────────────────────────────
st.markdown("### La Crisi del National Vulnerability Database")

st.markdown(
    """
    Il 15 Aprile 2026, NIST ha implementato una **policy di triage**:

    - **Priorita immediata**: Solo CVE presenti nel catalogo CISA KEV
      o utilizzate da software federale
    - **Priorita minima**: Tutte le altre CVE
    - **Deficit giornaliero**: ~8.959 analisi/giorno mancanti per smaltire il backlog
    """
)

st.error(
    """
    **Il sistema CVE/NVD e fondamentalmente inadeguato** per ingerire,
    valutare e arricchire vulnerabilita generate da intelligenza artificiale
    a questa scala. Serve un ripensamento architetturale dell'intera
    infrastruttura di disclosure globale.
    """
)
