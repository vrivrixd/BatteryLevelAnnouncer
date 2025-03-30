# batteryLevelAnnouncer.py
# Battery Level Announcer - Version 1.0
# A global plugin for NVDA that announces the battery level at configurable intervals using a custom WAV sound and/or speech,
# without announcing the initial level on NVDA startup, with robust translation support and custom sound per percentage.
# Copyright (C) 2025 Vitor Bruski
# Licensed under the GNU General Public License v2 (GPLv2)

import globalPluginHandler
import threading
import psutil
import nvwave
import os
import config
import gui
import ui
import wx
import addonHandler
from logHandler import log

# Initialize translation support
addonHandler.initTranslation()

# Default configuration specification
confSpec = {
    "checkInterval": "integer(default=1)",  # Default check interval: 1 second
    "interval": "string(default=5)",  # Default announcement interval: 5%
    "announceMode": "string(default=soundAndSpeech)",  # Default mode: sound and speech
    "soundFile": "string(default=beep.wav)",  # Default sound file: beep.wav
    "useCustomSounds": "boolean(default=False)"  # Use custom sounds per percentage: default False
}

class SettingsPanel(gui.SettingsPanel):
    # Title of the settings panel
    title = _("Battery Level Announcer")

    def makeSettings(self, settingsSizer):
        sHelper = gui.guiHelper.BoxSizerHelper(self, sizer=settingsSizer)
        
        # Label for battery check interval in seconds
        checkIntervalLabel = _("Battery check interval (seconds):")
        self.checkIntervalText = sHelper.addLabeledControl(
            checkIntervalLabel,
            wx.TextCtrl,
            value=str(config.conf["batteryLevelAnnouncer"]["checkInterval"])
        )

        # Label for announcement interval
        intervalLabel = _("Announcement interval:")
        # Dictionary mapping internal keys to translated strings
        self.intervalOptions = {
            "disabled": _("Disabled"),
            "5": _("5%"),
            "10": _("10%"),
            "20": _("20%"),
            "25": _("25%"),
            "50": _("50%"),
            "full": _("Only when battery is full")  # New option
        }
        self.intervalChoice = sHelper.addLabeledControl(
            intervalLabel,
            wx.Choice,
            choices=list(self.intervalOptions.values())
        )
        currentInterval = config.conf["batteryLevelAnnouncer"]["interval"]
        for index, (key, value) in enumerate(self.intervalOptions.items()):
            if key == currentInterval:
                self.intervalChoice.SetSelection(index)
                break
        else:
            self.intervalChoice.SetSelection(0)

        # Label for announcement mode
        modeLabel = _("Announcement mode:")
        self.modeOptions = {
            "speech": _("Speech only"),
            "sound": _("Sound only"),
            "soundAndSpeech": _("Sound and Speech")
        }
        self.modeChoice = sHelper.addLabeledControl(
            modeLabel,
            wx.Choice,
            choices=list(self.modeOptions.values())
        )
        currentMode = config.conf["batteryLevelAnnouncer"]["announceMode"]
        for index, (key, value) in enumerate(self.modeOptions.items()):
            if key == currentMode:
                self.modeChoice.SetSelection(index)
                break
        else:
            self.modeChoice.SetSelection(0)
        self.modeChoice.Bind(wx.EVT_CHOICE, self.onModeChange)

        # Checkbox for using custom sounds per percentage
        self.useCustomSoundsCheckBox = sHelper.addItem(wx.CheckBox(self, label=_("Use custom sounds for each percentage")))
        self.useCustomSoundsCheckBox.SetValue(config.conf["batteryLevelAnnouncer"]["useCustomSounds"])
        self.useCustomSoundsCheckBox.Bind(wx.EVT_CHECKBOX, self.onUseCustomSoundsChange)

        # Label for general sound selection
        self.soundLabel = _("Select announcement sound:")
        soundDir = os.path.join(os.path.dirname(__file__), "sounds")
        soundFiles = [f for f in os.listdir(soundDir) if f.endswith(".wav") and not os.path.isdir(os.path.join(soundDir, f))]
        if not soundFiles:
            # Message when no sounds are available
            soundFiles = [_("No sounds available")]
        self.soundChoice = sHelper.addLabeledControl(
            self.soundLabel,
            wx.Choice,
            choices=soundFiles
        )
        currentSound = config.conf["batteryLevelAnnouncer"]["soundFile"]
        if currentSound in soundFiles:
            self.soundChoice.SetStringSelection(currentSound)
        else:
            self.soundChoice.SetSelection(0)
        self.soundChoice.Bind(wx.EVT_CHOICE, self.onSoundChange)

        # Button to open the general sounds folder
        self.openSoundsButton = sHelper.addItem(wx.Button(self, label=_("Open sounds folder")))
        self.openSoundsButton.Bind(wx.EVT_BUTTON, self.onOpenSoundsFolder)

        # Button to open the custom sounds folder
        self.openCustomSoundsButton = sHelper.addItem(wx.Button(self, label=_("Open custom sounds folder")))
        self.openCustomSoundsButton.Bind(wx.EVT_BUTTON, self.onOpenCustomSoundsFolder)

        # Update initial visibility
        self.updateSoundOptionsVisibility()

    def onModeChange(self, evt):
        # Update sound options visibility when mode changes
        self.updateSoundOptionsVisibility()
        evt.Skip()

    def onUseCustomSoundsChange(self, evt):
        # Update visibility and check the custom folder when checkbox changes
        useCustomSounds = self.useCustomSoundsCheckBox.GetValue()
        if useCustomSounds:
            customSoundDir = os.path.join(os.path.dirname(__file__), "sounds", "custom")
            # Create custom folder if it doesn't exist
            if not os.path.exists(customSoundDir):
                try:
                    os.makedirs(customSoundDir, exist_ok=True)
                    # Warning when custom folder doesn't exist and suggest restarting
                    gui.messageBox(
                        _("The custom sounds folder was not found and may have been deleted. It has been recreated. Please restart NVDA to ensure it is fully initialized, then add WAV files (e.g., 5.wav, 10.wav, etc.) to 'sounds/custom'."),
                        _("Warning"),
                        wx.OK | wx.ICON_WARNING
                    )
                except Exception as e:
                    log.error(f"Error creating custom folder: {e}")
            # Check if the folder is empty
            elif not any(f.endswith(".wav") for f in os.listdir(customSoundDir)):
                # Alert when custom folder is empty
                gui.messageBox(
                    _("The custom sounds folder is empty. Please add WAV files (e.g., 5.wav, 10.wav, etc.) to the 'sounds/custom' folder for each percentage."),
                    _("Warning"),
                    wx.OK | wx.ICON_WARNING
                )
        self.updateSoundOptionsVisibility()
        evt.Skip()

    def onSoundChange(self, evt):
        # Play the selected sound from the ComboBox
        selectedSound = self.soundChoice.GetStringSelection()
        if selectedSound != _("No sounds available"):
            soundFile = os.path.join(os.path.dirname(__file__), "sounds", selectedSound)
            if os.path.exists(soundFile):
                try:
                    nvwave.playWaveFile(soundFile)
                except Exception as e:
                    log.error(f"Error playing sound: {e}")
                    # Error message if sound playback fails
                    gui.messageBox(_("Failed to play sound: {error}").format(error=e), 
                                   _("Error"), wx.OK | wx.ICON_ERROR)
        evt.Skip()

    def updateSoundOptionsVisibility(self):
        # Show or hide sound options based on announcement mode and custom sounds checkbox
        selectedModeIndex = self.modeChoice.GetSelection()
        selectedMode = list(self.modeOptions.keys())[selectedModeIndex]
        isSpeechOnly = selectedMode == "speech"
        useCustomSounds = self.useCustomSoundsCheckBox.GetValue()

        self.useCustomSoundsCheckBox.Show(not isSpeechOnly)
        # Hide soundChoice and openSoundsButton if useCustomSounds is checked
        self.soundChoice.Show(not isSpeechOnly and not useCustomSounds)
        self.openSoundsButton.Show(not isSpeechOnly and not useCustomSounds)
        self.openCustomSoundsButton.Show(not isSpeechOnly and useCustomSounds)

        # Adjust visibility of the sound selection label
        for child in self.GetChildren():
            if isinstance(child, wx.StaticText) and child.GetLabel() == self.soundLabel:
                child.Show(not isSpeechOnly and not useCustomSounds)
                break
        self.Layout()

    def onOpenSoundsFolder(self, evt):
        # Open the general sounds folder in the file explorer
        soundDir = os.path.join(os.path.dirname(__file__), "sounds")
        try:
            os.startfile(soundDir)
        except Exception as e:
            log.error(f"Error opening sounds folder: {e}")
            # Error message if opening the sounds folder fails
            gui.messageBox(_("Failed to open sounds folder: {error}").format(error=e), 
                           _("Error"), wx.OK | wx.ICON_ERROR)

    def onOpenCustomSoundsFolder(self, evt):
        # Open the custom sounds folder in the file explorer
        customSoundDir = os.path.join(os.path.dirname(__file__), "sounds", "custom")
        try:
            os.startfile(customSoundDir)
        except Exception as e:
            log.error(f"Error opening custom sounds folder: {e}")
            # Error message if opening the custom sounds folder fails
            gui.messageBox(_("Failed to open custom sounds folder: {error}").format(error=e), 
                           _("Error"), wx.OK | wx.ICON_ERROR)

    def onSave(self):
        # Validate battery check interval
        try:
            checkInterval = int(self.checkIntervalText.GetValue())
            if checkInterval <= 0:
                raise ValueError("Interval must be a positive integer greater than 0")
            config.conf["batteryLevelAnnouncer"]["checkInterval"] = checkInterval
        except ValueError:
            # Error message for invalid check interval
            gui.messageBox(
                _("Please enter a valid positive integer for the battery check interval (e.g., 1, 2, 3)."),
                _("Invalid Input"),
                wx.OK | wx.ICON_ERROR
            )
            return

        # Save settings using internal keys
        selectedIntervalIndex = self.intervalChoice.GetSelection()
        intervalKey = list(self.intervalOptions.keys())[selectedIntervalIndex]
        config.conf["batteryLevelAnnouncer"]["interval"] = intervalKey
        
        selectedModeIndex = self.modeChoice.GetSelection()
        modeKey = list(self.modeOptions.keys())[selectedModeIndex]
        config.conf["batteryLevelAnnouncer"]["announceMode"] = modeKey
        
        soundSelection = self.soundChoice.GetStringSelection()
        if soundSelection != _("No sounds available"):
            config.conf["batteryLevelAnnouncer"]["soundFile"] = soundSelection
        
        config.conf["batteryLevelAnnouncer"]["useCustomSounds"] = self.useCustomSoundsCheckBox.GetValue()

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    # Last announced level to avoid repetitions, initialized as None
    lastAnnouncedLevel = None
    # Flag to indicate if the plugin should be disabled due to no battery
    isDisabled = False

    def __init__(self):
        super(GlobalPlugin, self).__init__()
        # Register configuration specification
        config.conf.spec["batteryLevelAnnouncer"] = confSpec
        
        # Check if the system has a battery
        if not self.checkBatteryPresence():
            # Schedule warning dialog after NVDA is fully loaded
            wx.CallAfter(self.showNoBatteryWarning)
            self.isDisabled = True
            return

        # Add settings panel to NVDA if battery is present
        gui.settingsDialogs.NVDASettingsDialog.categoryClasses.append(SettingsPanel)
        # Create custom folder on plugin startup if it doesn't exist
        customSoundDir = os.path.join(os.path.dirname(__file__), "sounds", "custom")
        if not os.path.exists(customSoundDir):
            try:
                os.makedirs(customSoundDir, exist_ok=True)
                log.info("Folder 'sounds/custom' created successfully.")
            except Exception as e:
                log.error(f"Error creating custom folder on startup: {e}")
        self.initializeLastAnnouncedLevel()
        self.startBatteryMonitor()

    def checkBatteryPresence(self):
        # Check if the system has a battery (returns True if battery exists, False otherwise)
        try:
            battery = psutil.sensors_battery()
            return battery is not None
        except Exception as e:
            log.error(f"Error checking battery presence: {e}")
            return False

    def showNoBatteryWarning(self):
        # Display warning about no battery and disable the plugin
        wx.MessageBox(
            _("This computer does not have a system battery. The Battery Level Announcer will be disabled."),
            _("No Battery Detected"),
            wx.OK | wx.ICON_INFORMATION
        )

    def initializeLastAnnouncedLevel(self):
        # Initialize the last announced level with the current battery percentage
        try:
            battery = psutil.sensors_battery()
            if battery is not None:
                self.lastAnnouncedLevel = int(battery.percent)
                log.info(f"Initialized lastAnnouncedLevel to {self.lastAnnouncedLevel}%")
            else:
                log.warning("Unable to retrieve initial battery level.")
        except Exception as e:
            log.error(f"Error initializing battery level: {e}")

    def startBatteryMonitor(self):
        # Start the timer to check battery level at configured intervals if not disabled
        if not self.isDisabled and config.conf["batteryLevelAnnouncer"]["interval"] != "disabled":
            self.checkBatteryLevel()
            checkInterval = float(config.conf["batteryLevelAnnouncer"]["checkInterval"])
            self.timer = threading.Timer(checkInterval, self.startBatteryMonitor)
            self.timer.start()

    def checkBatteryLevel(self):
        # Check battery level based on the configured interval
        try:
            battery = psutil.sensors_battery()
            if battery is None:
                log.warning("Unable to retrieve battery information.")
                return

            percent = int(battery.percent)
            interval = config.conf["batteryLevelAnnouncer"]["interval"]
            
            # Handle different interval configurations
            if interval == "full":
                if percent == 100 and percent != self.lastAnnouncedLevel:
                    self.announceBatteryLevel(percent)
                    self.lastAnnouncedLevel = percent
            else:
                intervalValue = int(interval)
                if percent % intervalValue == 0 and percent != self.lastAnnouncedLevel:
                    self.announceBatteryLevel(percent)
                    self.lastAnnouncedLevel = percent

        except Exception as e:
            log.error(f"Error checking battery level: {e}")

    def announceBatteryLevel(self, level):
        # Announce battery level using the configured mode and interval
        mode = config.conf["batteryLevelAnnouncer"]["announceMode"]
        useCustomSounds = config.conf["batteryLevelAnnouncer"]["useCustomSounds"]
        interval = config.conf["batteryLevelAnnouncer"]["interval"]
        
        # Check if level aligns with configured interval
        if interval == "full" and level == 100 or (interval != "full" and level % int(interval) == 0):
            if mode in ("sound", "soundAndSpeech"):
                if useCustomSounds:
                    soundFile = os.path.join(os.path.dirname(__file__), "sounds", "custom", f"{level}.wav")
                else:
                    soundFile = os.path.join(os.path.dirname(__file__), "sounds", config.conf["batteryLevelAnnouncer"]["soundFile"])
                if os.path.exists(soundFile):
                    nvwave.playWaveFile(soundFile)
            
            if mode in ("speech", "soundAndSpeech"):
                # Message announced with the battery level
                ui.message(_("Battery level: {level}%").format(level=level))

    def terminate(self):
        # Stop the timer and remove settings panel on plugin shutdown if not disabled
        if not self.isDisabled:
            if hasattr(self, "timer"):
                self.timer.cancel()
            gui.settingsDialogs.NVDASettingsDialog.categoryClasses.remove(SettingsPanel)
        super(GlobalPlugin, self).terminate()