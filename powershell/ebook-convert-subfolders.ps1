# Convert all files in subfolders from XXX.pdf to XXX.txt with ebook-convert
Get-ChildItem -Recurse -Filter "*.pdf" | ForEach-Object { ebook-convert $_.FullName ($_.FullName -replace '\.pdf$','.txt') }
