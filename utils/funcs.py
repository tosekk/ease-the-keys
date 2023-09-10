# This software is dedicated to the public domain under the Creative Commons Zero (CC0) license.
# SPDX-License-Identifier: CC0-1.0

import bpy


import math


def interpolate_keyframes(favor: float, midpoint: float, fcurve) -> None:

    selected_kpoints = [keyframe for keyframe in fcurve.keyframe_points 
                        if keyframe.select_control_point]

    left = min(selected_kpoints, key=lambda keyframe: keyframe.co_ui.x)
    right = max(selected_kpoints, key=lambda keyframe: keyframe.co_ui.x)

    low = min(selected_kpoints, key=lambda keyframe: keyframe.co_ui.y)
    high = max(selected_kpoints, key=lambda keyframe: keyframe.co_ui.y)

    range_y = high.co_ui.y - low.co_ui.y

    for keyframe in selected_kpoints:

        mapped_x = keyframe.co_ui.x / (right.co_ui.x - left.co_ui.x)
        mapped_favor = map_range(favor, 0.0, 1.0, 1.0, 50.0)

        # Thank you, Junichiro Horikawa https://twitter.com/jhorikawa_err/status/1700894368021012646?s=20
        keyframe.co_ui.y = 1.0 / (1.0 + math.exp(-mapped_favor * (mapped_x - midpoint)))
        keyframe.co_ui.y *= range_y

        if favor < 0.1:
            keyframe.interpolation = "LINEAR"
        elif 0.1 <= favor <= 0.9:
            keyframe.interpolation = "BEZIER"
        else: 
            keyframe.interpolation = "CONSTANT"
            
            

def map_range(value, input_min, input_max, output_min, output_max):
    if input_max - input_min == 0:
        return output_min
    else:
        mapped_value = ((value - input_min) / (input_max - input_min)) * (output_max - output_min) + output_min
        return mapped_value
