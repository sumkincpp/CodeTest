osascript <<EOF
tell application "Safari"
    open location "http://example.com"
    activate
    do JavaScript "alert('example');" in current tab of first window
end tell
EOF
