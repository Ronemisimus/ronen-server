setlocal
SET PATH=%~dp0\site-packages;%PATH%
pip install --root=site-packages .
python -m ronen-server