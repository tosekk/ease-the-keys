# This software is dedicated to the public domain under the Creative Commons Zero (CC0) license.
# SPDX-License-Identifier: CC0-1.0

import bpy
from bpy.types import Operator


class ANIM_OT_EaseTheKeys(Operator):
    """Ease the Keys UI Button"""
    bl_idname = "object.etk.ease_keys"
    bl_label = "Ease the Keys"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        return {'FINISHED'}


classes = [
    ANIM_OT_EaseTheKeys
]


def register_classes():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister_classes():
    for cls in classes:
        bpy.utils.unregister_class(cls)