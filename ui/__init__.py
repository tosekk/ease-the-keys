# This software is dedicated to the public domain under the Creative Commons Zero (CC0) license.
# SPDX-License-Identifier: CC0-1.0

from . import operators
from . import panels


def register_modules():
    operators.register_classes()
    panels.register_classes()


def unregister_modules():
    panels.unregister_classes()
    operators.unregister_classes()