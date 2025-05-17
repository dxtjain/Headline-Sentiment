#!/usr/bin/env python3
"""
Headline Sentiment Analyzer - Text Analysis Tool
This script allows you to analyze the sentiment of news headlines
using the trained model.
"""

import argparse
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from keras.models import load_model
import os
import sys
from colorama import init, Fore, Style

# Initialize colorama for colored terminal output
init()

def load_data_and_vectorizer():
    """Load the original dataset to fit the vectorizer"""
    try:
        doc = pd.read_csv("all-data.csv", header=None)
        lines = doc[1]
        
        vectorizer = TfidfVectorizer()
        vectorizer.fit(lines)
        return vectorizer
    except FileNotFoundError:
        print(f"{Fore.RED}Error: Could not find the dataset file 'all-data.csv' in the current directory.{Style.RESET_ALL}")
        print(f"Make sure you're running this script from the project's root directory.")
        sys.exit(1)

def analyze_text(text, vectorizer, model_path="headline_model.h5"):
    """Analyze the sentiment of a given text"""
    try:
        if not os.path.exists(model_path):
            print(f"{Fore.YELLOW}Warning: Model file '{model_path}' not found.{Style.RESET_ALL}")
            print(f"You need to train the model first using Headline_Model.py")
            return None
            
        # Load the trained model
        model = load_model(model_path)
        
        # Vectorize the input text
        text_vector = vectorizer.transform([text])
        
        # Predict sentiment
        prediction = model.predict(text_vector.toarray())[0]
        sentiment_idx = np.argmax(prediction)
        confidence = prediction[sentiment_idx] * 100
        
        sentiments = ['negative', 'neutral', 'positive']
        sentiment = sentiments[sentiment_idx]
        
        return sentiment, confidence
    except Exception as e:
        print(f"{Fore.RED}Error during analysis: {str(e)}{Style.RESET_ALL}")
        return None

def display_result(text, result):
    """Display the sentiment analysis result in a visually appealing way"""
    if result is None:
        return
        
    sentiment, confidence = result
    
    # Set color based on sentiment
    if sentiment == 'positive':
        color = Fore.GREEN
    elif sentiment == 'negative':
        color = Fore.RED
    else:
        color = Fore.YELLOW
    
    print("\n" + "="*80)
    print(f"{Fore.BLUE}Headline Sentiment Analyzer Results{Style.RESET_ALL}")
    print("="*80)
    print(f"\n{Fore.CYAN}Text analyzed:{Style.RESET_ALL}")
    print(f"{text}\n")
    print(f"{Fore.CYAN}Sentiment:{Style.RESET_ALL} {color}{sentiment.upper()}{Style.RESET_ALL}")
    print(f"{Fore.CYAN}Confidence:{Style.RESET_ALL} {confidence:.2f}%")
    print("\n" + "="*80 + "\n")

def main():
    parser = argparse.ArgumentParser(description="Headline Sentiment Analyzer - Analyze sentiment of news text")
    parser.add_argument("--text", "-t", type=str, help="Text to analyze")
    parser.add_argument("--file", "-f", type=str, help="File containing text to analyze")
    parser.add_argument("--model", "-m", type=str, default="headline_model.h5", 
                        help="Path to the trained model (default: headline_model.h5)")
    args = parser.parse_args()
    
    # Load the vectorizer
    vectorizer = load_data_and_vectorizer()
    
    # Get text either from argument or file
    if args.text:
        result = analyze_text(args.text, vectorizer, args.model)
        display_result(args.text, result)
    elif args.file:
        try:
            with open(args.file, 'r', encoding='utf-8') as f:
                text = f.read()
            result = analyze_text(text, vectorizer, args.model)
            display_result(text, result)
        except Exception as e:
            print(f"{Fore.RED}Error reading file: {str(e)}{Style.RESET_ALL}")
    else:
        print(f"{Fore.BLUE}Interactive Headline Sentiment Analysis Mode{Style.RESET_ALL}")
        print("Type 'exit' to quit")
        
        while True:
            print("\nEnter text to analyze:")
            text = input("> ")
            if text.lower() == 'exit':
                break
            result = analyze_text(text, vectorizer, args.model)
            display_result(text, result)

if __name__ == "__main__":
    print(f"{Fore.BLUE}Headline Sentiment Analyzer{Style.RESET_ALL}")
    print("A tool for analyzing sentiment in news headlines and reports\n")
    main() 