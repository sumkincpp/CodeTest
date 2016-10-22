

osascript -e "the clipboard"

osascript -e "set volume output volume 15"
osascript -e 'set volume output muted true'
osascript -e 'set volume output muted false'

osascript -e 'tell app "Finder" to get disks'
osascript -e 'tell app "Finder" to empty trash'
osascript -e 'tell app "Finder" to restart'

osascript -e 'quit application "GrowlSafari"'
osascript -e 'tell application "XXX" to hide'

# Speeking what are you~
osascript -e 'say "what are you doing" using "alex"'
