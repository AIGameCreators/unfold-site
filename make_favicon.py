from PIL import Image
import os

try:
    img = Image.open('images/icon.png')
    img.resize((64, 64), Image.Resampling.LANCZOS).save('images/favicon.png')
    print('Favicon created successfully')
except Exception as e:
    print('Failed:', e)
