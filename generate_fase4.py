from PIL import Image
import numpy as np

img = Image.open('static/img/santossssssssssssss.webp').convert('L')
img = img.resize((900, 380))

arr = np.array(img, dtype=np.float32)
mn, mx = arr.min(), arr.max()
normalizado = (arr - mn) / (mx - mn) * 20 + 105
img_proc = Image.fromarray(normalizado.astype(np.uint8)).convert('RGB')

img_proc.save('static/img/fase4_hidden.png')
print("Imagem gerada sem texto!")
