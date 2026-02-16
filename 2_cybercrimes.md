---
marp: true
---

Un attaccante inietta un payload che cifra il database aziendale (rendendolo inaccessibile). Successivamente, invia una mail al CTO chiedendo 5 BTC per la chiave di decrittazione.

---

* **Violazione:** **Art. 629 c.p. (Estorsione)** + **635 bis (Danneggiamento dati)** + **615 ter (Accesso abusivo)**.
* **Logica:** L'input soddisfa la classe `Estorsione` perché c'è *violenza/minaccia* (blocco dati) + *coartazione psichica* (costrizione a pagare) + *ingiusto profitto* con altrui danno. Il ransomware è un attacco multi-thread che istanzia più reati concorrenti.

---



Utente A e Utente B hanno una relazione. A invia consensualmente foto intime a B. Dopo la rottura (evento `breakup`), B carica le foto su un gruppo Telegram pubblico senza il consenso di A, per vendicarsi.

--- 

* **Violazione:** **Art. 612 ter c.p. (Diffusione illecita di immagini o video sessualmente espliciti).**
* **Logica:** Il consenso iniziale (all'invio) non è ereditario per la classe `Pubblicazione`. La *ratio* è la tutela della privacy sessuale. Il dolo è specifico (volontà di diffondere).

---

Un utente utilizza una GAN (Generative Adversarial Network) per generare immagini fotorealistiche di minori di 18 anni in atti sessuali, pur non essendo soggetti reali esistenti, e le conserva sul PC.

---

* **Violazione:** **Art. 600 quater.1 c.p. (Pornografia virtuale).**
* **Logica:** Il codice non richiede un soggetto `biologico` reale vittima di abuso (a differenza del 600 bis). L'input è illegale se l'immagine è *rappresentativa* di minori.

---

Un SysAdmin di un ospedale, avendo credenziali di root legittime, accede al DB pazienti per copiare le cartelle cliniche di un VIP e venderle a un giornalista.

---

* **Violazione:** **Art. 167 / 167 bis / 167 ter Codice Privacy (Trattamento illecito di dati, diffusione illecita e acquisizione fraudolenta).**
* **Logica:** Anche se l'auth è legittima (`615 ter` potrebbe non scattare se ha i permessi), la finalità del trattamento viola la policy (profitto/danno). È un abuso di privilegi per finalità non previste dallo schema del DB.

---

Un soggetto riceve sul proprio wallet crypto dei fondi derivanti da una frode informatica (phishing) commessa da terzi. Per "pulirli", li fa passare attraverso un "mixer" e poi li converte in NFT.

---

* **Violazione:** **Art. 648 bis c.p. (Riciclaggio).**
* **Logica:** L'azione di *obfuscation* (mixer) serve a ostacolare l'identificazione della provenienza delittuosa (`Backtrace` impossibile). Se li avesse rubati lui stesso, sarebbe `648 ter` (Autoriciclaggio).

---

Un moderatore di un forum crea un thread incitando gli utenti a commettere atti violenti contro un gruppo etnico specifico, basandosi sulla loro origine.

---

* **Violazione:** **Art. 604 bis c.p. (Propaganda e istigazione a delinquere per motivi di discriminazione).**
* **Logica:** Non è semplice diffamazione (595 c.3). La funzione obiettivo è l'*odio razziale/etnico* e l'*istigazione concreta* (pericolo reale).

---

Un adulto di 40 anni chatta su Fortnite con un utente di 13 anni. Dopo settimane di *social engineering* (fiducia), gli chiede insistentemente di incontrarsi al parco per "scambiarsi dei giochi", con l'intenzione segreta di compiere atti sessuali. L'incontro non avviene perché interviene la Polizia.

---

* **Violazione:** **Art. 609 undecies c.p. (Adescamento di minorenni).**
* **Logica:** Reato di pericolo (buffer overflow preventivo). Non serve che l'atto sessuale avvenga. Basta la `condotta` (lusinghe/artifizi) + l'`intento` (dolo specifico).

---

Tizio scrive sulla bacheca Facebook di Caio (visibile a tutti): "Sei un ladro incompetente e truffi i clienti", senza che ciò sia vero.

---

* **Violazione:** **Art. 595 comma 3 c.p. (Diffamazione aggravata).**
* **Logica:** Offesa all'altrui reputazione + Assenza della persona offesa (comunicazione con più persone). L'uso del mezzo "social network" attiva l'aggravante del mezzo di pubblicità (broadcasting).

---

Un investigatore privato installa uno sniffer sulla rete Wi-Fi di un'azienda per leggere le email scambiate tra i dipendenti in tempo reale.

---

* **Violazione:** **Art. 617 quater c.p. (Intercettazione, impedimento o interruzione illecita di comunicazioni informatiche).**
* **Logica:** Captazione di un flusso di dati `in transit`. La tutela è sulla segretezza del flusso, non solo sul dato statico.

---

Una società sposta i server contenenti dati sensibili in un paradiso fiscale e cripta i log, rifiutandosi di fornire le chiavi durante un'ispezione della Guardia di Finanza delegata dal Garante.

---

* **Violazione:** **Art. 379 c.p. (favoreggiamento reale) / Art. 168 (Falsità di norifica al Garante) / 170 (Inosservanza) Codice Privacy.**
* **Logica:** Pietropaoli sottolinea spesso come le strutture off-shore servano a eludere il controllo. Qui si configura l'ostacolo alle funzioni di controllo (`Denial of Service` verso l'autorità).

