#!/bin/bash

# Function to check if MongoDB is installed
check_mongodb_installed() {
    if command -v mongod >/dev/null 2>&1; then
        echo "✅ MongoDB is already installed."
        return 0
    else
        echo "⚠️ MongoDB is not installed. Installing MongoDB..."
        install_mongodb
    fi
}

# Function to install MongoDB
install_mongodb() {
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        # Ubuntu/Debian
        sudo apt update
        sudo apt install -y mongodb
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        # macOS with Homebrew
        if ! command -v brew >/dev/null 2>&1; then
            echo "❌ Homebrew not found. Please install Homebrew first: https://brew.sh"
            exit 1
        fi
        brew tap mongodb/brew
        brew install mongodb-community
    else
        echo "❌ Unsupported OS. Please install MongoDB manually."
        exit 1
    fi
}

# Function to start MongoDB
start_mongodb() {
    echo "🚀 Starting MongoDB..."
    if [[ "$OSTYPE" == "linux-gnu"* ]]; then
        sudo systemctl start mongodb
    elif [[ "$OSTYPE" == "darwin"* ]]; then
        brew services stop mongodb-community@7.0
    fi
    sleep 3
}

# Start your backend server
start_backend() {
    echo "📦 Starting Backend..."
    cd backend || exit
    npm install
    npm start
}

check_mongodb_installed
start_mongodb
start_backend
