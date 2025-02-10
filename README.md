# Image to ASCII Art Converter

A simple Python script that converts images into ASCII art. This tool takes any image file as input and creates an artistic representation using ASCII characters, maintaining the visual essence of the original image through different character densities.

## Features

- Converts any image format supported by PIL (PNG, JPG, etc.)
- Maintains aspect ratio of original image
- Customizable output width
- Outputs both to console and text file
- Uses a rich set of ASCII characters for detailed gradients
- Preserves image contrast and details
- Available in both CLI and GUI versions

## Requirements

- Python 3.x
- Pillow (PIL)
- NumPy
- Tkinter (included with Python)

Install the required packages using:

```bash
pip install Pillow numpy
```

## Usage

### Command Line Interface
1. Run the script:
```bash
python image_to_ascii.py
```
2. When prompted:
   - Enter the path to your image file
   - Enter desired width (default is 100 characters)

### Graphical User Interface
1. Run the UI version:
```bash
python image_to_ascii_ui.py
```
2. Use the interface to:
   - Select an image using the "Select Image" button
   - Set the desired width
   - Click "Convert" to generate ASCII art
   - Save the result using the "Save ASCII" button

The ASCII art will be:
- Displayed in the application window
- Can be saved to a text file of your choice

## Example

Command Line Input:
```
Enter the path to your image: cat.jpg
Enter desired width (default 100): 100
```

The script will generate ASCII art and save it to `ascii_output.txt`.

## Tips for Best Results

- Use high-contrast images
- Ensure your terminal uses a monospace font
- Larger widths provide more detail but may not display properly in all terminals
- Dark backgrounds work better for viewing the output
- Simple images with clear subjects work best

## Character Set

The converter uses a range of ASCII characters to represent different levels of brightness:

```
$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. 
```

- Denser characters (like '@', '#', '&') represent darker areas
- Lighter characters (like '.', '`', ' ') represent brighter areas

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to fork this repository and submit pull requests for any improvements.