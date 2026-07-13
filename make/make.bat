@echo off

where python >nul 2>&1
if errorlevel 1 (
    echo Installing Python...
    winget install --id Python.Python.3.12 -e
)

if not exist venv (
    python -m venv venv
)

call venv\Scripts\activate.bat

python -m pip install --upgrade pip
python -m pip install -e .

echo.
echo Journal is ready!
pause