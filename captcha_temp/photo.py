from PIL import Image, ImageEnhance

def photo_bright():
    image = Image.open('captcha_temp/secpic4.png')

    if image.mode != "RGB":
        image = image.convert("RGB")

    brightness_factor = 1.2
    enhancer_b = ImageEnhance.Brightness(image)
    bright_img = enhancer_b.enhance(brightness_factor)

    contrast_factor = 1.5
    enhancer_c = ImageEnhance.Contrast(bright_img)
    final_img = enhancer_c.enhance(contrast_factor)

    final_img = final_img.convert('1')
    final_img.save("capthca_temp/result.png")