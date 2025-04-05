from rembg import remove
from PIL import Image
import io

# Load your input image
input_path = 'image3.jpg'         # Change to your image path
output_path = 'output_image3.png'       # Output will be saved as PNG (supports transparency)

with open(input_path, 'rb') as input_file:
    input_data = input_file.read()

# Remove background
output_data = remove(input_data)

# Save the output image
output_image = Image.open(io.BytesIO(output_data))
output_image.save(output_path)

print(f"Background removed and saved to {output_path}")
