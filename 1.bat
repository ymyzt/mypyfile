CocosCreator.exe --path ./ --build "platform=win32;debug=true;template=default"
python  clvs.py
CocosCreator.exe --path ./ --compile "platform=win32;debug=true;template=default"
pause