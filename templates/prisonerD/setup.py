import PyInstaller.__main__

# This script can be used as build script which will pack your code
# This use pyinstaller to create the executable file
# you need to install following pip pakage for this and then
# add your python file name
# 'pip install pyinstaller'
PyInstaller.__main__.run([
    'src/clientApp.py',
    '--onefile',
    '--windowed'
])

# This is example to pack multiple files project into one executable.
# pyinstaller C:/version_0_1_client_server/scripts/filename.py --paths C:/version_0_1_client_server/  --add-data 'data/config.yaml;data' --add-data 'data/image.png;data'
