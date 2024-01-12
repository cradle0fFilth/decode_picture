import json

def hex_to_png(hex_data, output_file_path):
    binary_data = bytes.fromhex(hex_data)
    with open(output_file_path, 'wb') as file:
        file.write(binary_data)

for i in range(10000):
    dir = f'../atomlizard1/atomlizard1/item-{i}.json'
    with open(dir,'r') as file:
        data = json.load(file)
    png_data = data["data"]["image.png"]["$b"]
    output_file_path = f'pics/output_image{i}.png'
    hex_to_png(png_data, output_file_path)
    print(f"图片已保存为 {output_file_path}")
