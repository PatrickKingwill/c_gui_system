from PIL import Image

# The Font_spray_font data
Font_spray_font_a = [
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,192,192,192,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,225,
  225,225,  0,  0,  7,  7,  7,  0,112,112,112,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,128,192,192,224,
  224,240,240,248,252,252,254,254,127,127,127,127, 63, 63, 63, 63,
   63, 63,  0,  0,  0, 96, 96,  0,  0,  0,  7,  7,  7,224,224,224,
    0,  7,  7,  7,224,224,224,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,255,255,255,255,255,255,255,255,  7,  1,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,252,252,252,252,252,
  252,252,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,252,252,252, 12,
   12, 12, 12, 12, 12, 28,252,248,224,  0,  0,192,192,224,224,224,
  224,224,224,224,192,128,  0,  0,192,192,224,224,224,224,224,224,
  224,224,192,128,  0, 64,224,238,238,238,  0,  0,128,192,224,224,
  224,224,224,224,224,255,255,255,255,255,255,255,255,255,255,255,
  250,233,228,146,201, 36,146, 73, 36,146, 73,164,146,201,228,242,
  253,255,255,255,255,255,255,255,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,255,255,255, 28, 28, 28, 28, 28,124,254,255,135,  3,  0,
  112,248,252,156,140,140,140,140,140,255,255,255,  0,  0,255,255,
  255,128,128,128,128,128,128,255,255,255,  0,  0,  0,255,255,255,
    0,  0,255,255,255,128,128,128,128,128,128,255,255,255,  3,  7,
    7, 15, 15, 31, 31, 63, 63,127,127,127,255,255,255,255,255,255,
  255,255,127,127,127, 63, 63, 31, 31, 15, 15,  7,  7,  3,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  3,  3,  3,  0,  0,  0,  0,  0,
    0,  3,  3,  3,  0,  0,  0,  1,  3,  3,  3,  3,  3,  3,  3,  3,
    3,  1,  0,  0,127,127,127,  3,  3,195, 99, 35, 99, 67,  1,128,
  128,128,128,131,  3,  3,128,128,  0,129,131,131,131,  3,  3,131,
    3,  3,  3,129,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  1,  1,  1,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  9,
   27, 19, 26, 14,  0,127, 25, 16, 24, 15,  0, 15,  1,  0,  0, 30,
   18, 18, 31,  0,  0, 15, 80, 80, 80,127,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
    0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0
]

# Define the dimensions of the image (8x8 grid)
width = 102
height = 64

# Create a new grayscale image
img = Image.new('L', (width, height))

# Set the pixel data in the image
img.putdata(Font_spray_font_a)

# Save the image as a grayscale bitmap (adjust the filename as needed)
img.save('font_spray_font.png')