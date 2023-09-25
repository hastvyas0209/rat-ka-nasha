from base64 import standard_b64decode, standard_b64encode
from datetime import datetime

import pytz
import requests

def str_to_b64(__str: str) -> str:
    str_bytes = __str.encode("ascii")
    bytes_b64 = standard_b64encode(str_bytes)
    b64 = bytes_b64.decode("ascii")
    return b64


def b64_to_str(b64: str) -> str:
    bytes_b64 = b64.encode("ascii")
    bytes_str = standard_b64decode(bytes_b64)
    __str = bytes_str.decode("ascii")
    return __str


def get_current_time():
    tz = pytz.timezone("Asia/Kolkata")
    return int(datetime.now(tz).timestamp())


def shorten_url(url):
    site_url = f"https://shrinkforearn.in/api?api=ae3f5cca86a4056dfacf4f0a4ce3d804a44a907c&url={url}&format=text"
    return str(requests.get(site_url).text)
