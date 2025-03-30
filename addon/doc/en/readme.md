# Battery Level Announcer
## By Vitor Bruski
The **Battery Level Announcer** is an NVDA add-on that announces the battery level at configurable intervals using sound and/or speech. It offers flexible options to customize the announcements.
## Features
- Configurable announcement intervals;
- Announcement modes;
- Customizable battery check interval;
- Support for custom sounds for each percentage.
## Usage
After installation, configure the add-on through the menu **NVDA > Preferences > Settings > Battery Level Announcer**. The available options are:
- **Battery check interval (seconds):** Set how many seconds the add-on waits between each battery level check. The lower the value, the higher the CPU usage.
- **Announcement interval:** Choose from:
  - Disabled; No announcements.
  - 5% (announces at 5%, 10%, 15%, etc.)
  - 10% (announces at 10%, 20%, 30%, etc.)
  - 20% (announces at 20%, 40%, 60%, etc.)
  - 25% (announces at 25%, 50%, 75%, 100%)
  - 50% (announces at 50%, 100%)
  - Only when battery is full (announces only at 100%)
- **Announcement mode:** Select between:
  - Speech only;
  - Sound only;
  - Sound and speech.
- **Select announcement sound:** Choose a WAV file from the `sounds\` folder for announcements.
- **Use custom sounds for each percentage:** Check this box to use specific WAV files (e.g., 5.wav, 10.wav) in the `sounds\custom\` folder, corresponding to the chosen interval.
- **Open sounds folder:** Opens the `sounds\` folder in the file explorer, so you can use your own sounds.
- **Open custom sounds folder:** Opens the `sounds\custom\` folder.
## Requirements
- NVDA version 2019.3 or higher.
- Windows operating system with battery support (e.g., laptops).
## License
Licensed under the [GNU General Public License v2 (GPLv2)](https:\\www.gnu.org\licenses\gpl-2.0.html).