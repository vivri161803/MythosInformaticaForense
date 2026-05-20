"""
Page 07 — Fonti
================
Curated source list with relevance ratings.
"""

import streamlit as st
import pandas as pd

st.markdown("## 📚 Fonti e Riferimenti")
st.markdown(
    """
    Elenco curato delle fonti primarie utilizzate in questa analisi,
    con valutazione di rilevanza per il framework dell'ethical hacking
    e degli aspetti legali.
    """
)

st.markdown("---")

sources = pd.DataFrame(
    {
        "Data": [
            "7 Apr 2026",
            "7 Apr 2026",
            "10 Apr 2026",
            "13 Apr 2026",
            "15 Apr 2026",
            "20 Apr 2026",
            "Mag 2026",
            "18 Mag 2026",
            "19 Mag 2026",
            "Mag 2026",
        ],
        "Fonte": [
            "Anthropic (Ufficiale)",
            "Fortune Magazine",
            "Forrester Research",
            "UK AI Security Institute",
            "IBM Security",
            "Foreign Policy",
            "NIST / NVD Updates",
            "CyberScoop",
            "Financial Markets Data",
            "Brookings Institution",
        ],
        "Rilevanza": [
            "🔴 Critica",
            "🟠 Alta",
            "🔴 Critica",
            "🔴 Critica",
            "🟡 Media",
            "🟠 Alta",
            "🟠 Alta",
            "🟠 Alta",
            "🟡 Media",
            "🟠 Alta",
        ],
        "Descrizione": [
            "Lancio Project Glasswing, capacita zero-day di Mythos, impegno $100M",
            "Reporting originale sul leak CMS e le metriche del tier Capybara",
            "10 conseguenze di secondo ordine, disruption di mercato, colli di bottiglia open-source",
            "Valutazione indipendente: 73% CTF expert, completamento range TLO a 32 step",
            "Cost of Data Breach Report 2025 ($4.44M media globale, lifecycle 241 giorni)",
            "Analisi geopolitica, warnings di Bengio, shift nel calcolo cyber",
            "Shift operativi NVD per +263% CVE submissions e algoritmi di prioritizzazione",
            "Lancio OpenAI Daybreak e GPT-5.5-Cyber verso operazione agentica autonoma",
            "Performance azionarie (CRWD, PANW), traiettoria Anthropic verso $380B",
            "Rischi dual-use dell'AI, basse barriere d'ingresso, implicazioni attori non-statali",
        ],
        "URL": [
            "https://www.anthropic.com/glasswing",
            "https://fortune.com",
            "https://www.forrester.com/blogs/project-glasswing-the-10-consequences-nobodys-writing-about-yet/",
            "https://www.aisi.gov.uk/blog/our-evaluation-of-claude-mythos-previews-cyber-capabilities",
            "https://www.ibm.com/reports/data-breach",
            "https://foreignpolicy.com/2026/04/20/claude-mythos-preview-anthropic-project-glasswing-cybersecurity-ai-hacking-danger/",
            "https://www.nist.gov/news-events/news/2026/04/nist-updates-nvd-operations-address-record-cve-growth",
            "https://cyberscoop.com/openai-daybreak-gpt-5-5-anthropic-mythos-cybersecurity/",
            "https://stockinvest.us/stock/CRWD",
            "https://www.brookings.edu/articles/ai-risks-from-non-state-actors/",
        ],
    }
)

st.dataframe(
    sources,
    use_container_width=True,
    hide_index=True,
    column_config={
        "URL": st.column_config.LinkColumn("Link", display_text="Apri"),
    },
    height=420,
)

st.markdown("---")

# ── Additional references ──────────────────────────────────────────────────
st.markdown("### Riferimenti Normativi Addizionali")

st.markdown(
    """
    - **EU AI Act** — Regolamento (UE) 2024/1689 del Parlamento Europeo
    - **CISA KEV Catalog** — Known Exploited Vulnerabilities
    - **NIST NVD** — National Vulnerability Database
    - **CAISI** — Center for AI Standards and Innovation (USA)
    - **Five Eyes Guidance** — Coordinamento CISA/NSA su AI agentici
    - **SentinelOne 2026 Trends** — 74% organizzazioni restringe autonomia AI nei SOC
    """
)

st.markdown("---")

st.markdown(
    """
    <div style="
        text-align: center;
        color: #6C63FF;
        padding: 24px;
        font-size: 0.85rem;
    ">
        <p>Informatica Forense — Analisi Accademica</p>
        <p style="color:#808098;">Maggio 2026</p>
    </div>
    """,
    unsafe_allow_html=True,
)
