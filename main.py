#!/usr/bin/env python3
"""
Headline Sentiment Analyzer - Main Entry Point
This script serves as the main entry point for the Headline Sentiment Analyzer project.
"""

import os
import argparse
import sys

def main():
    """Main entry point for the Headline Sentiment Analyzer application"""
    parser = argparse.ArgumentParser(description="Headline Sentiment Analyzer - Analyze sentiment in news headlines")
    parser.add_argument("--analyze", "-a", type=str, help="Analyze a specific headline")
    parser.add_argument("--file", "-f", type=str, help="Analyze headlines from a file")
    parser.add_argument("--webapp", "-w", action="store_true", help="Launch the web application")
    parser.add_argument("--model", "-m", type=str, default="headline_model.h5", 
                        help="Path to the trained model (default: headline_model.h5)")
    args = parser.parse_args()
    
    if args.webapp:
        print("Launching web application...")
        # This would normally import and run the web app
        from webapp import app
        app.run(debug=False, host='0.0.0.0', port=8000)
    elif args.analyze:
        print(f"Analyzing headline: {args.analyze}")
        # This would normally import and use the analyzer
        from src.analyze_sentiment import analyze_text, display_result
        import pandas as pd
        from sklearn.feature_extraction.text import TfidfVectorizer
        
        # Load the vectorizer
        doc = pd.read_csv("data/raw/all-data.csv", header=None)
        vectorizer = TfidfVectorizer()
        vectorizer.fit(doc[1])
        
        # Analyze headline
        result = analyze_text(args.analyze, vectorizer, args.model)
        display_result(args.analyze, result)
    elif args.file:
        print(f"Analyzing headlines from file: {args.file}")
        # This would normally import and analyze a file
        pass
    else:
        parser.print_help()

if __name__ == "__main__":
    main() 