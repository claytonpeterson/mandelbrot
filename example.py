import mandelbrot as m

m.set_view(center_x=-1, center_y=0, zoom=2)

m.save_image(
    m.create_image(
        width=1024,
        height=1024,
        iterations=512,
        color=m.color_options.basic), file_name='test', file_type='.png')
