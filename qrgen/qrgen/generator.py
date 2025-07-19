import qrcode
from io import BytesIO
from PIL import Image

def generate_qr_image(text: str) -> Image.Image:
    """
    Generate a QR code image from the given text.

    Args:
        text (str): The text to encode into a QR code.

    Returns:
        PIL.Image.Image: The generated QR code image.
    """
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color="black", back_color="white")
    return img.convert("RGB")  # This returns a true PIL.Image.Image



def save_qr_image(text: str, filename: str = "qr.png") -> None:
    """
    Generate a QR code from text and save it to a file.

    Args:
        text (str): The text to encode into a QR code.
        filename (str): The file path to save the QR code image.
    """
    img = generate_qr_image(text)
    img.save(filename)
