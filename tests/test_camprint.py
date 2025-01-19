import unittest
from PIL import Image
import sys
import os

# Add parent directory to path to import camprint
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from camprint import camprint

class TestCamPrint(unittest.TestCase):
    def test_preprocess_image(self):
        # Create a test image
        test_image = Image.new('RGB', (640, 480), color='white')
        
        # Process the image
        processed = camprint.preprocess_image(test_image)
        
        # Check if the processed image has the correct width
        self.assertEqual(processed.size[0], 384)
        
        # Check if the image is binary (1-bit)
        self.assertEqual(processed.mode, '1')

if __name__ == '__main__':
    unittest.main() 