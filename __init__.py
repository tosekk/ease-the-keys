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


from . import _reload_
from . import ui
from . import utils


_reload_.reload_modules()


def register():
    utils.register_modules()
    ui.register_modules()


def unregister():
    ui.unregister_modules()
    utils.unregister_modules()


if __name__ == "__main__":
    register()