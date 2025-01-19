import serial
import subprocess
from PIL import Image, ImageOps, ImageEnhance

# Function to capture an image using libcamera-still
def capture_image(output_path="captured.jpg"):
    """
    Captures an image using libcamera-still and saves it to the specified path.
    """
    try:
        subprocess.run(["libcamera-still", "-o", output_path, "--width", "640", "--height", "480", "-t", "1000"], check=True)
        return output_path
    except subprocess.CalledProcessError as e:
        raise Exception(f"Failed to capture image: {e}")

# Function to preprocess the image for better thermal printing
def preprocess_image(img):
    """
    Enhances and preprocesses the image for thermal printing.
    
    - Resizes to 384 pixels wide (or printer width).
    - Converts to high-contrast monochrome (1-bit).
    - Enhances contrast and sharpness aggressively for better clarity.
    - Applies adaptive thresholding for better detail visibility.
    """
    width = 384  # Fixed width for the printer
    aspect_ratio = img.height / img.width
    height = int(width * aspect_ratio)  # Maintain the original aspect ratio
    img = img.resize((width, height))

    img = ImageEnhance.Contrast(img).enhance(3.0)  # Increase contrast more aggressively
    img = ImageEnhance.Sharpness(img).enhance(3.0)  # Increase sharpness further
    img = img.convert('L')  # Convert to grayscale
    
    # Apply adaptive thresholding to enhance details
    img = img.point(lambda x: 0 if x < 128 else 255, '1')  # Binarize image
    
    return img

# Function to convert an image to ESC/POS binary data
def image_to_escpos(img):
    """
    Converts a PIL Image object to ESC/POS binary data for printing.
    """
    width, height = img.size
    pixels = img.load()
    escpos_data = b"\x1B\x40"  # Initialize printer (ESC @)

    for y in range(height):
        row_data = b""
        for x in range(0, width, 8):
            byte = 0
            for bit in range(8):
                if x + bit < width:
                    pixel = pixels[x + bit, y]
                    if pixel == 0:  # Black pixel
                        byte |= (1 << (7 - bit))
            row_data += bytes([byte])

        escpos_data += b'\x1D\x76\x30\x00'  # GS v 0 (raster bit image mode)
        escpos_data += bytes([width // 8, 0, 1, 0])
        escpos_data += row_data

    escpos_data += b'\x1D\x56\x00'  # Cut paper
    return escpos_data

# Main script
def main():
    """
    Captures an image, preprocesses it, and sends it to the thermal printer.
    """
    printer_port = '/dev/serial0'  # Serial port where the printer is connected
    baud_rate = 9600

    print("Capturing image...")
    image_path = capture_image()

    print("Loading captured image...")
    img = Image.open(image_path)

    print("Preprocessing image...")
    img = preprocess_image(img)

    ser = serial.Serial(printer_port, baud_rate)

    print("Converting image to ESC/POS format...")
    escpos_data = image_to_escpos(img)

    print("Sending data to printer...")
    ser.write(escpos_data)
    ser.close()
    print("Image printed successfully.")

if __name__ == "__main__":
    main()
