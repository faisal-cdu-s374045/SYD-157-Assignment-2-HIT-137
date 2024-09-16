from PIL import Image
import time

# Generate the number 'n'
current_time = int(time.time())
generated_number = (current_time % 100) + 50
if generated_number % 2 == 0:
    generated_number += 10

print(f"Generated Number: {generated_number}")

# Open the image
img = Image.open("chapter1.jpg")
pixels = img.load()

# Getting image size
width, height = img.size

# Modify pixels by adding the generated number and sum red values
red_sum = 0
for y in range(height):
    for x in range(width):
        r, g, b = pixels[x, y]
        # Add generated_number to (r, g, b) with modulo to avoid overflow
        new_r = (r + generated_number) % 256
        new_g = (g + generated_number) % 256
        new_b = (b + generated_number) % 256
        # Save the new pixel values
        pixels[x, y] = (new_r, new_g, new_b)
        # Sum the red values
        red_sum += new_r

# Save the modified image
img.save("chapter1out.png")
print(f"Sum of red pixel values: {red_sum}")
