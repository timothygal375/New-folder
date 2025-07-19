import unittest
from qrgen import generate_qr_image, save_qr_image
from PIL import Image
import os

class TestQRGenerator(unittest.TestCase):

    def test_generate_qr_image_returns_image(self):
        img = generate_qr_image("Hello, QR!")
        self.assertIsInstance(img, Image.Image)

    def test_save_qr_image_creates_file(self):
        filename = "test_qr.png"
        save_qr_image("Test QR", filename)
        self.assertTrue(os.path.exists(filename))
        os.remove(filename)

if __name__ == "__main__":
    unittest.main()
