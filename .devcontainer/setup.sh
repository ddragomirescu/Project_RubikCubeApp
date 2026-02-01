#!/bin/bash

# Update package list
apt-get update

# Install build dependencies required for kociemba (C extensions)
apt-get install -y \
    gcc \
    g++ \
    python3-dev \
    build-essential

# Clean up apt cache to reduce image size
rm -rf /var/lib/apt/lists/*

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

echo "Dev container setup complete!"
