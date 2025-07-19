"""
qrgen - A simple Python library for generating QR codes from text.
"""

__version__ = "0.1.0"

from .generator import generate_qr_image, save_qr_image

__all__ = ["generate_qr_image", "save_qr_image"]

