import bpy
import parameter_editor
import pickle

from freestyle.types import (
    Operators,
)



class ViewMapSnapshot(bpy.types.Operator):
    bl_idname = "object.viewmap_snapshot"
    bl_label = "ViewMap Snapshot"
    bl_options = {'REGISTER', 'UNDO'}
    bl_space_type = "VIEW_3D"
    bl_region_type = "TOOLS"

    @classmethod
    def poll(cls, context):
        return True

    def execute(self, context):
        bpy.context.scene.render.use_freestyle = True
        bpy.context.scene.render.layers.active.use_freestyle = True

        def lineset_post_viewmap(scene, layer, lineset):
            print(type(Operators()))
            print(dir(Operators()))
            print(Operators().get_strokes_size())

            # I want to pickle viewmap (Operators() ? )objects...
            for i in range(Operators().get_strokes_size()):
                for j in Operators().get_stroke_from_index(i):
                    print(j.point_3d.x, j.point_3d.y, j.point_3d.z)

            # [FIXME]
            x = pickle.dumps(Operators())
            print(x)

        def post_render(scene):
            parameter_editor.callbacks_lineset_post.remove(lineset_post_viewmap)
            bpy.app.handlers.render_post.remove(post_render)

        parameter_editor.callbacks_lineset_post.append(lineset_post_viewmap)
        bpy.app.handlers.render_post.append(post_render)

        bpy.ops.render.render()

        return {'FINISHED'}
