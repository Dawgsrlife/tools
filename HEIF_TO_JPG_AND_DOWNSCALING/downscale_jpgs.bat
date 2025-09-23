@echo off
setlocal

set "IV=C:\Program Files\IrfanView\i_view64.exe"
set "INDIR=%~dp0downscale"
set "OUTDIR=%INDIR%\out"

if not exist "%OUTDIR%" mkdir "%OUTDIR%"

echo Input folder: %INDIR%
echo Output folder: %OUTDIR%
echo.

for %%F in (%INDIR%\*.jpg) do (
  echo Processing: %%F
  "%IV%" "%%~fF" /resize=^(50p,50p^) /resample /jpgq=85 /convert="%OUTDIR%\%%~nxF"
)

echo.
echo Done. Check the "out" folder inside downscale.
pause
