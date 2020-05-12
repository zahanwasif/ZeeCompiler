@ECHO off
SETLOCAL ENABLEDELAYEDEXPANSION
set myvar=PATH
FOR %%i IN ("%~dp0..") DO SET ZEE_ROOT=%%~fi
SET "FILE_PATH = "%ZEE_ROOT%\util""
"C:\Users\zahan\AppData\Local\Microsoft\WindowsApps\python3.exe" ""%CD%"\parser.py"
