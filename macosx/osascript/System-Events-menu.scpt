tell application "System Events"
	tell process "Firefox"
		name of every menu of menu bar 1
		name of every menu item of menu 1 of menu bar 1
		name of first menu bar item of menu bar 1
		name of last menu bar item of menu bar 1
	end tell
end tell
