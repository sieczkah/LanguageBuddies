"""
Avatars are created by using Multiavatar package.
Check the official git repo for more info:
https://github.com/multiavatar/multiavatar-python
They also have a webpage. Check it out!
https://multiavatar.com/
"""

from multiavatar.multiavatar import multiavatar


def create_avatar(avatar_name):
    avatar_name = str(avatar_name)
    svg_code = multiavatar(avatar_name, None, None)

    return svg_code
