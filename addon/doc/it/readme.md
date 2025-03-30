# Annunciatore del Livello della Batteria
## Di Vitor Bruski
L'**Annunciatore del Livello della Batteria** è un componente aggiuntivo per NVDA che annuncia il livello della batteria a intervalli configurabili usando suono e/o voce. Offre opzioni flessibili per personalizzare gli annunci.
## Caratteristiche
- Intervalli di annuncio configurabili;
- Modalità di annuncio;
- Intervallo di controllo della batteria personalizzabile;
- Supporto per suoni personalizzati per ogni percentuale.
## Uso
Dopo l'installazione, configura il componente aggiuntivo tramite il menu **NVDA > Preferenze > Impostazioni > Annunciatore del Livello della Batteria**. Le opzioni disponibili sono:
- **Intervallo di controllo della batteria (secondi):** Definisci quanti secondi il componente aggiuntivo aspetta tra ogni controllo del livello della batteria. Più basso è il valore, maggiore è il consumo della CPU.
- **Intervallo di annuncio:** Scegli tra:
  - Disattivato; Nessun annuncio.
  - 5% (annuncia al 5%, 10%, 15%, ecc.)
  - 10% (annuncia al 10%, 20%, 30%, ecc.)
  - 20% (annuncia al 20%, 40%, 60%, ecc.)
  - 25% (annuncia al 25%, 50%, 75%, 100%)
  - 50% (annuncia al 50%, 100%)
  - Solo quando la batteria è piena (annuncia solo al 100%)
- **Modalità di annuncio:** Seleziona tra:
  - Solo voce;
  - Solo suono;
  - Suono e voce.
- **Seleziona suono di annuncio:** Scegli un file WAV dalla cartella `sounds\` per gli annunci.
- **Usa suoni personalizzati per ogni percentuale:** Spunta questa casella per usare file WAV specifici (es.: 5.wav, 10.wav) nella cartella `sounds\custom\`, corrispondenti all'intervallo scelto.
- **Apri cartella dei suoni:** Apre la cartella `sounds\` nell'esplora file, per consentirti di usare i tuoi suoni.
- **Apri cartella dei suoni personalizzati:** Apre la cartella `sounds\custom\`.
## Requisiti
- Versione di NVDA 2019.3 o superiore.
- Sistema operativo Windows con supporto per la batteria (es.: portatili).
## Licenza
Licenziato sotto la [GNU General Public License v2 (GPLv2)](https:\\www.gnu.org\licenses\gpl-2.0.html).