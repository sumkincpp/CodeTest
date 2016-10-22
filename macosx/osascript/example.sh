
osascript -e 'tell app "Finder" to get disks'

osascript -e "the clipboard"

osascript -e 'set volume output muted true'
osascript -e 'set volume output muted false'

osascript -e 'tell app "Finder" to empty trash'

osascript -e 'quit application "GrowlSafari"'

# Speeking what are you~
osascript -e 'say "what are you doing" using "alex"'
