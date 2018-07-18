@set a=%~n0
@set b=%~p0
@echo off
cd ..
@set c=%cd%
cd %b%
python movegame.py %a% %c%
pause