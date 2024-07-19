# AuraSR
![aurasr example](https://storage.googleapis.com/falserverless/gallery/aurasr-animated.webp)

GAN-based Super-Resolution for real-world images, a variation of the [GigaGAN](https://mingukkang.github.io/GigaGAN/) paper for image-conditioned upscaling. Torch implementation is based on the unofficial [lucidrains/gigagan-pytorch](https://github.com/lucidrains/gigagan-pytorch) repository.

## Usage

```bash
$ pip install aura-sr
```

```python
from aura_sr import AuraSR

aura_sr = AuraSR.from_pretrained()
```

```python
import requests
from io import BytesIO
from PIL import Image

def load_image_from_url(url):
    response = requests.get(url)
    image_data = BytesIO(response.content)
    return Image.open(image_data)

image = load_image_from_url("https://mingukkang.github.io/GigaGAN/static/images/iguana_output.jpg").resize((256, 256))
upscaled_image = aura_sr.upscale_4x(image)
```

### Reduce Seam Artifacts 

`upscale_4x` upscales the image in tiles that do not overlap. This can result in seams. Use `upscale_4x_overlapped` to reduce seams. This will double the time upscaling by taking an additional pass and averaging the results. 
