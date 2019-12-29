#    Rigify for MB-Lab
#    Copyright (C) 2019 Daniel Engler

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.

#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

bl_info = {
    "name": "MB-Lab-Rigify",
    "description": "Backported rigify rig for MB-Lab",
    "author": "Daniel Engler",
    "version": (2, 79, 0),
    "blender": (2, 79, 0),
    "location": "View3D > Tools > Rigify for MB-Lab",
    "category": "Characters"
}

import bpy

from .add_rig import RIGIFYFORMBLAB_OT_addrig
from .generate_rig import RIGIFYFORMBLAB_OT_generaterig
from .panel import RIGIFYFORMBLAB_OT_enable_rigify, RIGIFYFORMBLAB_PT_panel
from .rename_vertex_groups import (RIGIFYFORMBLAB_OT_rename_vertex_groups,
                                   RIGIFYFORMBLAB_OT_unrename_vertex_groups)
from .backport import make_annotations

# List of the name of the classes inherited from Blender types like
# AddonPreferences, Operator, Panel etc
# Dependency order matters

classes = (
   RIGIFYFORMBLAB_OT_addrig,
   RIGIFYFORMBLAB_OT_rename_vertex_groups,
   RIGIFYFORMBLAB_OT_unrename_vertex_groups,
   RIGIFYFORMBLAB_OT_generaterig,
   RIGIFYFORMBLAB_OT_enable_rigify,
   RIGIFYFORMBLAB_PT_panel
)

def register():
    for cls in classes:
        make_annotations(cls)
        bpy.utils.register_class(cls)

def unregister():  # note how unregistering is done in reverse
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)

if __name__ == "__main__":
    register()
