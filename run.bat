setlocal
SET PATH=%~dp0package-chace;%PATH%
echo %PATH%
pip install --target=package-chace .
python -m ronen-server