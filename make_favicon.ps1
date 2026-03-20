Add-Type -AssemblyName System.Drawing
$imgPath = Join-Path $PWD "images\icon.png"
$outPath = Join-Path $PWD "images\favicon.png"

$img = [System.Drawing.Image]::FromFile($imgPath)
$bmp = New-Object System.Drawing.Bitmap 64, 64
$graph = [System.Drawing.Graphics]::FromImage($bmp)

# Set high-quality interpolation
$graph.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic

$graph.DrawImage($img, 0, 0, 64, 64)
$bmp.Save($outPath, [System.Drawing.Imaging.ImageFormat]::Png)

$graph.Dispose()
$bmp.Dispose()
$img.Dispose()

Write-Host "Favicon created successfully"
