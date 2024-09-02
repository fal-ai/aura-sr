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
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
