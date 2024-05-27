import json
import os
from PIL import Image
from colorsys import rgb_to_hls, hls_to_rgb

def load_json(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r') as json_file:
        return json.load(json_file)

def adjust_lightness(color_a, color_al, color_b):
    def rgba_to_hls(rgba):
        # Normalize RGB values to [0, 1] range and ignore alpha for conversion
        rgb = [x / 255.0 for x in rgba[:3]]
        return rgb_to_hls(*rgb)

    def hls_to_rgba(hls, alpha):
        # Convert HLS back to RGB and denormalize to [0, 255] range
        rgb = hls_to_rgb(*hls)
        return [int(x * 255) for x in rgb] + [alpha]

    # Convert to HLS
    hls_a = rgba_to_hls(color_a)
    hls_al = rgba_to_hls(color_al)
    hls_b = rgba_to_hls(color_b)

    # Calculate the lightness adjustment factor
    lightness_adjustment = hls_al[1] / hls_a[1]

    # Apply the lightness adjustment to Color B
    hls_bl = (hls_b[0], hls_b[1] * lightness_adjustment, hls_b[2])

    # Convert back to RGBA
    color_bl = hls_to_rgba(hls_bl, color_b[3])

    return color_bl

def hex_to_rgba(hex_color):
    """Convert HEX color to RGBA."""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4)) + (255,)

def adjust_color(original_color, relative_color):
    """Adjust the base color with the relative color."""
    return tuple(min(max(bc + rc, 0), 255) for bc, rc in zip(original_color, relative_color))

def generate_image_from_json_data(json_data, generate_color, image_size):
    """Generate an image from JSON data and a base color."""
    # Create a blank image with transparency
    img = Image.new("RGBA", image_size, (0, 0, 0, 0))
    pixels = img.load()

    # Adjust colors and fill rectangles
    for rel_color_str, rectangles in json_data.items():
        if rel_color_str == "original_color":
            continue  # Skip the original_color entry

        rel_color = tuple(map(int, rel_color_str.strip("()").split(", ")))
        adjusted_color = adjust_color(generate_color, rel_color)
        
        for rect in rectangles:
            # print(rect)
            from_x, from_y, to_x, to_y = rect[0], rect[1], rect[2], rect[3]
            for x in range(from_x, to_x + 1):
                for y in range(from_y, to_y + 1):            
                    pixels[x, y] = adjusted_color

    return img

def generate_image_from_json(json_path, generate_base_color, image_path):

    if json_path == None:        
        # Search for json files in the current directory
        json_files = [f for f in os.listdir('.') if f.endswith('.json')]
        json_files.append('Enter file path manually')

        # Display files for selection (example implementation for manual selection)
        print("Select a JSON file:")
        for idx, file in enumerate(json_files):
            print(f"{idx + 1}. {file}")

        # Get user selection
        selection = int(input("Enter the number corresponding to the file: ")) - 1

        if selection == len(json_files) - 1:
            json_path = input("Enter the full file path: ")
        else:
            json_path = json_files[selection]

    # Load JSON data
    relative_color_rectangles = load_json(json_path)

    # Extract and remove dimensions from JSON data
    dimensions = relative_color_rectangles.pop("dimensions")
    image_size = (dimensions["width"], dimensions["height"])

    original_color = relative_color_rectangles.pop("base_color")
    original_color = (original_color[0], original_color[1], original_color[2], original_color[3])
    compare_color = (61, 174, 233, 255)

    # Convert generate_color from HEX to RGBA
    generate_base_color = hex_to_rgba(generate_base_color)

    # Calculate color difference
    generate_base_color = adjust_lightness(compare_color, original_color, generate_base_color)
    
    # Generate the image
    img = generate_image_from_json_data(relative_color_rectangles, generate_base_color, image_size)

    # Save or display the image
    img.save(image_path)
