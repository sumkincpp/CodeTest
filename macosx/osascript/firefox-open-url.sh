tell application "Firefox" to activate
tell application "System Events" to keystroke "n" using command down
delay 3
tell application "Firefox"
    open location "http://rubyquicktips.tumblr.com/"
end tell
