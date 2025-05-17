@echo off
REM Headline Sentiment Analyzer - Startup Script

echo ===================================================================
echo         Headline Sentiment Analyzer - Setup ^& Launch Script        
echo ===================================================================
echo.

REM Check Python version
echo Checking Python installation...
where python >nul 2>nul
if %ERRORLEVEL% NEQ 0 (
    echo Error: Python not found. Please install Python 3.7 or higher
    exit /b 1
)

python --version
set PYTHON_CMD=python

REM Create virtual environment
echo.
echo Setting up virtual environment...
if not exist venv (
    %PYTHON_CMD% -m venv venv
    echo Virtual environment created.
) else (
    echo Virtual environment already exists.
)

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo.
echo Installing dependencies...
pip install -r requirements.txt

echo.
echo ===================================================================
echo                          Setup Complete                           
echo ===================================================================
echo.

REM Provide options to run
echo What would you like to do?
echo 1^) Run the web application
echo 2^) Analyze a headline
echo 3^) Exit

set /p choice="Enter your choice (1-3): "

if "%choice%"=="1" (
    echo.
    echo Starting web application...
    python main.py --webapp
) else if "%choice%"=="2" (
    echo.
    set /p headline="Enter a headline to analyze: "
    python analyze_headline.py --headline "%headline%"
) else if "%choice%"=="3" (
    echo Exiting...
) else (
    echo Invalid choice. Exiting...
)

REM Deactivate virtual environment
call venv\Scripts\deactivate.bat 