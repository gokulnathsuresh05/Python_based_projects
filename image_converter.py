from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image
import os


class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter")
        self.root.geometry("400x300")

        Label(root, text="Select Image(s) to Convert", font=("Arial", 14)).pack(pady=10)

        Button(root, text="Choose Images", command=self.load_images).pack(pady=5)

        Label(root, text="Select Output Format:").pack(pady=5)
        self.format_var = StringVar(value="PNG")
        OptionMenu(root, self.format_var, "PNG", "JPG", "BMP", "GIF").pack(pady=5)

        Label(root, text="Resize (Optional): Width x Height").pack()
        self.width_entry = Entry(root)
        self.width_entry.pack()
        self.height_entry = Entry(root)
        self.height_entry.pack()

        Button(root, text="Convert and Save", command=self.convert_images).pack(pady=20)
        self.images = []

    def load_images(self):
        self.images = filedialog.askopenfilenames(filetypes=[("Image files", "*.jpg *.png *.bmp *.gif")])
        if self.images:
            messagebox.showinfo("Selected", f"{len(self.images)} image(s) loaded.")

    def convert_images(self):
        output_format = self.format_var.get().lower()
        output_dir = filedialog.askdirectory(title="Select Output Directory")

        if not self.images or not output_dir:
            messagebox.showerror("Error", "No images selected or output folder missing.")
            return

        for img_path in self.images:
            try:
                img = Image.open(img_path)
                base = os.path.basename(img_path)
                filename = os.path.splitext(base)[0]

                # Resize if given
                width = self.width_entry.get()
                height = self.height_entry.get()
                if width and height:
                    img = img.resize((int(width), int(height)))

                # Save image
                output_path = os.path.join(output_dir, f"{filename}.{output_format}")
                if output_format == "jpg":
                    img = img.convert("RGB")
                img.save(output_path)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to convert {img_path}:\n{e}")
                return
        messagebox.showinfo("Success", f"{len(self.images)} image(s) converted!")


if __name__ == "__main__":
    root = Tk()
    app = ImageConverterApp(root)
    root.mainloop()
