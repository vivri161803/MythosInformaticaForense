import sys
import os
import genanki
import markdown2

# --- CONFIGURAZIONE ---
# ID fissi per permettere l'aggiornamento del mazzo (non cambiarli)
MODEL_ID = 1607392319
DECK_ID = 2059400110
DECK_NAME = "Informatica Criminale :: Studio" 

# CSS per rendere le card leggibili (supporto Dark Mode e Code Blocks)
CSS_STYLE = """
.card {
 font-family: 'Segoe UI', arial, sans-serif;
 font-size: 20px;
 text-align: center;
 color: #333;
 background-color: white;
}
.card.nightMode {
 background-color: #2e2e2e;
 color: #f0f0f0;
}
/* Stile per i blocchi di codice */
code {
 background-color: #f4f4f4;
 padding: 2px 4px;
 border-radius: 3px;
 font-family: 'Consolas', monospace;
 color: #d63384;
 font-size: 0.9em;
}
pre {
 text-align: left;
 background-color: #282c34;
 color: #abb2bf;
 padding: 10px;
 border-radius: 5px;
 overflow-x: auto;
 font-size: 0.8em;
}
.nightMode code { background-color: #444; color: #ff79c6; }
.nightMode pre { background-color: #1e1e1e; }
hr#answer { border: 0; border-top: 1px solid #ccc; margin: 20px 0; }
"""

# Definizione del Modello Anki (Fronte -> Retro)
my_model = genanki.Model(
  MODEL_ID,
  'Marp Markdown Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ],
  css=CSS_STYLE
)

def parse_markdown_slides(filename):
    """Legge il file MD e divide le slide basandosi sul separatore ---"""
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"❌ Errore: Il file '{filename}' non esiste.")
        sys.exit(1)

    # Splitta usando il separatore standard di Marp
    raw_slides = content.split("---")
    
    # Pulisce gli spazi bianchi e rimuove slide vuote
    slides = [s.strip() for s in raw_slides if s.strip()]

    # Rimuove l'header YAML di Marp se presente (solitamente la prima slide)
    # Controllo se la prima slide contiene configurazioni tipiche
    if slides and ("marp: true" in slides[0].lower() or "theme:" in slides[0].lower()):
        print("ℹ️  Header YAML rilevato e rimosso.")
        slides.pop(0)

    return slides

def main():
    # 1. Controllo Argomenti CLI
    if len(sys.argv) < 2:
        print("⚠️  Uso corretto: python md2anki.py nome_file.md")
        sys.exit(1)

    input_file = sys.argv[1]
    
    # Calcola il nome del file di output (stesso nome, estensione .apkg)
    base_name = os.path.splitext(input_file)[0]
    output_file = f"{base_name}.apkg"

    print(f"🔄 Elaborazione di: {input_file}...")

    # 2. Parsing delle Slide
    slides = parse_markdown_slides(input_file)
    
    total_slides = len(slides)
    if total_slides % 2 != 0:
        print(f"⚠️  Attenzione: Numero di slide dispari ({total_slides}). L'ultima verrà ignorata.")
        slides = slides[:-1] # Rimuove l'ultima spaiata

    # 3. Creazione del Mazzo
    my_deck = genanki.Deck(DECK_ID, DECK_NAME)
    
    count = 0
    # Itera a passi di 2: 
    # Indice 0 (Slide 1) = Fronte
    # Indice 1 (Slide 2) = Retro
    for i in range(0, len(slides), 2):
        front_md = slides[i]
        back_md = slides[i+1]

        # Converte Markdown -> HTML (con supporto per code blocks)
        front_html = markdown2.markdown(front_md, extras=["fenced-code-blocks", "tables"])
        back_html = markdown2.markdown(back_md, extras=["fenced-code-blocks", "tables"])

        note = genanki.Note(
            model=my_model,
            fields=[front_html, back_html]
        )
        my_deck.add_note(note)
        count += 1

    # 4. Esportazione
    genanki.Package(my_deck).write_to_file(output_file)
    
    print(f"✅ Successo! Create {count} flashcard.")
    print(f"📂 File generato: {os.path.abspath(output_file)}")

if __name__ == "__main__":
    main()