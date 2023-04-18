import os
import numpy as np
import pandas as pd
from src.data.analysis import get_img_name
from PIL import Image, ImageOps


def load_data(datadir: str = "data") -> pd.DataFrame:

    return pd.concat(
        [
            pd.read_csv(f"{datadir}/X.csv", index_col=0),
            pd.read_csv(f"{datadir}/y.csv", index_col=0)
        ],
        axis=1)


def get_imgs_filenames(productids: list[int], imageids: list[int]) -> list[str]:
    """
    Return a list of filenames from productids and imagesids.

    Arguments:
    - productids: list of product ids
    - imageids: list of image ids

    Return:
    A list of the same size as productids and imageids containing the filenames.
    """
    if (len(productids) != len(imageids)):
        raise ValueError("productids and imageids should be the same size")

    return [get_img_name(productid, imageid) for productid, imageid in zip(productids, imageids)]


def remove_white_stripes(img_array: np.ndarray) -> np.ndarray:
    """
    Analyse each lines and column of the array to remove the outer white stripes they might contain.

    Arguments:
    - img_array: imaged loaded into a np.ndarray.
    Returns:
    - The same array without the outer white stripes.
    Example:
    - remove_white_stripes(np.asarray(Image.open("my_image.png")))
    """
    top_line = -1
    right_line = -1
    bottom_line = -1
    left_line = -1

    i = 1
    while (top_line == -1 or bottom_line == -1
            or left_line == -1 or right_line == -1):
        if top_line == -1 and img_array[:i].mean() != 255:
            top_line = i
        if bottom_line == -1 and img_array[-i:].mean() != 255:
            bottom_line = i
        if left_line == -1 and img_array[:, :i].mean() != 255:
            left_line = i
        if right_line == -1 and img_array[:, -i:].mean() != 255:
            right_line = i

        i += 1
        if i >= img_array.shape[0]:
            break

    if (top_line == -1 or bottom_line == -1
       or left_line == -1 or right_line == -1):
        return img_array
    else:
        return img_array[top_line:-bottom_line,
                         left_line:-right_line,
                         :]


def crop_resize_img(filename: str, imput_img_dir: str, output_img_dir: str, width: int, height: int, keep_ratio: bool, grayscale: bool = False) -> None:
    """
    Crop, resize and apply a grayscale filter to the image.

    Arguments:
    - filename - str: name of the image to process. Must contain the extension.
    - input_img_dir - str: directory containing the image.
    - output_img_dir - str: directory to save the processed image in.
    - width, height - int: width and height of the processed image.
    - keep_ratio - bool: True to keep the image ratio and eventualy add some white stripes around to fill empty space. False to stretch the image.
    - grayscale - bool: True to remove the colors and set them as grayscale.
    """

    # Remove the outer white stripes from the image
    img_array = np.asarray(Image.open(imput_img_dir + filename))
    new_img_array = remove_white_stripes(img_array)
    new_img = Image.fromarray(new_img_array)

    if keep_ratio:
        new_width = new_img.width
        new_height = new_img.height

        ratio = new_width - new_height
        padding_value = np.abs(ratio) // 2
        padding = ()
        if ratio > 0:
            padding = (0, padding_value, 0, padding_value)
        else:
            padding = (padding_value, 0, padding_value, 0)

        new_img = ImageOps.expand(new_img, padding, (255, 255, 255))

    new_img = new_img.resize((width, height))

    if grayscale:
        new_img = ImageOps.grayscale(new_img)

    new_img.save(f"{output_img_dir}/{filename}")


def get_output_dir(width: int, height: int, keep_ratio: bool, grayscale: bool, type: str):
    result = f"cropped_w{width}_h{height}"
    if keep_ratio:
        result += "_ratio"
    else:
        result += "_stretched"
    if grayscale:
        result += "_graycaled"
    else:
        result += "_colors"

    return os.path.join("data", "images", result, type)


def get_img_full_path(width: int, height: int, keep_ratio: bool, grayscale: bool, type: str, prdtypecode: int, filename: str):
    output_dir = get_output_dir(width, height, keep_ratio, grayscale, type)
    return os.path.join("data", "images", type, output_dir, prdtypecode, filename)
