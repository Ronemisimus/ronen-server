TEMPPATH=$PATH
PATH="$(pwd)/site-packages;$PATH" 
printf "%s\r\n\n" $PATH
pip install --root=site-packages .
python -m ronen-server
PATH=$TEMPPATH