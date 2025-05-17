#!/usr/bin/env python3
"""
Headline Sentiment Analyzer - Web Application
This module provides a simple web interface for the sentiment analyzer.
"""

from flask import Flask, render_template, request, jsonify
import os
import sys
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Add parent directory to path to import from src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.analyze_sentiment import analyze_text

app = Flask(__name__)

# Load the vectorizer on startup
try:
    doc = pd.read_csv("data/raw/all-data.csv", header=None)
    vectorizer = TfidfVectorizer()
    vectorizer.fit(doc[1])
except Exception as e:
    print(f"Error loading data: {str(e)}")
    vectorizer = None

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """Analyze the headline text"""
    if request.method == 'POST':
        headline = request.form.get('headline', '')
        
        if not headline:
            return jsonify({'error': 'No headline provided'})
        
        if vectorizer is None:
            return jsonify({'error': 'Vectorizer not loaded'})
        
        try:
            result = analyze_text(headline, vectorizer, "models/headline_model.h5")
            if result:
                sentiment, confidence = result
                return jsonify({
                    'headline': headline,
                    'sentiment': sentiment,
                    'confidence': f"{confidence:.2f}%"
                })
            else:
                return jsonify({'error': 'Analysis failed'})
        except Exception as e:
            return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True) 