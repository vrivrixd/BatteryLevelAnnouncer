# Anunciador do Nível da Bateria
## Por Vitor Bruski
O **Anunciador do Nível da Bateria** é um complemento para o NVDA que anuncia o nível da bateria em intervalos configuráveis usando som e/ou voz. Ele oferece opções flexíveis para personalizar os anúncios.
## Recursos
- Intervalos de anúncio configuráveis;
- Modos de anúncio;
- Intervalo de verificação da bateria personalizável;
- Suporte a sons personalizados para cada percentagem.
## Uso
Após a instalação, configure o complemento através do menu **NVDA > Preferências > Configurações > Anunciador do Nível da Bateria**. As opções disponíveis são:
- **Intervalo de verificação da bateria (segundos):** Defina quantos segundos o complemento espera entre cada verificação do nível da bateria. Quanto menor o valor, mais elevado será o consumo de CPU.
- **Intervalo de anúncio:** Escolha entre:
  - Desactivado; Sem anúncios.
  - 5% (anuncia em 5%, 10%, 15%, etc.)
  - 10% (anuncia em 10%, 20%, 30%, etc.)
  - 20% (anuncia em 20%, 40%, 60%, etc.)
  - 25% (anuncia em 25%, 50%, 75%, 100%)
  - 50% (anuncia em 50%, 100%)
  - Apenas quando a bateria estiver cheia (anuncia apenas em 100%)
- **Modo de anúncio:** Seleccione entre:
  - Apenas voz;
  - Apenas som;
  - Som e voz.
- **Seleccionar som de anúncio:** Escolha um ficheiro WAV da pasta `sounds\` para anúncios.
- **Utilizar sons personalizados para cada percentagem:** Marque esta caixa para usar ficheiros WAV específicos (ex.: 5.wav, 10.wav) na pasta `sounds\custom\`, correspondentes ao intervalo escolhido.
- **Abrir pasta de sons:** Abre a pasta `sounds\` no explorador de ficheiros, para que possa usar os seus próprios sons.
- **Abrir pasta de sons personalizados:** Abre a pasta `sounds\custom\`.
## Requisitos
- Versão do NVDA 2019.3 ou superior.
- Sistema operativo Windows com suporte a bateria (ex.: portáteis).
## Licença
Licenciado sob a [GNU General Public License v2 (GPLv2)](https:\\www.gnu.org\licenses\gpl-2.0.html).