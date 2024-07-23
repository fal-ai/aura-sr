from setuptools import setup


setup(
    name="aura-sr",
    version="0.0.4",
    description="GAN-based Super-Resolution for AI generated images, based on the GigaGAN architecture.",
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
