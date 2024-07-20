from setuptools import setup


setup(
    name="aura-sr",
    version="0.0.3",
    description="GAN-based Super-Resolution for AI generated images, a variation of the GigaGAN paper.",
    py_modules=["aura_sr"],
    install_requires=[
        "torch>=2.0",
        "torchvision",
        "numpy",
        "einops",
        "huggingface_hub",
        "safetensors",
    ],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
)
