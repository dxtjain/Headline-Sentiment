#!/usr/bin/env python3
"""
Headline Sentiment Analyzer - Command Line Interface
Analyze sentiment of news headlines directly from the command line.
"""

import argparse
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import sys
from src.analyze_sentiment import analyze_text, display_result

def main():
    parser = argparse.ArgumentParser(description="Headline Sentiment Analyzer - Command Line Tool")
    parser.add_argument("--headline", "-hd", type=str, required=True, help="News headline to analyze")
    parser.add_argument("--model", "-m", type=str, default="models/headline_model.h5", 
                        help="Path to the trained model (default: models/headline_model.h5)")
    args = parser.parse_args()
    
    try:
        # Load the vectorizer
        print("Loading dataset...")
        doc = pd.read_csv("data/raw/all-data.csv", header=None)
        vectorizer = TfidfVectorizer()
        vectorizer.fit(doc[1])
        
        # Analyze the headline
        result = analyze_text(args.headline, vectorizer, args.model)
        display_result(args.headline, result)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 