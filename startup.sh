#!/bin/bash
# Headline Sentiment Analyzer - Startup Script

echo "==================================================================="
echo "        Headline Sentiment Analyzer - Setup & Launch Script        "
echo "==================================================================="
echo ""

# Check Python version
echo "Checking Python installation..."
if command -v python3 &>/dev/null; then
    PYTHON_CMD=python3
    echo "Found Python: $(python3 --version)"
elif command -v python &>/dev/null; then
    PYTHON_CMD=python
    echo "Found Python: $(python --version)"
else
    echo "Error: Python not found. Please install Python 3.7 or higher"
    exit 1
fi

# Create virtual environment
echo ""
echo "Setting up virtual environment..."
if [ ! -d "venv" ]; then
    $PYTHON_CMD -m venv venv
    echo "Virtual environment created."
else
    echo "Virtual environment already exists."
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

echo ""
echo "==================================================================="
echo "                          Setup Complete                           "
echo "==================================================================="
echo ""

# Provide options to run
echo "What would you like to do?"
echo "1) Run the web application"
echo "2) Analyze a headline"
echo "3) Exit"

read -p "Enter your choice (1-3): " choice

case $choice in
    1)
        echo ""
        echo "Starting web application..."
        python main.py --webapp
        ;;
    2)
        echo ""
        read -p "Enter a headline to analyze: " headline
        python analyze_headline.py --headline "$headline"
        ;;
    3)
        echo "Exiting..."
        ;;
    *)
        echo "Invalid choice. Exiting..."
        ;;
esac

# Deactivate virtual environment
deactivate 