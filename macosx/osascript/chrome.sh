osascript <<EOF
tell application "Google Chrome"
	open location "http://example.com"
	activate
	execute front window's active tab javascript "alert('example');"
end tell
EOF
