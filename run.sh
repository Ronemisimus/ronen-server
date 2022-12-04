TEMPPATH=$PATH
PATH="$(pwd)/package-chace;$PATH"
pip install --target=package-chace .
python -m ronen-server
PATH=$TEMPPATH