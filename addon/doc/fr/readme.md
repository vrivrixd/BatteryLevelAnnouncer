# Annonciateur du Niveau de Batterie
## Par Vitor Bruski
L'**Annonciateur du Niveau de Batterie** est un module complémentaire pour NVDA qui annonce le niveau de la batterie à des intervalles configurables en utilisant un son et/ou la voix. Il offre des options flexibles pour personnaliser les annonces.
## Fonctionnalités
- Intervalles d'annonce configurables ;
- Modes d'annonce ;
- Intervalle de vérification de la batterie personnalisable ;
- Support des sons personnalisés pour chaque pourcentage.
## Utilisation
Après l'installation, configurez le module via le menu **NVDA > Préférences > Paramètres > Annonciateur du Niveau de Batterie**. Les options disponibles sont :
- **Intervalle de vérification de la batterie (secondes) :** Définissez combien de secondes le module attend entre chaque vérification du niveau de la batterie. Plus la valeur est faible, plus la consommation de CPU est élevée.
- **Intervalle d'annonce :** Choisissez parmi :
  - Désactivé ; Pas d'annonces.
  - 5 % (annonce à 5 %, 10 %, 15 %, etc.)
  - 10 % (annonce à 10 %, 20 %, 30 %, etc.)
  - 20 % (annonce à 20 %, 40 %, 60 %, etc.)
  - 25 % (annonce à 25 %, 50 %, 75 %, 100 %)
  - 50 % (annonce à 50 %, 100 %)
  - Seulement lorsque la batterie est pleine (annonce uniquement à 100 %)
- **Mode d'annonce :** Sélectionnez entre :
  - Voix uniquement ;
  - Son uniquement ;
  - Son et voix.
- **Sélectionner un son d'annonce :** Choisissez un fichier WAV dans le dossier `sounds\` pour les annonces.
- **Utiliser des sons personnalisés pour chaque pourcentage :** Cochez cette case pour utiliser des fichiers WAV spécifiques (ex. : 5.wav, 10.wav) dans le dossier `sounds\custom\`, correspondant à l'intervalle choisi.
- **Ouvrir le dossier des sons :** Ouvre le dossier `sounds\` dans l'explorateur de fichiers, pour que vous puissiez utiliser vos propres sons.
- **Ouvrir le dossier des sons personnalisés :** Ouvre le dossier `sounds\custom\`.
## Exigences
- Version de NVDA 2019.3 ou supérieure.
- Système d'exploitation Windows avec prise en charge de la batterie (ex. : ordinateurs portables).
## Licence
Licencié sous la [GNU General Public License v2 (GPLv2)](https:\\www.gnu.org\licenses\gpl-2.0.html).