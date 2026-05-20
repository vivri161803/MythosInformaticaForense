# 🛡️ Informatica Forense — AI & Ethical Hacking Presentation

> **Presentazione accademica interattiva sulle conseguenze di Claude Mythos Preview
> nel framework dell'ethical hacking e negli aspetti legali della cybersecurity.**

Webapp Streamlit multipage che analizza l'impatto dei modelli linguistici agentici
(Mythos-class) sulla vulnerability discovery, il penetration testing, la responsible
disclosure e la regolamentazione internazionale (EU AI Act).

---

## 📋 Struttura del Progetto

```
InformaticaForense/
├── app.py                         # Entry-point Streamlit (navigazione multipage)
├── pages/
│   ├── 01_intro.py                # Introduzione, abstract e timeline eventi
│   ├── 02_capabilities.py         # Capacità tecniche di Claude Mythos Preview
│   ├── 03_ethical_hacking.py      # Impatto sul framework dell'ethical hacking
│   ├── 04_legal.py                # Aspetti legali: EU AI Act, dual-use, compliance
│   ├── 05_before_after.py         # Confronto prima/dopo nel panorama zero-day
│   ├── 06_risk_matrix.py          # Matrice del rischio e analisi scenari
│   └── 07_sources.py              # Fonti e riferimenti bibliografici
├── .streamlit/
│   └── config.toml                # Tema dark accademico personalizzato
├── specs/
│   ├── mission.md                 # Mission del progetto
│   ├── roadmap.md                 # Roadmap di sviluppo
│   ├── tech-stack.md              # Stack tecnologico
│   └── 2026-05-20-streamlit-presentation/
│       ├── plan.md                # Piano di implementazione
│       ├── requirements.md        # Requisiti funzionali
│       └── validation.md          # Criteri di validazione
├── source.md                      # Documento sorgente dell'analisi
├── requirements.txt               # Dipendenze Python
├── pyproject.toml                 # Configurazione progetto (uv)
└── README.md
```

---

## 🚀 Quick Start

### Prerequisiti

- **Python 3.9+**
- **uv** (consigliato) oppure `pip`

### Installazione

```bash
# Con uv (consigliato)
uv sync

# Oppure con pip
pip install -r requirements.txt
```

### Avvio

```bash
# Con uv
uv run streamlit run app.py

# Oppure direttamente
streamlit run app.py
```

L'app sarà disponibile su `http://localhost:8501`.

---

## 📖 Contenuti della Presentazione

| Sezione | Descrizione |
|---|---|
| **Introduzione** | Abstract, ambito dell'analisi e cronologia degli eventi chiave (Marzo–Maggio 2026) |
| **Capacità di Mythos** | Benchmark empirici: 181 exploit vs 2 (Opus 4.6), CTF expert-level 73%, range TLO |
| **Ethical Hacking** | Cambio di paradigma: costi, disclosure, certificazioni, open-source bottleneck |
| **Aspetti Legali** | EU AI Act, paradosso compliance, dual-use, governance Glasswing, framework internazionali |
| **Prima / Dopo** | Tabella comparativa zero-day landscape, accuracy scanner, crisi NVD |
| **Matrice del Rischio** | 4 scenari futuri con probabilità, impatto e strategie di mitigazione |
| **Fonti** | 10 fonti primarie curate con rating di rilevanza e link diretti |

---

## 🛠️ Stack Tecnologico

- **[Streamlit](https://streamlit.io/)** — Framework per webapp interattive in Python
- **[Pandas](https://pandas.pydata.org/)** — Manipolazione dati e tabelle comparative
- **Tema personalizzato** — Dark mode accademico con accent `#6C63FF`, font Inter

---

## 📚 Fonte Dati

L'analisi si basa sul documento `source.md`, un report accademico completo che copre:
- L'annuncio di Claude Mythos Preview e Project Glasswing (Aprile 2026)
- Reazioni dell'industria (CrowdStrike, Palo Alto Networks, Forrester, Gartner)
- Valutazioni governative indipendenti (UK AISI, BSI, CISA/NSA)
- Impatto sui mercati finanziari e disruption dei modelli di business
- Regolamentazione: EU AI Act, CAISI, Five Eyes guidance

---

## 📄 Licenza

Progetto accademico — Informatica Forense, Maggio 2026.