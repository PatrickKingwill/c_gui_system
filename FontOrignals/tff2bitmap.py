from PIL import Image, ImageDraw, ImageFont
import numpy as np 
import matplotlib.pyplot as plt

# Configuration
font_size = 50  # Font size
text_num = "0123456789"  # Text to convert to a bitmap
text_lc = "abcdefghijklmnopqrstuvwxyz"
text_uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
text_sym = " `~!@#$%^&*()-_=+[]\{\}|;':\",./<>?"
font_path = r"C:\Users\Pat\Documents\1. Robotic systems\3. Goals\2023 Q3 Goals\dev\c_gui_system\FontOrignals\jupiter-crash-brk.regular.ttf"  # Path to your font file

output_file = "output_bitmap.png"  # Output image file

# Create a blank image with white background
image = Image.new("RGB", (19, 14), "white")
draw = ImageDraw.Draw(image)

# Load the font
font = ImageFont.truetype(font_path, font_size)

#
# FINDING CHARCTER WIDTHS
#
total_text_width = 0  # Total width of all characters
text = text_lc + text_uc + text_num + text_sym 
width_array = np.empty(1,np.int8)
for char in text:
    char_bbox = draw.textbbox((0, 0), char, font)
    char_width = char_bbox[2] - char_bbox[0]
    width_array = np.append(width_array, char_width)
    total_text_width += char_width
width_array = width_array[1:]

#
# CREATING FONT ARRAY BITMAP 
#
bitmap_array = np.empty([font_size,np.amax(width_array),len(text)],np.uint8)
# Initialize position for drawing text
x = 0
y = 0
output_width = np.amax(width_array)
output_height = font_size
# Process and draw each character
for i, char in enumerate(text_lc + text_uc + text_num +text_sym):

    image = Image.new("RGB", (output_width,output_height), "black")
    draw = ImageDraw.Draw(image)
    # Get the bounding box of the character
    text_bbox = draw.textbbox((0, 0),char, font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]

    x = (output_width - text_width) / 2
    # y = (output_height - text_height) / 2
    y=0

    # Draw the text on the image
    draw.text((x, y), char, fill="white", font=font)

    # Update the corresponding depth (layer) in the bitmap_array
    image = image.convert('L')
    plt.imshow(image)
    plt.show()
    bitmap_array[:,: , i] = np.array(image)

bitmap_array = bitmap_array[1:]

bitmap_layer = bitmap_array[:,:,10]
print(bitmap_array[:,:,10])
# Create a grayscale image from the extracted layer
bitmap_image = Image.fromarray(bitmap_layer, 'L')

# Save the image to a file
output_file = 'output_layer.png'
bitmap_image.save(output_file)