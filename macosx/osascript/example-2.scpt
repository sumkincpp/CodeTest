--Integer Variables
set theFirstNumber to 3
set the theSecondNumber to 2

--Variable Operations
set theAnswer to (theFirstNumber + theSecondNumber)
set theAnswer to (theAnswer + 1)

--String Variables
set theString to "3+2+1="

--Display Dialog
tell application "Finder"
	
	display dialog theString & theAnswer
	
end tell
