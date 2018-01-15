"""
Copyright (C) 2018 unikko <chino.coffee.1204@gmail.com>


This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""


bl_info = {
    "name": "Siphon",
    "author": "unikko",
    "version": (0, 0, 0),
    "blender": (2, 78, 0),
    "location": "",
    "description": "Siphon is a blender addon specialized for creating illustrations",
    "warning": "",
    "support": "TESTING",
    "wiki_url": "",
    "tracker_url": "",
    "category": "Node",
}



import bpy
import traceback


from . import operators


def siphon_startup(*args, **kwargs):
    print("siphon_startup")


def save_pre_operations(*args, **kwargs):
    print("save_pre")


def register():
    bpy.app.handlers.load_post.append(siphon_startup)
    bpy.app.handlers.save_pre.append(save_pre_operations)
    bpy.utils.register_class(operators.ViewMapSnapshot)

    """
    try:
        bpy.utils.register_module(__name__)
    except:
        traceback.print_exc()
    """
    print("hello from siphon")

    #register_keymaps()


def unregister():
    bpy.app.handlers.load_post.remove(siphon_startup)
    bpy.app.handlers.save_pre.remove(save_pre_operations)
    bpy.utils.unregister_class(operators.ViewMapSnapshot)

    #unregister_keymaps()

    """
    try:
        bpy.utils.unregister_module(__name__)
    except:
        traceback.print_exc()
    """
