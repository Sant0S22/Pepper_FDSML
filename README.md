

# Progetto Robot Pepper per Assistenza Ospedaliera

## Introduzione
Questo repository contiene il codice e la documentazione relativa al progetto di ricerca sull'utilizzo del robot Pepper come strumento di supporto nell'ambito dell'assistenza ospedaliera. Nell'ambito di questa ricerca, ci siamo concentrati sull'implementazione di un sistema che sfrutta il robot Pepper per assistere il personale ospedaliero nelle attività quotidiane e migliorare l'esperienza dei pazienti.

## Contenuto del Repository
Il repository è organizzato nel seguente modo:
- **Codice**: Contiene l'implementazione del sistema sul robot Pepper.
- **Documentazione**: Contiene documentazione tecnica e guide per l'utilizzo del sistema.
- **Immagini**: Contiene le immagini relative al corridoio, alla mappa generata dal robot Pepper e all'architettura del sistema.

## Tecnologie Utilizzate
- **Robot Pepper**: Il robot utilizzato come interfaccia fisica per interagire con il personale ospedaliero e i pazienti.
- **Assistente Vocale Alexa**: Utilizzato per consentire interazioni vocali intuitive tra il robot Pepper, il personale ospedaliero e i pazienti.
- **Database NoSQL Firebase**: Utilizzato per memorizzare le informazioni sulle stanze ospedaliere e i pazienti, facilitando la comunicazione tra il sistema e il robot Pepper.
- **Algoritmo di Riconoscimento Facciale**: Utilizzato per rilevare la presenza dei pazienti nelle stanze utilizzando le telecamere integrate nel robot Pepper.

## Funzionalità Principali
Il sistema implementato offre le seguenti funzionalità principali:
1. Comunicazione tramite assistente vocale Alexa per interazioni intuitive.
2. Identificazione delle stanze in cui è necessario prestare assistenza.
3. Generazione di una mappa dell'ambiente ospedaliero.
4. Rilevamento della presenza dei pazienti nelle stanze tramite riconoscimento facciale.
5. Trasmissione delle informazioni rilevanti al personale medico.

## Configurazione e Utilizzo
Per configurare e utilizzare il sistema, fare riferimento alla documentazione fornita nella directory `Documentazione`.

## Contributi
I contributi a questo progetto sono benvenuti. Si prega di seguire le linee guida per i contributi descritte nella sezione `CONTRIBUTING.md`.

## Autori
- Luigi Emanuele Sica
- Francesco Paciello
- Nicola Pio Santorsa



![Corridoio](/img/Corridoio.png)
*Immagine del corridoio sul quale abbiamo eseguito il nostro esperimento*

![Mappa](/img/mappa.png)
*Mappa generata dal robot Pepper dell'ambiente*

![Architettura](/img/Architettura.png)
*Architettura del sistema*

## Esecuzione del codice
Per eseguire il codice bisogna:

1) Da file connessioneFirebase.ipynb, avviare il blocco di codice per restare in ascolto di modifiche sul database firestore
2) Da file face_recognition.ipynb, avviare il blocco di codice per l'esecuzione dell'algoritmo di face detection e recognition
3) Da file pepper.ipynb, avviare il blocco di codice con "Da far partire per iniziare il lavoro svolto" per restare in ascolto di messaggi da alexa e face recognition

