from PIL import Image
from ..helpers import divergence_index
from mandelbrot.viewer import rasterize
from config import DEFAULT_IMAGE_DIRECTORY
from config import DEFAULT_FILE_NAME
from config import DEFAULT_FILE_TYPE
from config import IMG_WIDTH
from config import IMG_HEIGHT
from config import ITERATIONS


def create_image(width: IMG_WIDTH, height: IMG_HEIGHT, iterations: ITERATIONS, color) -> Image:
    """
    :param width: The output image width
    :param height: The output image height
    :param iterations: The number of iterations per pixel
    :param color: A color function that returns a tuple with a max value of (255, 255, 255)
    :return: A PIL image file
    """
    image = Image.new("RGB", (width, height))
    for x in range(0, width):
        for y in range(0, height):
            coordinates = rasterize(x, y, height)
            divergence = divergence_index(constant=coordinates, iterations=iterations)
            image.putpixel((x, y), color(divergence))
    return image


def save_image(image: Image, directory=DEFAULT_IMAGE_DIRECTORY, file_name=DEFAULT_FILE_NAME, file_type=DEFAULT_FILE_TYPE):
    """
    :param image: a PIL image file
    :param directory: The location where you want to save the image
    :param file_name: The name of the image
    :param file_type: The type of file you want to save
    :return: None
    """
    image.save(directory + '/' + file_name + file_type)
