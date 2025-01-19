from setuptools import setup, find_packages

setup(
    name="thermal-camera-printer",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "Pillow>=9.0.0",
        "pyserial>=3.5",
    ],
    author="Your Name",
    author_email="your.email@example.com",
    description="A Raspberry Pi application that captures and prints images on a thermal printer",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/thermal-camera-printer",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
    ],
    python_requires=">=3.6",
) 