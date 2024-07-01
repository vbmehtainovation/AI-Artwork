from PIL import Image,ImageDraw,ImageChops
import random
import colorsys


    

def random_color():
    h = random.random()
    s = 1
    v = 1
    float_rgb = colorsys.hsv_to_rgb(h,s,v)
    rgb = [int(x * 225)for x in float_rgb]
    return tuple(rgb) 
random_color()

def interpolate(start_color, end_color):
    recipocal =float(random.uniform(0.1,1))
    recipocal=float(recipocal) 
    factor = recipocal-1
    return(
        int(start_color[0] * recipocal + end_color[0] *factor),
        int(start_color[1] * recipocal + end_color[1] *factor),
        int(start_color[2] * recipocal + end_color[2] *factor),
    )
def generate_art(path:str):
    print("Drawing...")
    image_size_px = 1000
    image_bg_color = (0,0,0)
    start_color = random_color()
    end_color = random_color()
    image=Image.new("RGB",size=(image_size_px, image_size_px),color=(image_bg_color))


    draw = ImageDraw.Draw(image)
    for _ in range(100000):
        random_point_1 = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px),
        )
        random_point_2= (
            random.randint(0,image_size_px), 
            random.randint(0,image_size_px),
        )
        random_point_3 = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px),
        )
        random_point_4= (
            random.randint(0,image_size_px), 
            random.randint(0,image_size_px),
        )
        random_point_5 = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px),
        )
        random_point_6= (
            random.randint(0,image_size_px), 
            random.randint(0,image_size_px),
        )
        random_point_7 = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px),
        )
        random_point_8= (
            random.randint(0,image_size_px), 
            random.randint(0,image_size_px),
        )
        random_point_9 = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px),
        )
        random_point_10= (
            random.randint(0,image_size_px), 
            random.randint(0,image_size_px),
        )
        random_point_11 = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px),
        )
        random_point_12= (
            random.randint(0,image_size_px), 
            random.randint(0,image_size_px),
        )
        random_point_13 = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px),
        )
        random_point_14= (
            random.randint(0,image_size_px), 
            random.randint(0,image_size_px),
        )
        random_point_15 = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px),
        )
        random_point_16= (
            random.randint(0,image_size_px), 
            random.randint(0,image_size_px),
        )
        random_point_17 = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px),
        )
        random_point_18= (
            random.randint(0,image_size_px), 
            random.randint(0,image_size_px),
        )
        random_point_19= (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px),
        )
        random_point_20= (
            random.randint(0,image_size_px), 
            random.randint(0,image_size_px),
        )
        random_point_21= (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px),
        )
        random_point_22= (
            random.randint(0,image_size_px), 
            random.randint(0,image_size_px),
        )
        random_point_23= (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px),
        )
        random_point_24= (
            random.randint(0,image_size_px), 
            random.randint(0,image_size_px),
        )
        random_point_25= (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px),
        )
        random_point_26= (
            random.randint(0,image_size_px), 
            random.randint(0,image_size_px),
        )
        random_point_27 = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px),
        )
        random_point_28= (
            random.randint(0,image_size_px), 
            random.randint(0,image_size_px),
        )
        random_point_29 = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px),
        )
        random_point_30= (
            random.randint(0,image_size_px), 
            random.randint(0,image_size_px),
        )
        random_point_31 = (
            random.randint(0, image_size_px), 
            random.randint(0, image_size_px),
        )
        random_point_32= (
            random.randint(0,image_size_px), 
            random.randint(0,image_size_px),
        )
    overlay_image = Image.new("RGB",size=(image_size_px, image_size_px),color=(image_bg_color))
    overlay_draw = ImageDraw.Draw(overlay_image)
    line_A = (random_point_1, random_point_2,random_point_3,random_point_4)
    line_B= (random_point_5, random_point_6,random_point_7,random_point_8)
    line_C= (random_point_9, random_point_10,random_point_11,random_point_12)
    line_D= (random_point_13, random_point_14,random_point_15,random_point_16)
    line_E= (random_point_17, random_point_18,random_point_19,random_point_20)
    line_F= (random_point_21, random_point_22,random_point_23,random_point_24)
    line_G= (random_point_25, random_point_26,random_point_27,random_point_28)
    line_H= (random_point_29, random_point_30,random_point_31,random_point_32)
    thicknessA = random.randint(5,5)
    thicknessB = random.randint(5,5)
    thicknessC = random.randint(5,5)
    thicknessD = random.randint(5,5)
    overlay_draw.line(line_A,fill=(interpolate(start_color , end_color)),width=thicknessA)
    image = ImageChops.add(image,overlay_image)
    overlay_draw.line(line_B,fill=(interpolate(start_color , end_color)),width=thicknessB)
    image = ImageChops.add(image,overlay_image)
    overlay_draw.line(line_C,fill=(interpolate(start_color , end_color)),width=thicknessC)
    image = ImageChops.add(image,overlay_image)
    overlay_draw.line(line_D,fill=(interpolate(start_color , end_color)),width=thicknessD)
    image = ImageChops.add(image,overlay_image)
    overlay_draw.line(line_E,fill=(interpolate(start_color , end_color)),width=thicknessA)
    image = ImageChops.add(image,overlay_image)
    overlay_draw.line(line_F,fill=(interpolate(start_color , end_color)),width=thicknessB)
    image = ImageChops.add(image,overlay_image)
    overlay_draw.line(line_G,fill=(interpolate(start_color , end_color)),width=thicknessC)
    image = ImageChops.add(image,overlay_image)
    overlay_draw.line(line_H,fill=(interpolate(start_color , end_color)),width=thicknessD)
    image = ImageChops.add(image,overlay_image)
    image.save(path)

if __name__ == "__main__":
    for i in range(0,10):
            generate_art(f"test_image{i}.png")    
