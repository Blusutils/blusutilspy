@REM i am so lazy
@echo off
del /f .\dist\*.tar.gz
python setup.py sdist
twine upload dist/*
pause