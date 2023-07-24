# # This software is dedicated to the public domain under the Creative Commons Zero (CC0) license.
# # SPDX-License-Identifier: CC0-1.0

# import bpy

# def interpolate_keyframes(region_start, region_end, favor, midpoint):
#     # Get the active object and its animation data
#     obj = bpy.context.active_object
#     anim_data = obj.animation_data

#     if anim_data is None or anim_data.action is None:
#         print("No active animation data found.")
#         return

#     action = anim_data.action
#     fcurve_dict = {}  # Dictionary to store fcurves by data path

#     # Collect all fcurves in the specified region
#     for fcurve in action.fcurves:
#         for keyframe_point in fcurve.keyframe_points:
#             frame = keyframe_point.co.x
#             if region_start <= frame <= region_end:
#                 if fcurve.data_path in fcurve_dict:
#                     fcurve_dict[fcurve.data_path].append(keyframe_point)
#                 else:
#                     fcurve_dict[fcurve.data_path] = [keyframe_point]

#     # Interpolate the selected keyframes
#     for data_path, keyframe_points in fcurve_dict.items():
#         if len(keyframe_points) < 2:
#             continue

#         first_point = keyframe_points[0]
#         last_point = keyframe_points[-1]
#         total_frames = last_point.co.x - first_point.co.x
#         mid_frame = first_point.co.x + total_frames * midpoint

#         for point in keyframe_points:
#             frame = point.co.x
#             t = (frame - first_point.co.x) / total_frames

#             if frame < mid_frame:
#                 factor = t / midpoint if midpoint > 0 else 0
#             else:
#                 factor = (1 - t) / (1 - midpoint) if midpoint < 1 else 0

#             if favor == 0:  # Linear interpolation
#                 point.interpolation = 'LINEAR'
#             elif favor == 1:  # Constant interpolation
#                 point.interpolation = 'CONSTANT'

#             # Interpolate the value
#             for i in range(len(point.co)):
#                 point.co[i] = (1 - factor) * first_point.co[i] + factor * last_point.co[i]

# # Example usage:
# # Define the region of keyframes to select and interpolate
# region_start = 1  # Start frame of the region
# region_end = 50   # End frame of the region
# favor = 0.5       # 0 for linear, 1 for constant
# midpoint = 0.5    # 0 to 1 (0 means midpoint on the first keyframe, 1 means on the last keyframe)

# interpolate_keyframes(region_start, region_end, favor, midpoint)
