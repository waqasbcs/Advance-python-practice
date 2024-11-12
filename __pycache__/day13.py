import os
from PIL import Image
from rembg import remove

# Define paths
input_path = r'__pycache__/clgot.jpeg'
output_dir = r'output'
output_path = os.path.join(output_dir, 'clgot_output.png')

# Create output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Process the image
inp = Image.open(input_path)
output = remove(inp)
output.save(output_path)
print(f"Image saved at {output_path}")
