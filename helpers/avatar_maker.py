"""
Avatars are created by using Multiavatar package.
Check the official git repo for more info:
https://github.com/multiavatar/multiavatar-python
They also have a webpage. Check it out!
https://multiavatar.com/
"""

from random import choices
from string import ascii_letters

from multiavatar.multiavatar import multiavatar

ASCII = ascii_letters + "1234567890!@#$%"


def create_avatar(avatar_name="random"):
    avatar_name = str(avatar_name)
    if avatar_name == "random":
        avatar_name = "".join(choices(ASCII, k=16))

    svg_code = multiavatar(avatar_name, None, None)

    return svg_code
