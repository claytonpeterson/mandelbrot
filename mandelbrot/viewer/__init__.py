from config import DEFAULT_CENTER_X
from config import DEFAULT_CENTER_Y
from config import DEFAULT_ZOOM


view = {
    'center_x': DEFAULT_CENTER_X,
    'center_y': DEFAULT_CENTER_Y,
    'zoom': DEFAULT_ZOOM
}


def set_view(center_x, center_y, zoom):
    view['center_x'] = center_x
    view['center_y'] = center_y
    view['zoom'] = zoom


def rasterize(x, y, image_size):
    x = view['center_x'] - (view['zoom'] / 2) + (view['zoom'] * x / image_size)
    i = view['center_y'] - (view['zoom'] / 2) + (view['zoom'] * y / image_size)
    return complex(x, i)
