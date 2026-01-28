import base64
import io


def image_to_base64(image):
    """Converte image to PIL from string Base64"""
    if image is None:
        return None

    buffered = io.BytesIO()
    image.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str
