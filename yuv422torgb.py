from PIL import Image
import matplotlib.pyplot as plt
import IPython

def gen_img565(bar):
    # Create a new image with a size of 100x100 pixels
    img = Image.new('RGB', (100, 100), (255, 0, 0))
    data = img.load()
    # Generate the 1st line of the bar
    my_list = [0] *100
    for x in range(100): 
        idx = int(x/len(bar))
        idx = idx % len(bar)
        # print(idx)
        my_list[x] = bar[idx]
    # Copy the 1st line to the other lines
    for y in range(100):
        for x in range(100):
            data[x, y] = my_list[x]
    return img

#   /* EBU color bars
#    * See also https://stackoverflow.com/questions/6939422 */
# the yuv color bars and rgb color bars are referred to the same color
bar_color_yuv = [
    # /*  Y,   U,   Y,   V */
    ( 235, 128, 235, 128), # /* 100% White */
    ( 219,  16, 219, 138), # /* Yellow */
    ( 188, 154, 188,  16), # /* Cyan */
    ( 173,  42, 173,  26), # /* Green */
    (  78, 214,  78, 230), # /* Magenta */
    (  63, 102,  63, 240), # /* Red */
    (  32, 240,  32, 118), # /* Blue */
    (  16, 128,  16, 128), # /* Black */
  ]
bar_color_rgb =[
        ( 255, 255, 255 ),  # // 100% White
        ( 255, 255,   0 ),  # // Yellow
        (   0, 255, 255 ),  # // Cyan
        (   0, 255,   0 ),  # // Green
        ( 255,   0, 255 ),  # // Magenta
        ( 255,   0,   0 ),  # // Red
        (   0,   0, 255 ),  # // Blue
        (   0,   0,   0 ),  # // Black
]


# Claim a 8 line list for data conversion
bar_color_rgb_from_yuv = [0]*8
# convert yuv422 to rgb888
# refer to https://blog.csdn.net/mianhuantang848989/article/details/27308437
for i in range(8):
    y1,u,y2,v = bar_color_yuv[i]
    r = max(0,min(255,   1.164*y1 + 1.596 * (v - 128)                       ))
    g = max(0,min(255,   1.164*y1 - 0.392 * (u - 128) - 0.813 * (v - 128)   ))
    b = max(0,min(255,   1.164*y1 + 2.017 * (u - 128)                       ))
    bar_color_rgb_from_yuv[i] = (int(r),int(g),int(b))

# We show two images, one is the right rgb answer and the other is our solution
fig, axs = plt.subplots(1, 2, figsize=(10, 5))
axs[0].imshow(gen_img565(bar_color_rgb))
axs[0].set_title('Image 1. Right RGB')
axs[1].imshow(gen_img565(bar_color_rgb_from_yuv))
axs[1].set_title('Image 2. RGB converted from YUV422')
plt.show()

# IPython.embed()