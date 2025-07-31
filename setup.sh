#!/bin/bash

# This script will help setup generate_commit.py to the path 
# so it is accessible from anywhere in the system.

# Usage: ./setup.sh

sudo cp generate_commit.py /usr/local/bin/generate_commit
sudo chmod +x /usr/local/bin/generate_commit
echo "generate_commit.py has been installed to /usr/local/bin as 'generate_commit'."

# you'll have to run this script with sudo privileges
# also ensure that /usr/local/bin is in your PATH

# you have to create an api key from groq 

# export GROQ_API_KEY="your_api_key_here"