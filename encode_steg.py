from PIL import Image

def encode_lsb(image_path, message, output_path):
    img = Image.open(image_path).convert('RGB')
    pixels = list(img.getdata())

    message += '\x00'  # marcador de fim
    bits = ''.join(format(ord(c), '08b') for c in message)

    if len(bits) > len(pixels) * 3:
        raise ValueError("Mensagem grande demais para essa imagem.")

    new_pixels = []
    bit_index = 0

    for pixel in pixels:
        r, g, b = pixel
        if bit_index < len(bits):
            r = (r & 0xFE) | int(bits[bit_index]); bit_index += 1
        if bit_index < len(bits):
            g = (g & 0xFE) | int(bits[bit_index]); bit_index += 1
        if bit_index < len(bits):
            b = (b & 0xFE) | int(bits[bit_index]); bit_index += 1
        new_pixels.append((r, g, b))

    img.putdata(new_pixels)
    img.save(output_path, 'PNG')
    print(f"Mensagem escondida com sucesso em: {output_path}")

encode_lsb(
    'static/img/liberdade.jpg',
    '/fase/p3n8w',
    'static/img/liberdade.png'
)
