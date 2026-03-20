import os
import struct

def get_png_size(file_path):
    try:
        with open(file_path, 'rb') as f:
            head = f.read(24)
            if head.startswith(b'\x89PNG\r\n\x1a\n'):
                w, h = struct.unpack('>II', head[16:24])
                return w, h
    except:
        pass
    return None

for file in os.listdir('images'):
    if file.endswith('.png'):
        print(f"{file}: {get_png_size(os.path.join('images', file))}")
