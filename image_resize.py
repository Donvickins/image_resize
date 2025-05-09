from PIL import Image
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

root = tk.Tk()
root.title('Image Resizer')

img_vars = {"width": 740, "height": 220,"image_path":'', 'dim_width':None, 'dim_height': None, 'output_folder_path': ''}


root.geometry(f"{img_vars['width']}x{img_vars['height']}")
root.resizable(width=False, height=False)

def image_selector():
    img_vars['image_path'] = filedialog.askopenfilename(parent=root,title='Select image')
    img_path_entry.delete(0, tk.END)
    img_path_entry.insert(0, img_vars['image_path'])

def output_folder():
    img_vars['output_folder_path'] = filedialog.askdirectory()
    img_output_entry.delete(0, tk.END)
    img_output_entry.insert(0, img_vars['output_folder_path'])

def resize():
    image = Image.open(img_vars['image_path'])
    img_vars['dim_width'] = img_dim_entry_width.get()
    img_vars['dim_height'] = img_dim_entry_height.get()
    new_size = (int(img_vars['dim_width']), int(img_vars['dim_height']))
    resized_image = image.resize(new_size)
    img_vars['output_folder_path'] = img_output_entry.get()
    resized_image.save(f"{img_vars['output_folder_path']}/resized_image_{img_vars['dim_width']}x{img_vars['dim_height']}.png")
    messagebox.showinfo("Done", f"File saved in {img_vars['output_folder_path']}")

frame_img_path = tk.Frame(master=root)
frame_img_path.grid(row=0,column=0)
frame_img_path.columnconfigure(0, minsize=120)

img_path_label = tk.Label(master=frame_img_path, text='Image Path: ')
img_path_label.grid(row=0, column=0, padx=5, pady=10, sticky='e')

img_path_entry = tk.Entry(master=frame_img_path, width=50)
img_path_entry.grid(row=0, column=1, padx=5, pady=10)

img_path_selector_button = tk.Button(master=frame_img_path, text='Select image', command=image_selector)
img_path_selector_button.grid(row=0, column=2, padx=5, pady=10)

frame_img_dim = tk.Frame(master=root)
frame_img_dim.grid(row=1, column=0, sticky='w')
frame_img_dim.columnconfigure(0, minsize=120)

img_dim_label = tk.Label(master=frame_img_dim, text='Image dims: ')
img_dim_label.grid(row=0, column=0, padx=5, pady=10, sticky='e')

img_dim_entry_width = tk.Entry(master=frame_img_dim, width=10)
img_dim_entry_width.grid(row=0, column=1, padx=5, pady=10)

img_dim_label_x = tk.Label(master=frame_img_dim, text='X')
img_dim_label_x.grid(row=0, column=2, padx=5, pady=10)

img_dim_entry_height = tk.Entry(master=frame_img_dim, width=10)
img_dim_entry_height.grid(row=0, column=3, padx=5, pady=10)

frame_img_output = tk.Frame(master=root)
frame_img_output.grid(row=2, column=0, sticky='w')
frame_img_output.columnconfigure(0, minsize=120)

img_output_label = tk.Label(master=frame_img_output, text='Output folder: ')
img_output_label.grid(row=0,column=0, padx=5, pady=10, sticky='e')

img_output_entry = tk.Entry(master=frame_img_output, width=50)
img_output_entry.grid(row=0, column=1,padx=5, pady=10)

img_output_button = tk.Button(master=frame_img_output, text='Output path', command=output_folder)
img_output_button.grid(row=0, column=2, padx=10, pady=10)

frame_action_buttons = tk.Frame(master=root)
frame_action_buttons.grid(row=3, column=0)
frame_action_buttons.columnconfigure(0, minsize=120)

action_button_resize = tk.Button(master=frame_action_buttons, text='Resize', command=resize)
action_button_resize.pack()

root.mainloop()
