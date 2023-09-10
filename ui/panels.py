# This software is dedicated to the public domain under the Creative Commons Zero (CC0) license.
# SPDX-License-Identifier: CC0-1.0

import bpy
from bpy.types import Panel


class ANIM_PT_EaseTheKeys(Panel):
    """Ease the Keys UI Panel"""
    bl_label = "Ease the Keys"
    bl_space_type = "GRAPH_EDITOR"
    bl_region_type = "UI"
    bl_context = "object"
    bl_category = "Ease the Keys"

    @classmethod
    def poll(cls, context):
        return context.active_object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        properties = scene.etk

        col = layout.column()
        col.scale_y = 1.2

        col.prop(properties, "favor")
        col.prop(properties, "midpoint")


classes = [
    ANIM_PT_EaseTheKeys
]


def register_classes():
    for cls in classes:
        bpy.utils.register_class(cls)
    

def unregister_classes():
    for cls in classes:
        bpy.utils.unregister_class(cls)
