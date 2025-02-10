from PIL import Image
import numpy as np

def image_to_ascii(image_path, width=100):
    # ASCII characters from darkest to lightest
    ascii_chars = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    
    # Open and resize image
    img = Image.open(image_path)
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio * 0.5)  # * 0.5 to account for terminal character spacing
    img = img.resize((width, height))
    
    # Convert to grayscale
    img = img.convert('L')
    pixels = np.array(img)
    
    # Convert pixels to ASCII
    ascii_str = ''
    for row in pixels:
        for pixel in row:
            # Map pixel value (0-255) to ASCII character
            char_index = int(pixel / 255 * (len(ascii_chars) - 1))
            ascii_str += ascii_chars[char_index]
        ascii_str += '\n'
    
    return ascii_str

def main():
    # Example usage
    try:
        image_path = input("Enter the path to your image: ")
        width = int(input("Enter desired width (default 100): ") or 100)
        
        ascii_art = image_to_ascii(image_path, width)
        
        # Print to console
        print(ascii_art)
        
        # Save to file
        output_file = "ascii_output.txt"
        with open(output_file, 'w') as f:
            f.write(ascii_art)
        print(f"\nASCII art has been saved to {output_file}")
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main() 