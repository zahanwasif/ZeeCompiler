@ECHO off
SETLOCAL ENABLEDELAYEDEXPANSION
FOR %%i IN ("%~dp0..") DO SET ZEE_ROOT=%%~fi
REM echo %ZEE_ROOT%
echo "Zee language Compiler made by Zahan Wasif"
REM more %ZEE_ROOT%\LICENSE
python3 %ZEE_ROOT%\util\parser.py %1 %2 %3 %4 %5 %6 %7 %8 %9