---

Hacker ottiene accesso alla webcam di Tizio, registra un video intimo e minaccia: "Paga 500€ o lo mando a tua moglie".

--- 

* **Violazione:** **Art. 629 c.p. (Estorsione)** (Concorso con 615 bis se ha registrato indebitamente).
* **Logica:** La differenza col Revenge Porn è lo scopo: qui è il *profitto* (If `pay` then `delete`), nel Revenge Porn è il *danno* reputazionale (If `anger` then `publish`).

---

Ex partner invia 100 messaggi WhatsApp al giorno, monitora gli accessi online della vittima e le invia mail minatorie, causandole un perdurante stato di ansia e costringendola a cambiare numero.

---

* **Violazione:** **Art. 612 bis c.p. (Atti persecutori - Stalking).**
* **Logica:** Loop condizionale: Reiterazione (`while` action is repeated) + Evento psicologico (ansia/paura) o Evento pratico (cambio abitudini). Il mezzo telematico è aggravante.

---

Differenza tra Art. 600 bis, 600 ter, 600 quater.

---

* **Schema (Workflow):**
1. **600 bis:** *Produzione/Traffico* (Sfruttamento diretto del minore. Input: il corpo del minore). -> Reato più grave.
2. **600 ter:** *Distribuzione/Divulgazione* (Diffusione del file. Input: il file video/foto).
3. **600 quater:** *Detenzione* (Download/Storage. Input: possesso consapevole di ingente quantità).


> *Nota:* È una gerarchia di gravità decrescente (Creator > Distributor > Consumer).

---

Differenza tra Art. 167 (Trattamento illecito) e Art. 169 (Misure di sicurezza).

---

* **Art. 167 (Malice):** Richiede **Dolo Specifico** (nocumento/profitto). È un attacco attivo o un abuso intenzionale dei dati.
* **Art. 169 (Negligence):** Punisce l'omessa adozione di misure tecniche (es. no firewall, no password policy). È un reato di **omissione**.
> *Analisi:* 167 = Hacking/Data Leak volontario; 169 = Sysadmin pigro/incompetente (Vulnerabilità lasciata aperta).

---

Differenza tra 612 ter (Revenge Porn) e 615 bis (Interferenze illecite).

---

