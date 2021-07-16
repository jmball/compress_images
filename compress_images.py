"""Compress image files."""

import argparse
import pathlib

import PIL.Image


def get_args():
    """Get CLI arguments."""
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", default="", help="File or folder path.")
    parser.add_argument(
        "--quality", type=int, default=30, help="Compressed image quality percentage."
    )

    return parser.parse_args()


def compress_images(path, quality):
    """Compress an image file or all image files in a folder.

    Parameters
    ----------
    path : str
        File or folder path.
    """
    path = pathlib.Path(path)

    if path.exists() is False:
        raise ValueError(f"Invalid path: {path}")

    if path.is_dir():
        folder = path
        files = [f for f in path.iterdir()]
    elif path.is_file():
        folder = path.parent()
        files = [path]

    for f in files:
        try:
            im = PIL.Image.open(f)
            new_filename = f"compressed-{f.parts[-1]}"
            im.save(folder.joinpath(new_filename), optimize=True, quality=quality)
        except PIL.Image.UnidentifiedImageError:
            print(f"Invalid image file: {f}")


if __name__ == "__main__":
    args = get_args()
    compress_images(args.path, args.quality)
