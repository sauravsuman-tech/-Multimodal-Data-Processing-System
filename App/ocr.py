from PIL import Image
import pytesseract
from pathlib import Path

def ocr_image_file(path: Path) -> str:
    img = Image.open(str(path))
    text = pytesseract.image_to_string(img)
    return text
