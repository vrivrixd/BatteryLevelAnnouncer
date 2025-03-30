# Anunciador do Nível da Bateria
## Por Vitor Bruski
O **Anunciador do Nível da Bateria** é um complemento para o NVDA que anuncia o nível da bateria em intervalos configuráveis usando som e/ou fala. Ele oferece opções flexíveis para personalizar os anúncios.
## Recursos
- Intervalos de anúncio configuráveis;
- Modos de anúncio;
- Intervalo de verificação da bateria personalizável;
- Suporte a sons personalizados para cada porcentagem.
## Uso
Após a instalação, configure o complemento através do menu **NVDA > Preferências > Configurações > Anunciador do Nível da Bateria**. As opções disponíveis são:
- **Intervalo de verificação da bateria (segundos):** Defina quantos segundos o add-on espera entre cada verificação do nível da bateria. Quanto menor o valor, mais alto será o consumo de CPU.
- **Intervalo de anúncio:** Escolha entre:
  - Desativado; Sem anúncios.
  - 5% (anuncia em 5%, 10%, 15%, etc.)
  - 10% (anuncia em 10%, 20%, 30%, etc.)
  - 20% (anuncia em 20%, 40%, 60%, etc.)
  - 25% (anuncia em 25%, 50%, 75%, 100%)
  - 50% (anuncia em 50%, 100%)
  - Apenas quando a bateria estiver cheia (anuncia apenas em 100%)
- **Modo de anúncio:** Selecione entre:
  - Apenas fala;
  - Apenas som;
  - Som e fala.
- **Selecionar som de anúncio:** Escolha um arquivo WAV da pasta `sounds\` para anúncios.
- **Usar sons personalizados para cada porcentagem:** Marque esta caixa para usar arquivos WAV específicos (ex.: 5.wav, 10.wav) na pasta `sounds\custom\`, correspondentes ao intervalo escolhido.
- **Abrir pasta de sons:** Abre a pasta `sounds\` no explorador de arquivos, para que você possa usar seus próprios sons.
- **Abrir pasta de sons personalizados:** Abre a pasta `sounds\custom\`.
## Requisitos
- Versão do NVDA 2019.3 ou superior.
- Sistema operacional Windows com suporte a bateria (ex.: laptops).
## Licença
Licenciado sob a [GNU General Public License v2 (GPLv2)](https:\\www.gnu.org\licenses\gpl-2.0.html).