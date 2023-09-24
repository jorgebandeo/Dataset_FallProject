import os
import tkinter as tk
from PIL import Image, ImageTk

class ImageCropper:
    def __init__(self, root, image_path, save_path):
        self.root = root
        self.image_path = image_path
        self.save_path = save_path
        self.image_files = self.get_image_files()
        self.current_index = 0

        self.canvas = tk.Canvas(root, cursor="cross")
        self.canvas.pack(fill="both", expand=True)
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        self.rect = None
        self.image = self.load_next_image()
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
        self.canvas.bind("<ButtonPress-1>", self.on_press)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)

    def get_image_files(self):
        image_files = []
        for foldername, _, filenames in os.walk(self.image_path):
            for filename in filenames:
                if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                    image_files.append(os.path.join(foldername, filename))
        return image_files

    def load_next_image(self):
        if self.current_index < len(self.image_files):
            image_file = self.image_files[self.current_index]
            return Image.open(image_file)
        else:
            self.root.quit()

    def on_press(self, event):
        self.start_x = self.canvas.canvasx(event.x)
        self.start_y = self.canvas.canvasy(event.y)
        if self.rect:
            self.canvas.delete(self.rect)
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="red")

    def on_drag(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, self.end_x, self.end_y)

    def on_release(self, event):
        self.end_x = self.canvas.canvasx(event.x)
        self.end_y = self.canvas.canvasy(event.y)
        self.canvas.coords(self.rect, self.start_x, self.start_y, self.end_x, self.end_y)
        self.crop_and_save_image()
        self.current_index += 1
        self.image = self.load_next_image()
        if self.image:
            self.photo = ImageTk.PhotoImage(self.image)
            self.canvas.create_image(0, 0, anchor="nw", image=self.photo)
        else:
            self.root.quit()

    def crop_and_save_image(self):
        if self.start_x is not None and self.start_y is not None and self.end_x is not None and self.end_y is not None:
            left = min(self.start_x, self.end_x)
            top = min(self.start_y, self.end_y)
            right = max(self.start_x, self.end_x)
            bottom = max(self.start_y, self.end_y)
            cropped_image = self.image.crop((left, top, right, bottom))
            save_filename = os.path.basename(self.image_files[self.current_index])
            save_path = os.path.join(self.save_path, save_filename)
            cropped_image.save(save_path)

if __name__ == "__main__":
    root = tk.Tk()
    image_path = "C:/Users/jorge/Desktop/dataset/original/quedas/Fall Detection Dataset UTTEJ/images"  # Substitua pelo caminho da sua pasta de imagens
    save_path = "C:/Users/jorge/Desktop/dataset/original/quedas/Fall Detection Dataset UTTEJ/cropped_images"  # Substitua pelo caminho da pasta onde deseja salvar as imagens recortadas
    if not os.path.exists(save_path):
        os.makedirs(save_path)
    
    cropper = ImageCropper(root, image_path, save_path)
    root.mainloop()
