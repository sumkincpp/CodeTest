
osascript -e 'open location "$1"'

osascript -e 'display notification "Execution complete." with title "Done."'
osascript -e 'display dialog "What is your name?" default answer ""'

osascript -e "the clipboard"

osascript -e "set volume output volume 15"
osascript -e 'set volume output muted true'
osascript -e 'set volume output muted false'

osascript -e 'tell app "Finder" to get disks'
osascript -e 'tell app "Finder" to empty trash'
osascript -e 'tell app "Finder" to restart'
osascript -e 'tell app "Finder" to eject the disks'
osascript -e 'tell app "Finder" to eject (every disk whose ejectable is true)'

osascript -e 'tell application "ScreenSaverEngine"' -e 'activate' -e 'end tell'

osascript -e 'quit app "XXX"'
osascript -e 'tell app "XXX" to quit'
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
osascript -e 'tell application "iTunes" to artist of current track as string'
osascript -e 'tell application "iTunes" to name of current track as string'

osascript -e 'tell application "Safari" to return URL of front document'
osascript -e 'tell application "Safari" to return name of front document'

osascript -e 'tell application "Google Chrome" to reload active tab of window 1';

# Speeking what are you~
osascript -e 'say "what are you doing" using "alex"'

# Keystrokes -->
osascript -e 'tell application "System Events" to keystroke (key code 124)'
osascript -e 'tell application "System Events" to keystroke tab'
osascript -e 'tell application \"System Events\" to keystroke return'
osascript -e 'tell application "System Events" to keystroke "date\n"'
osascript -e 'tell application "System Events" to keystroke the clipboard as text'
# full screen
osascript -e 'tell application "System Events" to keystroke "f" using {command down, option down}'

osascript -e 'tell application "System Events" to set volume input volume 0'
osascript -e 'tell application "System Events" to set volume input volume 1'

osascript -e 'tell application "System Events" to delay 0.5';
osascript -e 'tell application "System Events" to log out'
osascript -e 'tell application "System Events" to shut down'
osascript -e 'tell application "System Events" to sleep'

osascript -e 'tell application "System Events" to get name of every application process'

osascript -e 'tell application "System Events" to set the autohide of the dock preferences to true'
osascript -e 'tell application "System Events" to set the autohide of the dock preferences to false'

osascript -e 'tell application "System Events" to delete login item "XXX"'

osascript -e "tell application \"System Events\" to make new login item with properties { path: \"/Users/$USER/Applications/$app\", hidden:true } at end"


# Volume
## Kill the annoying terminal bell
osascript -e 'set volume alert volume 0'
osascript -e 'output volume of (get volume settings)'
osascript -e 'get volume settings'

# log to /var/log/system.log
osascript -e 'log "hello message"'

#
osascript -e 'tell application "Firefox" to get windows'
osascript -e 'tell application "Firefox" to get properties'
osascript -e 'tell application "Firefox" to get the bounds of the first window'

osascript -e 'tell application "Firefox" to count (every window whose (closeable is true))'

# ---------------------------------------------------------

$ osascript -e "id of app \"Finder\"";
com.apple.finder

$ osascript -e 'output volume of (get volume settings)'
13

# ---------------------------------------------------------
# New tab ->
osascript -e 'activate application "iTerm"'
osascript -e 'tell application "System Events" to keystroke "t" using command down'
