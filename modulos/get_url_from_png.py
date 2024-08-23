import base64

def get_base64_of_png_file(png_file):
    with open(png_file, 'rb') as f:
        data = f.read()

    return base64.b64encode(data).decode()