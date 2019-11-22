Get-Content vscode-extensions.txt | ForEach-Object { code --install-extension $_ }
