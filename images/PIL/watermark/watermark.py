# -*- coding:utf-8 -*-
"""
定位水印
"""
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageChops
import glob, os, sys, argparse
import random

def crop_image(im):
    '''裁剪图片边缘空白'''
    bg = Image.new(mode='RGBA', size=im.size)
    diff = ImageChops.difference(im, bg)
    del bg
    bbox = diff.getbbox()
    if bbox:
        return im.crop(bbox)
    return im

def add_watermark(text, fontname, fontsize, position, angle, opacity, imagefile, output_dir,fillcolor="#ff0000"):
    #img = Image.open(imagefile).convert('RGBA')
    img = Image.open(imagefile)
    # PIL.Image.new(mode, size, color=0)  color Default is black
    watermark = Image.new('RGBA', img.size)
    n_font = ImageFont.truetype(fontname, fontsize)
    n_width, n_height = n_font.getsize(text.decode(sys.getfilesystemencoding()))
    draw = ImageDraw.Draw(watermark, 'RGBA')
    x_posinon = watermark.size[0] - n_width  # (x,0)
    y_posinon = watermark.size[1] - n_height  # (0,y)
    if (position == "UL"):  # 左上 upper left (UL)
        position = (0, 0)
    if (position == "CL"):  # 左中 center left (CL)
        position = (0, y_posinon / 2)
    if (position == "LL"):  # 左下 lower left (LL)
        position = (0, y_posinon)
    if (position == "CU"):  # 中上 center upper (CU)
        position = (x_posinon / 2, 0)
    if (position == "CT"):  # 中間 center (CT)
        position = (x_posinon / 2, y_posinon / 2)
    if (position == "CL"):  # 中下 center lower (CL)
        position = (x_posinon / 2, y_posinon)
    if (position == "UR"):  # 右上 upper right (UR)
        position = (x_posinon, 0)
    if (position == "CR"):  # 右中 center right (CR)
        position = (x_posinon, y_posinon / 2)
    if (position == "LR"):  # 右下 lower right (LR)
        position = (x_posinon, y_posinon)

    draw.text(position, text.decode(sys.getfilesystemencoding()), font=n_font, fill=fillcolor)

    watermark = watermark.rotate(angle)  # 預設為 Counterclockwise Rotation 逆時針 旋轉
    alpha = watermark.split()[3]
    # enhance(factor)  Factor 1.0 always returns a copy of the original image, lower factors mean less color (brightness, contrast, etc), and higher values more
    alpha = ImageEnhance.Brightness(alpha).enhance(opacity)
    watermark.putalpha(alpha)
    target_file = "%s%s" % (output_dir, os.path.basename(imagefile))
    print "Save to " + target_file
    # PIL.Image.composite(image1, image2, mask)
    try:
        Image.composite(watermark, img, watermark).save(target_file, 'JPEG', quality=60)
    except IOError:
        Image.composite(watermark, img, watermark).save(target_file, 'PNG')
    # 可參考 https://pillow.readthedocs.org/en/3.0.0/reference/Image.html


def usage():
    print "usage:"
    print "python example.py [-t 文字:簽名] [-f 字型:超世紀粗行書.TTF] [-S 字型大小:50] [-p 位置:CT] [-a 旋轉:0] [-o 透明度:0.8] -s src-dir -d dst-dir"
    sys.exit()

def main():
    parse = argparse.ArgumentParser()
    parse.add_argument("-s", "--src-dir", default="./", type=str, help="Source Dir")
    parse.add_argument("-d", "--dst-dir", default="./watermark_images/", type=str, help="Destination Dir")
    parse.add_argument("-t", "--text", default="测试签名", type=str, help="Water maker text")#水印文字
    parse.add_argument("-f", "--font-name", default="./font/青鸟华光简琥珀.ttf", type=str, help="Font file name")#字体
    parse.add_argument("-S", "--font-size", default=50, type=int, help="Font size")#字号
    parse.add_argument("-p", "--position", default="CT", type=str, help="Position")#位置
    parse.add_argument("-a", "--angle", default=0, type=int, help="Angle")#旋转角度
    parse.add_argument("-o", "--opacity", default=0.8, type=float, help="Opacity")#透明度
    parse.add_argument("-c", "--fill-color", default="#ff0000", type=str, help="Color")

    src_dir = "./"
    dst_dir = "watermark_images/"

    text, fontname, fontsize, position, angle, opacity = "测试签名", "font-chaoshijicuxingshu.TTF", "50", "CT", "0", "0.8"
    fillcolor = "#ff0000"

    args = parse.parse_args()

    if args.text:
            text = args.text
    if args.font_name:
            fontname = args.font_name.decode('utf-8')
    if args.font_size:
            fontsize = args.font_size
    if args.position:
            position = args.position
    if args.angle:
            angle = args.angle
    if args.opacity:
            opacity = args.opacity
    if args.src_dir:
            src_dir = args.src_dir
    if args.dst_dir:
            dst_dir = args.dst_dir
    if args.fill_color:
            fillcolor = args.fill_color

    if not( src_dir.endswith("/") or src_dir.endswith("\\")):
        src_dir = src_dir + "/"

    if not( dst_dir.endswith("/") or dst_dir.endswith("\\")):
        dst_dir = dst_dir + "/"

    if not os.path.isdir(dst_dir):
        os.mkdir(dst_dir)

    all_image_files = []
    if os.path.isfile(src_dir):
        all_image_files = [src_dir]
    else:
        # 找出目录下的所有图片
        types = ('*.png', '*.jpg', '*.jpeg', '*.bmp', '*.gif')
        for files in types:
            all_image_files.extend(glob.glob("%s%s" % (src_dir, files)))

    positions = ("UL", "CL", "LL", "CU", "CT", "CL", "UR", "CR", "LR")
    random.seed()
    pos_num = len(position)
    pos = position
    for image_file in all_image_files:
        print "Processing", image_file, "..."
        if position == 'auto':
            pos = positions[random.randint(0, pos_num - 1)]
        add_watermark(args.text, fontname, int(fontsize), pos, int(angle), float(opacity), image_file, dst_dir,fillcolor)


if __name__ == "__main__":
    main()