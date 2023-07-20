# --------------------------------------------------------------------------
# Ease The Keys Blender Add-on
# Version: v0.1.0
# Author: Zhandos Kadyrkulov
# License: CC0-v1.0 Universal (https://creativecommons.org/publicdomain/zero/1.0/)
# Description: Helps easing densely populated keyframes
# --------------------------------------------------------------------------

bl_info = {
    "name": "Ease the Keys",
    "author": "Zhandos Kadyrkulov",
    "version": (0, 1, 0),
    "blender": (3, 00, 0),
    "description": "Helps easing densely populated keyframes",
    "location": "Graph Editor -> Sidebar",
    "category": "Animation"
}


import bpy


from . import ui
from . import utils


def register():
    pass


def unregister():
    pass


if __name__ == "__main__":
    register()