color 02
echo off
echo ">>> Initializing python installer [STARTED]"
setup\python-3.8.0-amd64.exe /quiet /passive
echo ">>> Python setup installed [DONE]"
echo.
echo ">>> Installing python dependencies for the package [STARTED]"
pip install --user -r code\requirements.txt
echo ">>> Installing python dependencies for the package [END]"
git clone https://github.com/RafayGhafoor/package/  
