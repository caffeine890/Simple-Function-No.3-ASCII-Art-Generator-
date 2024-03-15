# ASCII Art Generator

This repository contains a Python script, `ascii.py`, designed to convert image files into ASCII art. Utilizing the Pillow library for image processing, it transforms any given image into a piece of art made entirely out of ASCII characters.

## Features

- **Grayscale Conversion**: Converts images to grayscale to enhance contrast in the ASCII representation.
- **Aspect Ratio Maintenance**: Resizes images to a specified output width while maintaining the aspect ratio.
- **Brightness Mapping**: Maps image pixels to a set of ASCII characters based on brightness levels.
- **Text Editor Compatibility**: Generates ASCII art that can be viewed in any text editor or console.


## Usage

To generate ASCII art from an image, follow these steps:

1. Ensure Python 3.x is installed on your system.
2. Install the Pillow library:

```bash
pip install Pillow
```


3. Run the `ascii.py` script with Python, specifying the path to your image:

```python
from ascii import generate_ascii_art
image_path = 'path/to/your/image.jpg'
ascii_art = generate_ascii_art(image_path, output_width=100)
print(ascii_art)
```



## Script Description

### `generate_ascii_art(image_path, output_width=100)`

This function converts the specified image file into ASCII art.

- **`image_path` (str)**: The path to the image file you want to convert.
- **`output_width` (int)**: The desired width of the ASCII art. The default value is 100 characters.

## Requirements

- **Python 3.x**: The script is written for Python 3.
- **Pillow library**: Required for image processing.

This script offers a unique way to repurpose your favorite images into ASCII art, blending creativity with technology.