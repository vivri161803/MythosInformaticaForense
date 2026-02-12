# Legal/Tech Study Pipeline (Markdown to Anki)

> **Automated Flashcard Generation for Law & Computer Science**
> _Converti appunti in Markdown (formato Marp) in mazzi Anki (.apkg) con Python._

Questo progetto implementa una pipeline di studio ottimizzata per **Data Scientist** che devono apprendere materie legali (es. Diritto dell'Informatica). Permette di scrivere flashcard come codice (Markdown), versionarle, e convertirle automaticamente in mazzi per la *Spaced Repetition* su Anki.

---

## 📋 Prerequisiti

### Software
1.  **Python 3.x** installato.
2.  **Anki Desktop** (Mac/Windows/Linux) - [Scarica qui](https://apps.ankiweb.net/).
3.  Account **AnkiWeb** (Gratuito) per la sincronizzazione su iPhone.

### Librerie Python
Installa le dipendenze necessarie eseguendo:

```bash
pip install genanki markdown2