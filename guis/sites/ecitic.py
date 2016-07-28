
"""
config the name of site , it will provide as the site param to post to API server.
"""
site_name = 'etrade.cs.ecitic.com'

"""
ext name of the CAPTCHA image
"""
image_ext = ".jpg"

def get_entry_page():
    """
    the entry page contains the captcha
    we start a session from this page
    :return: url of entry page
    """
    return "http://etrade.cs.ecitic.com/"


def get_captcha_url(page_content, session):
    """
    get the url of captcha
    :param page_content: the content of page from get_entry_page
    :return: the url of captcha
    """
    return "https://etrade.cs.ecitic.com/webtrade/pic/Kaptcha.jpg"


