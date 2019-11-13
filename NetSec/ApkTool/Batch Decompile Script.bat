@echo off
for %%a in (*.apk) do (
apktool d %%a 
)
echo Done
pause