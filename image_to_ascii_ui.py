import tkinter as tk
from tkinter import filedialog, ttk, scrolledtext
from PIL import Image, ImageTk
import numpy as np

class ASCIIArtConverter(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("ASCII Art Converter")
        self.geometry("800x600")
        
        # Create main frame
        self.main_frame = ttk.Frame(self, padding="10")
        self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create widgets
        self.create_widgets()
        
        # Selected image path
        self.image_path = None
        self.preview_image = None

    def create_widgets(self):
        # Image selection
        self.select_btn = ttk.Button(self.main_frame, text="Select Image", command=self.select_image)
        self.select_btn.grid(row=0, column=0, pady=5, sticky=tk.W)
        
        # Width entry
        ttk.Label(self.main_frame, text="Width:").grid(row=0, column=1, padx=5)
        self.width_var = tk.StringVar(value="100")
        self.width_entry = ttk.Entry(self.main_frame, textvariable=self.width_var, width=10)
        self.width_entry.grid(row=0, column=2, pady=5)
        
        # Convert button
        self.convert_btn = ttk.Button(self.main_frame, text="Convert", command=self.convert_image)
        self.convert_btn.grid(row=0, column=3, padx=5, pady=5)
        
        # Preview frame
        self.preview_frame = ttk.LabelFrame(self.main_frame, text="Image Preview", padding="5")
        self.preview_frame.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.preview_label = ttk.Label(self.preview_frame)
        self.preview_label.grid(row=0, column=0)
        
        # ASCII output
        self.output_frame = ttk.LabelFrame(self.main_frame, text="ASCII Output", padding="5")
        self.output_frame.grid(row=1, column=2, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        self.output_text = scrolledtext.ScrolledText(self.output_frame, width=40, height=20, font=("Courier", 10))
        self.output_text.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Save button
        self.save_btn = ttk.Button(self.main_frame, text="Save ASCII", command=self.save_ascii)
        self.save_btn.grid(row=2, column=0, columnspan=4, pady=5)
        
        # Configure grid weights
        self.main_frame.columnconfigure(2, weight=1)
        self.main_frame.rowconfigure(1, weight=1)

    def select_image(self):
        self.image_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.gif *.bmp")]
        )
        if self.image_path:
            self.show_preview()

    def show_preview(self):
        # Load and resize image for preview
        image = Image.open(self.image_path)
        # Resize to fit preview area while maintaining aspect ratio
        display_size = (200, 200)
        image.thumbnail(display_size, Image.Resampling.LANCZOS)
        
        self.preview_image = ImageTk.PhotoImage(image)
        self.preview_label.configure(image=self.preview_image)

    def convert_image(self):
        if not self.image_path:
            return
        
        try:
            width = int(self.width_var.get())
            ascii_art = self.image_to_ascii(self.image_path, width)
            self.output_text.delete(1.0, tk.END)
            self.output_text.insert(tk.END, ascii_art)
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter a valid width")

    def save_ascii(self):
        if not self.output_text.get(1.0, tk.END).strip():
            return
            
        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text files", "*.txt")]
        )
        if file_path:
            with open(file_path, 'w') as f:
                f.write(self.output_text.get(1.0, tk.END))

    def image_to_ascii(self, image_path, width=100):
        # ASCII characters from darkest to lightest
        ascii_chars = r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
        
        # Open and resize image
        img = Image.open(image_path)
        aspect_ratio = img.height / img.width
        height = int(width * aspect_ratio * 0.5)
        img = img.resize((width, height))
        
        # Convert to grayscale
        img = img.convert('L')
        pixels = np.array(img)
        
        # Convert pixels to ASCII
        ascii_str = ''
        for row in pixels:
            for pixel in row:
                char_index = int(pixel / 255 * (len(ascii_chars) - 1))
                ascii_str += ascii_chars[char_index]
            ascii_str += '\n'
        
        return ascii_str

def main():
    app = ASCIIArtConverter()
    app.mainloop()

if __name__ == "__main__":
    main() 