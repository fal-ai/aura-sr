# AuraSR
GAN-based Super-Resolution for real-world images, a variation of the [GigaGAN](https://mingukkang.github.io/GigaGAN/) paper for image-conditioned upscaling. Torch implementation is based on the unofficial [lucidrains/gigagan-pytorch](https://github.com/lucidrains/gigagan-pytorch) repository.

## Usage

```bash
$ pip install aura-sr
```

```python
from aura_sr import AuraSR

config = {
    "style_network": {
        "dim_in": 128,
        "dim_out": 512,
        "depth": 4
    },
    "dim": 64,
    "image_size": 256,
    "input_image_size": 64,
    "unconditional": True,
    "skip_connect_scale": 0.4
}

model = torch.load("/home/user/AuraSR/model.ckpt")

aura_sr = AuraSR(config)
aura_sr.upsampler.load_state_dict(model["G"], strict=True)
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
