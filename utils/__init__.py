# This software is dedicated to the public domain under the Creative Commons Zero (CC0) license.
# SPDX-License-Identifier: CC0-1.0

from . import props
from . import funcs


def register_modules():
    props.register_properties()


def unregister_modules():
    props.unregister_properties()