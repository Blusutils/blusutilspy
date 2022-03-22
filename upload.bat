@REM i am so lazy
del /f .\dist\*.tar.gz
python setup.py sdist
twine upload dist/*
pause