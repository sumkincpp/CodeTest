
osascript -e 'open location "$1"'

osascript -e 'display notification "Execution complete." with title "Done."'

osascript -e "the clipboard"

osascript -e "set volume output volume 15"
osascript -e 'set volume output muted true'
osascript -e 'set volume output muted false'

osascript -e 'tell app "Finder" to get disks'
osascript -e 'tell app "Finder" to empty trash'
osascript -e 'tell app "Finder" to restart'
osascript -e 'tell app "Finder"' -e 'eject the disks' -e 'end tell'

osascript -e 'tell application "ScreenSaverEngine"' -e 'activate' -e 'end tell'

osascript -e 'quit app "XXX"'
osascript -e 'tell app "XXX" to activate'
osascript -e 'tell app "XXX" to hide'

osascript -e 'tell app "Keynote" to show next'
osascript -e 'tell app "Keynote" to show previous'
osascript -e 'tell app "Keynote" to start slideshow'

osascript -e 'tell application "iTunes" to pause'
osascript -e 'tell application "iTunes" to play'
osascript -e 'tell application "iTunes" to next track'
osascript -e 'tell application "iTunes" to previous track'
# fast-forward to 30 seconds
osascript -e 'tell application "iTunes" to set player position to player position + 30'

# Speeking what are you~
osascript -e 'say "what are you doing" using "alex"'

# Keystrokes -->
osascript -e 'tell application "System Events" to keystroke tab';
osascript -e 'tell application "System Events" to keystroke "date\n"';
osascript -e 'tell application "System Events" to delay 0.5';

# Volume
## Kill the annoying terminal bell
osascript -e 'set volume alert volume 0'
osascript -e 'output volume of (get volume settings)'
osascript -e 'get volume settings'

# ---------------------------------------------------------

$ osascript -e "id of app \"Finder\"";
com.apple.finder

$ osascript -e 'output volume of (get volume settings)'
13
