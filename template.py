import argparse
from PIL import Image, ImageDraw, ImageFont

from config import GRID_SIZE
import grid
import pin_generator
import label_handler




# -> https://stackoverflow.com/questions/5414639/python-imaging-library-text-rendering

# change this to use the one found in input/ folder
test_data = {
    "columns": 8,
    "rows": 3,
    "categories": {
        # we could also just define categories without color
        "PSU": "red",
        "ADC": "green",
        "IO": "blue"
    }
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug', default=False)
    args = parser.parse_args()
    if args.debug:
        print("Use the test_data construct")
    else:
        print("Use 'sample_input/24pin_template.txt' file")

    image_size = (test_data["columns"]+1)*GRID_SIZE, (test_data["rows"]+1)*GRID_SIZE
    template_image = Image.new("RGB", image_size, (255, 255, 255))
    template_draw = ImageDraw.Draw(template_image)

    font_size = 15
    font = ImageFont.truetype("arial.ttf", font_size)
    

    g = grid.create_grid(test_data["columns"], test_data["rows"])
    #print(f'total grid {g} ')
    for col in g:
        for row_element in col:
            if row_element.is_graphic():
                grid_index = row_element.index
                label, category = label_handler.get_label_and_cat(grid_index)
                try:
                    pin_color = test_data["categories"][category]
                except:
                    pin_color = "black"
                pin = pin_generator.draw_pin(text=label, color=pin_color)
                
                #pin =1 Image.open("square.png")
                x, y = row_element.middle()
                template_image.paste(pin, (int(x-GRID_SIZE/2),int(y-GRID_SIZE/2)))
            else:
                x, y = row_element.middle()
                x -= GRID_SIZE/4
                #print(f'text "{row_element.text}" at {x}, {y}')
                template_draw.text((x, y), str(row_element.text), fill=0, font=font)


    template_image.show()
    template_image.save('output_template.png')
    


if __name__ == "__main__":
	main()