# This software is dedicated to the public domain under the Creative Commons Zero (CC0) license.
# SPDX-License-Identifier: CC0-1.0

import bpy
from bpy.types import Operator


class ANIM_OT_EaseTheKeys(Operator):
    """Ease the Keys UI Button"""
    bl_idname = "etk.ease_keys"
    bl_label = "Ease the Keys"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        scene = context.scene
        props = scene.etk
        selected_fcurves = context.selected_visible_fcurves
        interpolation = 'BEZIER'

        if props.favor == 0.0:
            interpolation = 'LINEAR'
        elif props.favor == 1.0:
            interpolation = 'CONSTANT'

        for index, fcurve in enumerate(selected_fcurves):
            selected_kpoints = [keyframe for keyframe in fcurve.keyframe_points if keyframe.select_control_point]

            leftmost = min(selected_kpoints, key=lambda keyframe: keyframe.co.x)
            rightmost = max(selected_kpoints, key=lambda keyframe: keyframe.co.x)
            lowest = min((leftmost, rightmost), key=lambda keyframe: keyframe.co.y)
            highest = max((leftmost, rightmost), key=lambda keyframe: keyframe.co.y)

            range_x = rightmost.co.x - leftmost.co.x
            range_y = highest.co.y - lowest.co.x

            middle_x = leftmost.co.x + range_x * props.midpoint
            middle_y = lowest.co.y + range_y * props.midpoint

            middlepoint = fcurve.keyframe_points.insert(middle_x, middle_y)

            print(leftmost.co.x, rightmost.co.x, sep=" --- ")

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