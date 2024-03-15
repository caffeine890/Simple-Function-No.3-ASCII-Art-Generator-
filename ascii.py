from PIL import Image

def generate_ascii_art(image_path, output_width=100):
    """
    Converts the specified image file to ASCII art.
    
    Args:
        image_path (str): Path to the image to convert.
        output_width (int): The width of the ASCII art (default is 100).
    
    Returns:
        str: The generated ASCII art.
    """
    # Open the image and convert to grayscale
    img = Image.open(image_path).convert('L')
    # Adjust the size of the image based on the output width
    width, height = img.size
    aspect_ratio = (height / width) * 0.5
    new_height = int(output_width * aspect_ratio)
    img = img.resize((output_width, new_height))
    
    # Set of ASCII characters
    ascii_chars = '@%#*+=-:. '
    # Convert the image to ASCII characters
    pixels = img.getdata()
    ascii_str = ''.join([ascii_chars[int(pixel/255.0*(len(ascii_chars)-1))] for pixel in pixels])
    # Insert line breaks at the specified width to construct the final ASCII image
    ascii_str_len = len(ascii_str)
    ascii_img=""
    for i in range(0, ascii_str_len, output_width):
        ascii_img += ascii_str[i:i+output_width] + '\n'
    
    return ascii_img

# Example usage
image_path = 'path/to/your/image.jpg'
ascii_art = generate_ascii_art(image_path)
print(ascii_art)