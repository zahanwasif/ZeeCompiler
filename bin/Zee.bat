@ECHO off
SETLOCAL ENABLEDELAYEDEXPANSION
FOR %%i IN ("%~dp0..") DO SET ZEE_ROOT=%%~fi
echo %ZEE_ROOT%
echo "Zee language Compiler made by Zahan Wasif"
more %ZEE_ROOT%\LICENSE
python3 %ZEE_ROOT%\util\parser.py