* **615 bis (Input Phase):** Il reato è nell'**acquisizione** (filmare di nascosto in domicilio privato). Non serve diffondere.
* **612 ter (Output Phase):** Il reato è nella **diffusione**. Il file sorgente poteva anche essere stato creato legittimamente/consensualmente.
* **617 septies:** È il "bridge": diffusione di riprese fatte fraudolentemente (collega l'illecito di origine alla diffusione).

---

Differenza 648 (Ricettazione) vs 648 bis (Riciclaggio).

---

* **648 (Statico):** Acquisto beni/dati di provenienza illecita per trarne profitto. (Es. Compro un DB rubato per usarlo).
* **648 bis (Dinamico):** Compio operazioni per **ostacolare l'identificazione**. (Es. Prendo Bitcoin sporchi e li converto in Monero).
> *Key:* Se c'è trasformazione/occultamento -> Riciclaggio.

---

Differenza 629 (Estorsione) vs 610 (Violenza privata) per `Genitore`, `Return Value`

---

* **Classe Genitore:** Entrambi costringono la vittima a fare/tollera/omettere qualcosa.
* **Discriminante (Return Value):**
    * Se il fine è un **ingiusto profitto** patrimoniale -> **629 (Estorsione)** (es. Ransomware).
    * Se manca il profitto economico (es. costringere qualcuno a cancellarsi da un social per dispetto) -> **610 (Violenza privata)**.


---

Relazione tra 615 ter e 635 bis.

---

* **615 ter (Breach):** Violo il perimetro (bypass auth o permanenza contro volontà). Integrità del sistema *logico*.
* **635 bis (Payload):** Distruggo, deteriorano o rendo inservibili i dati. Integrità del *dato*.
> *Scenario:* Spesso in concorso (entro -> 615 ter; cancello file -> 635 bis).

---

Soglia di attivazione del 612 bis (Stalking).

---

* **Condizione Necessaria (While Loop):** Reiterazione delle condotte (minacce/molestie).
* **Exit Condition (Evento):** Deve verificarsi ALMENO uno di questi tre eventi:
1. Perdurante stato d'ansia/paura.
2. Timore per l'incolumità propria/cari.
3. Alterazione delle abitudini di vita (es. chiudere profili social, cambiare strada).


> Senza l'evento -> Art. 660 (Molestia, reato minore).

---

Limite del 604 bis (Propaganda vs Istigazione).

---

* **Propaganda (Comma 1):** Diffusione di idee fondate sulla superiorità o odio razziale. (Reato di opinione violenta).
* **Istigazione (Comma 1 parte 2 & Comma 2):** Incitare a commettere **atti** di discriminazione o violenza.
* *Aggravante:* Se fatto via web, la pervasività aumenta il pericolo (reato di pericolo concreto).

---

Tizio, tramite una videochiamata Skype, costringe Caia (sotto minaccia di diffondere sue foto pregresse) a compiere atti di autoerotismo in diretta web-cam mentre lui guarda. Non c'è contatto fisico.

---

* **Violazione:** **Art. 609 bis c.p. (Violenza sessuale) - Interpretazione giurisprudenziale.**
* **Logica:** Attenzione al bug logico: molti pensano sia solo *Violenza Privata (610)* o *Estorsione (629)*. La Cassazione riconosce che l'atto sessuale può avvenire anche *senza contatto fisico* se c'è **interazione in tempo reale** e costrizione. La vittima è usata come strumento per il soddisfacimento del reo.

---

Un utente invia una *singola* email crittografata alla vittima con scritto: "So dove abiti, ti aspetto sotto casa per farti del male", allegando una foto del portone. Poi sparisce.

---

* **Violazione:** **Art. 612 c.p. (Minaccia) aggravata.**
* **Logica:** Manca il `Loop` (reiterazione) necessario per lo Stalking. È un evento singolo (`Single Instance`). Se la minaccia è grave (di morte o con armi/modi simbolici), si procede d'ufficio.

---

Hacker "X" crea un ransomware, incassa 10 Bitcoin (reato presupposto). Lo stesso Hacker "X" usa quei Bitcoin per comprare server in un data center estero per la sua attività "legale" di hosting.

---

* **Violazione:** **Art. 648 ter.1 c.p. (Autoriciclaggio).**
* **Logica:**
    * `if Subject(Reato Presupposto) == Subject(Riciclaggio)` allora è **Autoriciclaggio**.
    * `if Subject(Reato Presupposto) != Subject(Riciclaggio)` allora è **Riciclaggio (648 bis)**.


> È punito perché i soldi "sporchi" vengono reimmessi nell'economia legale (inquinamento economico), non per il mero possesso.

---

Differenza tra 604 bis (Reato autonomo) e 604 ter (Circostanza aggravante).

---

* **604 bis (Classe Base):** Il reato *è* l'istigazione o la discriminazione (es. scrivere "odio i [gruppo X]").
* **604 ter (Modificatore):** Si applica quando commetti un *altro reato* (es. 615 bis, 635 bis, 595) ma con la **finalità di discriminazione**.
> *Esempio:* Defaccio il sito di un'associazione politica (635 bis) scrivendo insulti razzisti -> Reato 635 bis + Aggravante 604 ter.

---

Durante un'istruttoria, il DPO (Data Protection Officer) invia al Garante un documento PDF modificato in cui dichiara di aver raccolto i consensi degli utenti 6 mesi fa, mentre in realtà li ha raccolti ieri (post-datazione).

---

* **Violazione:** **Art. 168 Codice Privacy (Falsità nelle dichiarazioni al Garante).**
* **Logica:** L'integrità del sistema di controllo si basa sulla fiducia dei dati di input forniti all'Authority. Fornire `False Data` in un procedimento formale è un reato autonomo, a prescindere dal danno agli utenti.

---

In che modo i cybercrimes sono diversi dai reati necessariamente informatici?

---

I cybercrimes vengono definiti come una evoluzione di una fattispecie criminosa, che potrebbe essere perpretrata anche senza supporto infromatico. I reati necessariamente informatici possono essere commessi solamente con l'ausilio di sistemi informatici. 

---

Quali sono le quatro classi di cybercrimes principali? 

---

- Danneggiamento a persone
    - pornogragia digitale
    - cyberbullismo
    - reati contro la privacy
- danneggiamoto tramite comunicazione: 
    - hate-speech
    - fake news
- danneggiamento oggetti (hardware)
    - Ransomware
    - DDos
    - Cyberlaundering

---

Il cyberbullismo e' un reato? 

---

No. Ad oggi non esiste una fattispecie specifica di reato per questo crimine. 

---