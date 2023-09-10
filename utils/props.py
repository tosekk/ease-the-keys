# This software is dedicated to the public domain under the Creative Commons Zero (CC0) license.
# SPDX-License-Identifier: CC0-1.0

import bpy
from bpy.props import FloatProperty, PointerProperty
from bpy.types import PropertyGroup


from . import funcs


class ETKProperties(PropertyGroup):
    """Ease the Keys Add-On Properties"""

    favor: FloatProperty(
        name="Favor",
        description="Defines the interpolation of eased keys",
        default=0.5,
        min=0.0,
        max=1.0,
        update=lambda self, context: self.update_fcurve(context)
    )

    midpoint: FloatProperty(
        name="Midpoint",
        description="Defines the midpoint position of eased keys",
        default=0.5,
        min=0.0,
        max=1.0,
        update=lambda self, context: self.update_fcurve(context)
    )


    def update_fcurve(self, context):
        selected_fcurves = context.selected_visible_fcurves

        for index, fcurve in enumerate(selected_fcurves):
            funcs.interpolate_keyframes(
                self.favor, self.midpoint, fcurve)

            fcurve.update()


def register_properties():
    bpy.utils.register_class(ETKProperties)

    bpy.types.Scene.etk = PointerProperty(type=ETKProperties)


def unregister_properties():
    bpy.utils.unregister_class(ETKProperties)

    del bpy.types.Scene.etk