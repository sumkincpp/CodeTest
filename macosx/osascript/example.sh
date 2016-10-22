
osascript -e 'display notification "Execution complete." with title "Done."'

osascript -e "the clipboard"

osascript -e "set volume output volume 15"
osascript -e 'set volume output muted true'
osascript -e 'set volume output muted false'

osascript -e 'tell app "Finder" to get disks'
osascript -e 'tell app "Finder" to empty trash'
osascript -e 'tell app "Finder" to restart'

osascript -e 'quit app "GrowlSafari"'
osascript -e 'tell app "XXX" to hide'

osascript -e 'tell app "Keynote" to show next'
osascript -e 'tell app "Keynote" to show previous'
osascript -e 'tell app "Keynote" to start slideshow'

# Speeking what are you~
osascript -e 'say "what are you doing" using "alex"'

# Keystrokes -->
osascript -e 'tell application "System Events" to keystroke tab';
osascript -e 'tell application "System Events" to keystroke "date\n"';
osascript -e 'tell application "System Events" to delay 0.5';

# ---------------------------------------------------------

$ osascript -e "id of app \"Finder\"";
com.apple.finder

$ osascript -e 'output volume of (get volume settings)'
13
