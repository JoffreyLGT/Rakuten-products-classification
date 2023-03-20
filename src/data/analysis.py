from matplotlib.gridspec import GridSpec, GridSpecFromSubplotSpec
import pandas as pd
import numpy as np
from pathlib import Path
import imagesize
import matplotlib.pyplot as plt
from PIL import Image

import data


IMG_SUB_DIR = "/images/image_train/"


def get_img_dir(datadir: str):
    return f"{datadir}{IMG_SUB_DIR}"


def get_img_name(productid: int, imageid: int) -> str:
    """
    Return the filename of the image.

    Arguments:
    - productid: int - "productid" field from the original DataFrame.
    - imageid: int - "imageid" field from the original DataFrame.

    Return:
    A string containing the filename of the image. Example: image_1000076039_product_580161.jpg
    """
    return f"image_{imageid}_product_{productid}.jpg"


def get_img_information(datadir: str) -> pd.DataFrame:
    """
    Return the list of images with their FileName, Width, Height and Aspect Ratio.

    Return:
    A DataFrame with 4 columns: FileName, Width, Height and Aspect Ratio.
    """
    img_dir = get_img_dir(datadir)
    # Get the name of all the images
    images_name = [img.name for img in Path(
        img_dir).iterdir() if img.suffix == ".jpg"]
    # Get the size of each image
    images_size = {}
    for name in images_name:
        images_size[str(name)] = imagesize.get(img_dir + name)
    # Convert the dictionnary into a DataFrame
    df_images = pd.DataFrame.from_dict([images_size]).T.reset_index().set_axis([
        'FileName', 'Size'], axis='columns')
    # Separate the width and the height into different columns
    df_images[["Width", "Height"]] = pd.DataFrame(
        df_images["Size"].tolist(), index=df_images.index)
    df_images = df_images.drop("Size", axis=1)
    # Calculate the aspect ratio
    df_images["Aspect Ratio"] = round(
        df_images["Width"] / df_images["Height"], 2)
    return df_images


def display_random_img(datadir: str, nb_img: int, df: pd.DataFrame = None):
    # Ensure we have the DataFrame
    if df is None:
        df = data.load_data(datadir)

    img_dir = get_img_dir(datadir)

    # Get random lines from DataFrame
    df_random = df.sample(nb_img)
    # Store the name of each file in a list
    random_images = [get_img_name(productid, imageid) for productid, imageid in zip(
        df_random["productid"], df_random["imageid"])]

    rows, cols = get_rows_cols(nb_img)
    print(rows, cols)
    # Create a figure and set the background to be transparent so we can see the white borders
    fig = plt.figure(figsize=(4*cols, 4*rows), layout="constrained")
    fig.patch.set_alpha(0.0)
    for i, filename in enumerate(random_images):
        img = np.asarray(Image.open(img_dir + filename))
        ax = fig.add_subplot(rows, cols, i + 1)
        ax.imshow(img)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.grid(False)

    fig.suptitle(f"{nb_img} images aléatoires")


def get_img_per_category(nb_img: int, df: pd.DataFrame) -> pd.DataFrame:
    """
    Return n images per category.

    Arguments:
    n: int - Number of images per category.

    Returns:
    A DataFrame containing 2 columns: prdtypecode, imagename.
    """
    # df_words.groupby("prdtypecode").value_counts().groupby(level=0).head(n).to_frame()
    images_per_category = df.groupby(
        "prdtypecode").value_counts().groupby(level=0).sample(nb_img).to_frame()
    images_per_category = images_per_category.reset_index()
    images_per_category = images_per_category.drop(0, axis=1)
    images_per_category["imagename"] = [get_img_name(productid, imageid) for productid, imageid in zip(
        images_per_category["productid"], images_per_category["imageid"])]
    return images_per_category.drop(["designation", "description", "productid", "imageid"], axis=1)


def get_rows_cols(nb_items: int, max_col: int = 3) -> tuple:
    if (nb_items <= max_col):
        return (1, nb_items)
    cols = max_col
    if (nb_items % max_col == 0):
        rows = nb_items//max_col
    else:
        rows = nb_items//max_col + 1
    return (rows, cols)


def format_axes(fig: plt.Figure):
    for ax in fig.axes:
        ax.set_xticks([])
        ax.set_yticks([])
        # ax.grid(False)
        ax.set_aspect(1)


def display_img_per_category(nb_img: int, datadir: str, df: pd.DataFrame, nb_limit_categories: int = 27):
    df_img_per_category = get_img_per_category(nb_img, df)

    img_dir = get_img_dir(datadir)

    fig = plt.figure(figsize=(20, 24), layout="constrained")
    rows, cols = get_rows_cols(nb_limit_categories)
    gs_cat = GridSpec(rows, cols, figure=fig)
    # gs_cat.tight_layout(fig)
    i = 0
    for i, prdtypecode in enumerate(df_img_per_category["prdtypecode"].unique()):
        type_images = df_img_per_category[df_img_per_category["prdtypecode"]
                                          == prdtypecode]["imagename"]

        gs_img = GridSpecFromSubplotSpec(1, nb_img, subplot_spec=gs_cat[i])
        j = 0
        as_title = False
        for j, imagename in enumerate(type_images):
            ax = fig.add_subplot(gs_img[j])
            if (as_title == False and (nb_img // (j+1) == nb_img // 2)):
                ax.set_title("Catégorie " + str(prdtypecode))
                as_title = True
            img = np.asarray(Image.open(img_dir + imagename))
            ax.imshow(img)
            j += 1
        i += 1

    format_axes(fig)
    fig.suptitle(f"{nb_img} images aléatoires de chaque catégorie")
    plt.show()
