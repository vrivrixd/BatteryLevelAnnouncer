# Anunciador del Nivel de Batería
## Por Vitor Bruski
El **Anunciador del Nivel de Batería** es un complemento para NVDA que anuncia el nivel de la batería en intervalos configurables usando sonido y/o voz. Ofrece opciones flexibles para personalizar los anuncios.
## Recursos
- Intervalos de anuncio configurables;
- Modos de anuncio;
- Intervalo de verificación de la batería personalizable;
- Soporte para sonidos personalizados para cada porcentaje.
## Uso
Tras la instalación, configure el complemento a través del menú **NVDA > Preferencias > Configuración > Anunciador del Nivel de Batería**. Las opciones disponibles son:
- **Intervalo de verificación de la batería (segundos):** Defina cuántos segundos espera el complemento entre cada verificación del nivel de la batería. Cuanto menor sea el valor, mayor será el consumo de CPU.
- **Intervalo de anuncio:** Elija entre:
  - Desactivado; Sin anuncios.
  - 5% (anuncia en 5%, 10%, 15%, etc.)
  - 10% (anuncia en 10%, 20%, 30%, etc.)
  - 20% (anuncia en 20%, 40%, 60%, etc.)
  - 25% (anuncia en 25%, 50%, 75%, 100%)
  - 50% (anuncia en 50%, 100%)
  - Solo cuando la batería esté llena (anuncia solo en 100%)
- **Modo de anuncio:** Seleccione entre:
  - Solo voz;
  - Solo sonido;
  - Sonido y voz.
- **Seleccionar sonido de anuncio:** Elija un archivo WAV de la carpeta `sounds\` para los anuncios.
- **Usar sonidos personalizados para cada porcentaje:** Marque esta casilla para usar archivos WAV específicos (ej.: 5.wav, 10.wav) en la carpeta `sounds\custom\`, correspondientes al intervalo elegido.
- **Abrir carpeta de sonidos:** Abre la carpeta `sounds\` en el explorador de archivos, para que pueda usar sus propios sonidos.
- **Abrir carpeta de sonidos personalizados:** Abre la carpeta `sounds\custom\`.
## Requisitos
- Versión de NVDA 2019.3 o superior.
- Sistema operativo Windows con soporte para batería (ej.: portátiles).
## Licencia
Licenciado bajo la [GNU General Public License v2 (GPLv2)](https:\\www.gnu.org\licenses\gpl-2.0.html).