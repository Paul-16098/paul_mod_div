chcp 65001
cd "%~p0"
echo off
cls
@REM python -m ensurepip --upgrade
@REM python -m pip install --upgrade pip
@REM pip install -r requirements.txt
python -m updata
@REM cd "%~p0\mods\BESC"
@REM git pull -v
cd "%~p0"
@REM pause
