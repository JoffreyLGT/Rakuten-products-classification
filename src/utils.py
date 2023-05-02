import requests


def load_lottieurl(url):
    """
    Fetch lottie anymation from URL
    """
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
