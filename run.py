#!/usr/bin/env python3
"""
Headline Sentiment Analyzer - All-in-One Runner Script
This script provides various ways to run the Headline Sentiment Analyzer.
"""

import os
import sys
import argparse
import subprocess

def run_webapp():
    """Run the web application"""
    try:
        print("Starting web application...")
        from webapp import app
        app.run(debug=False, host='0.0.0.0', port=8000)
    except ImportError:
        print("Error: Flask not installed or webapp module not found")
        sys.exit(1)

def run_analysis(headline=None):
    """Run headline analysis"""
    if headline:
        try:
            print(f"Analyzing headline: {headline}")
            subprocess.run([sys.executable, "analyze_headline.py", "--headline", headline])
        except Exception as e:
            print(f"Error running analysis: {str(e)}")
            sys.exit(1)
    else:
        print("Error: No headline provided for analysis")
        sys.exit(1)

def run_docker(build=False):
    """Run using Docker"""
    try:
        if build:
            print("Building and starting Docker containers...")
            subprocess.run(["docker-compose", "-f", "docker-compose.simple.yml", "up", "--build"])
        else:
            print("Starting Docker containers...")
            subprocess.run(["docker-compose", "-f", "docker-compose.simple.yml", "up"])
    except Exception as e:
        print(f"Error running Docker: {str(e)}")
        sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="Headline Sentiment Analyzer - Runner Script")
    subparsers = parser.add_subparsers(dest="command", help="Command to run")
    
    # Web application command
    webapp_parser = subparsers.add_parser("webapp", help="Run the web application")
    
    # Analysis command
    analyze_parser = subparsers.add_parser("analyze", help="Analyze a headline")
    analyze_parser.add_argument("--headline", type=str, help="Headline to analyze")
    analyze_parser.add_argument("--query", type=str, help="Query to search for headlines")
    
    # Docker command
    docker_parser = subparsers.add_parser("docker", help="Run using Docker")
    docker_parser.add_argument("--build", action="store_true", help="Build Docker images")
    
    args = parser.parse_args()
    
    if args.command == "webapp":
        run_webapp()
    elif args.command == "analyze":
        if args.headline:
            run_analysis(args.headline)
        elif args.query:
            print(f"Searching for headlines about: {args.query}")
            print("This feature is not yet implemented")
            sys.exit(1)
        else:
            analyze_parser.print_help()
            sys.exit(1)
    elif args.command == "docker":
        run_docker(args.build)
    else:
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main() 