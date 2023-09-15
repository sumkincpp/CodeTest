#!/bin/bash

if [ -z "$1" ]; then
  echo "Please provide a folder or file as a parameter."
  exit 1
fi

desired_location="$1"

find "$desired_location" -type d -exec chmod 0755 {} +
find "$desired_location" -type f -exec chmod 0644 {} +
