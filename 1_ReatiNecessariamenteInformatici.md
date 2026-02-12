---
marp: true
---

# Fronte

Un SysAdmin, regolarmente autorizzato, accede al database aziendale ma scarica i dati dei clienti per rivenderli a un competitor. Non ha forzato nessuna password.

---

# Retro

Art. 615-ter c.p. (Accesso abusivo a sistema informatico).

Logica: Anche se hai le credenziali (auth = true), l'accesso diventa abusivo se lo scopo è contrario alla volontà del titolare (teoria dello "sviamento di potere"). È un abuso della sessione, non un brute-force.

---

# Fronte

Tizio crea uno script Python per fare brute-force su account Instagram e lo carica su una repo pubblica di GitHub scrivendo "strumento per testare la sicurezza", ma nei commenti spiega come usarlo per hackerare ex fidanzate.

---

# Retro

Art. 615-quater c.p. (Detenzione e diffusione abusiva di codici di accesso).

Logica: Il reato punisce la distribuzione (deployment) di strumenti (codici, parole chiave, script) idonei all'accesso, se c'è il dolo specifico di usarli per danneggiare o accedere abusivamente.

---

# Fronte

Tizio altera l'algoritmo di un sito di e-commerce affinché, al checkout, il totale nel carrello venga calcolato con uno sconto del 99% non previsto. Il sistema processa l'ordine automaticamente.

---

# Retro

Art. 640-ter c.p. (Frode informatica).

Logica: A differenza della truffa classica (che inganna una persona), qui si "inganna" la macchina (alterazione del funzionamento di un sistema). L'ottenimento dell'ingiusto profitto avviene manipolando l'elaborazione dei dati.

---

# Fronte

Un attaccante lancia un ransomware che cifra tutti i file di un PC privato, rendendoli inutilizzabili, ma il sistema operativo (OS) continua a girare regolarmente.

---

# Retro

Art. 635-bis c.p. (Danneggiamento di informazioni, dati e programmi).

Logica: Il target è il dato (il software/file), non l'hardware o il sistema nel suo complesso. La condotta è "rendere inservibili" i dati.

---

# Fronte

Un hacker crea un malware. Questa volta il malware blocca l'avvio del server di un ente privato, rendendo impossibile il boot della macchina.

---

# Retro

Art. 635-quater c.p. (Danneggiamento di sistemi informatici).

Logica: Il danno scala di livello. Non sono solo i file a essere bloccati, ma l'intero sistema (system availability = 0).

---

# Fronte

Tizio installa uno sniffer hardware sul router di un internet café per catturare i pacchetti dati degli utenti (chat, email) in transito.

---

# Retro

Art. 617-quater c.p. (Intercettazione illecita).

Logica: È l'equivalente digitale delle microspie. Punisce chi intercetta (read) o impedisce (block) comunicazioni relative a un sistema informatico.

---

# Fronte

Mappa concettuale artt. 635-bis, ter, quater, quinquies.

--- 

# Retro

Immagina una matrice 2x2.

635-bis: Dati Privati.
635-ter: Sistemi di Pubblica Utilità.
635-quater: Sistemi di Pubblica Utilità (es. Ospedale).
635-quinquies: Sistemi di Pubblica Utilità.

**Nota**: Se tocchi la Pubblica Utilità, la pena schizza in alto (aggravante specifica o reato autonomo più grave).

--- 

# Fronte

Class `AccessoAbusivo` (Art. 615-ter)

---

# Retro
 
`Protected_System = True` (Il sistema deve essere protetto da misure di sicurezza, anche banali).

`Action = Entrare` (Login) OVVERO Trattenersi (Stay logged in) contro la volontà del titolare.

`User_Type = Chiunque` (Hacker esterno) O Insider (Admin/Dipendente con poteri ma scopo illecito).

--- 

# Fronte

Differenza 617-quater vs 617-sexies

---

# Retro

617-quater (Intercettazione): Riguarda la segretezza (Confidentiality). Ascolto ciò che non dovrei sentire.

617-sexies (Falsificazione): Riguarda l'integrità (Integrity) e l'autenticità. Modifico il contenuto della comunicazione o ne faccio apparire una falsa (es. spoofing email per far credere che l'abbia mandata il CEO).

---

# Fronte

Differenza 617-quater vs 617-quinquies

---

# Retro

617-quater (Intercettazione): Riguarda la segretezza (Confidentiality). Ascolto ciò che non dovrei sentire.

617-quinquies (Intento di Intercettazione): possiedo o provo ad installare strumenti volti alla violazione del 617-quater

---

# Fronte 

Differenza chiave Art. 640-ter vs 615-ter

--- 

# Retro

615-ter: È un reato "di ostacolo". Violo il domicilio digitale. Il danno non è necessario per la consumazione.

640-ter: È un reato "di evento". Devo ottenere un ingiusto profitto con altrui danno. Se entro abusivamente ma non rubo soldi/asset, è 615-ter, non frode.

---

# Fronte

Differenza 617-quater vs 617-sexies

---

615-ter: È un reato "di ostacolo". Violo il domicilio digitale. Il danno non è necessario per la consumazione.

615-quater: Possesso o installazione di strumenti volti alla violazione dell'articolo 615-ter



