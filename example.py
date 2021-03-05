import mandelbrot as m

m.set_view(center_x=-1.781248216, center_y=3.880767475e-19, zoom=.00000001)

m.save_image(
    m.create_image(
        width=512,
        height=512,
        iterations=1024,
        color=m.color_options.banded), file_name='test', file_type='.png')
