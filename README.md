# News Headline Sentiment Analysis with TF-IDF and Neural Networks

This project analyzes sentiment in news headlines using both TF-IDF and neural network approaches. It classifies headlines into three sentiment categories: positive, neutral, and negative.

## Easy to Get Started

We've created simple ways to run this project depending on your needs:

### Quick Start (Recommended)

#### On Linux/Mac:

```bash
# Make the startup script executable
chmod +x startup.sh

# Run the startup script
./startup.sh
```

#### On Windows:

```batch
# Run the Windows startup script
startup.bat
```

The startup script will:

1. Check your Python version
2. Set up a virtual environment
3. Install the necessary dependencies
4. Give you options to run the web application or analyze headlines

### Running the Application Manually

After installation, use the simple `run.py` script:

```bash
# Run the web application
python run.py webapp

# Analyze a news headline
python run.py analyze --headline "Stock markets rise as inflation cools"
```

### Docker Option

For a containerized setup:

```bash
# Build and run with Docker Compose
docker-compose -f docker-compose.simple.yml up --build

# Or use the run.py helper
python run.py docker --build
```

## Project Structure

```
Headline-Sentiment/
├── data/                      # Data files
│   ├── raw/                   # Raw data
│   └── processed/             # Processed data
├── models/                    # Saved model files
├── notebooks/                 # Jupyter notebooks
├── src/                       # Source code
├── webapp/                    # Web application
├── startup.sh                 # Linux/Mac startup script
├── startup.bat                # Windows startup script
├── docker-compose.simple.yml  # Simple Docker setup
├── Dockerfile                 # Docker config
└── run.py                     # All-in-one runner script
```

## Example: Analyzing a Single Headline

```bash
# Analyze directly from command line
python analyze_headline.py --headline "Stock markets rise as inflation cools"
```

## Performance

| Model Type       | Speed  | Accuracy | Best For                          |
|------------------|--------|----------|-----------------------------------|
| TF-IDF + NN      | Fast   | Good     | Quick analysis, limited resources |
| Neural Network   | Medium | Better   | More accurate results             |

## License

This project is licensed under the MIT License - see the LICENSE file for details.
