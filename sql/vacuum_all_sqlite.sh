find Library -type f -exec sh -c "grep '^SQLite format 3' \"{}\" && echo ' VACUUM;' | sqlite3 \"{}\" " \;
