import os
from tqdm import tqdm
from PIL import Image


def clear_meta(image):
    data = list(image.getdata())
    image_without_exif = Image.new(image.mode, image.size)
    image_without_exif.putdata(data)
    return image_without_exif


def main():
    folder = 'pics/20221110'

    filenames = [x for x in os.listdir(folder) if x.endswith('.jpg')]

    for filename in tqdm(filenames):
        path = os.path.join(folder, filename)
        image = Image.open(path)
        image_without_exif = clear_meta(image)
        image_without_exif.save(path)


if __name__ == '__main__':
    main()
