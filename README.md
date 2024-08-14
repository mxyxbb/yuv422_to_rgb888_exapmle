# YUV422 to RGB888 Example

A simple example showing how to convert YUV422 to RGB888 format.

一个简单的例子，展示了YUV422转换到RGB888格式的方式。
```
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
```

There are two arrays in the program, which correspond to each other and store 8 colors each.

We convert `bar_color_yuv` to RGB format in a certain way and store it in `bar_color_rgb_from_yuv`.

Then we draw the obtained 8 colors and the 8 colors specified by "answer" in the form of color bars to check the correctness of our conversion.

Obviously, we get the correct result.
![Figure_1](https://github.com/user-attachments/assets/7eb80eaf-59b6-44ca-9538-c914847645c1)

Conversion method

```
r = 1.164*y + 1.596 * (v - 128)                    
g = 1.164*y - 0.392 * (u - 128) - 0.813 * (v - 128)
b = 1.164*y + 2.017 * (u - 128)                    
```

## Chinese

程序中有两个数组，它们是相互对应的，各自均存储了8种颜色。

我们把`bar_color_yuv`通过一种方式转换到rgb格式，存储到`bar_color_rgb_from_yuv`当中。

然后把得到的这8种颜色，和"答案"指定的8种颜色，分别用彩条的方式绘制出来，查看我们转换的正确性。

显然，我们得到了正确的结果。
![Figure_1](https://github.com/user-attachments/assets/7eb80eaf-59b6-44ca-9538-c914847645c1)

转换方式

```
r = 1.164*y + 1.596 * (v - 128)                    
g = 1.164*y - 0.392 * (u - 128) - 0.813 * (v - 128)
b = 1.164*y + 2.017 * (u - 128)                    
```
