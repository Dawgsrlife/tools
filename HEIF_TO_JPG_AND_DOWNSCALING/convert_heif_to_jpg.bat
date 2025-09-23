@echo off

set "IV=C:\Program Files\IrfanView\i_view64.exe"

cd /d "%~dp0convert"

echo Converting images in: %cd%
echo Using IrfanView at: %IV%
echo.

for %%F in (*.heic *.HEIC *.png *.PNG *.bmp *.BMP *.tif *.tiff *.gif *.webp *.jpeg *.JPEG) do (
  if /I not "%%~xF"==".jpg" (
    echo Converting: %%~nxF
    "%IV%" "%%~fF" /jpgq=92 /convert="%%~dpnF.jpg"
  )
)

echo.
echo Finished. Check this folder for JPGs.
pause
