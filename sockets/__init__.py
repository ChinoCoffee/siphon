
from bpy.types import NodeSocket


class SiphonNodeSocket(NodeSocket):
    bl_idname = "SiphonNodeSocket"
    bl_label = "Siphon Node Socket"

    def draw(self, context, layout, node, x):
        layout.label(self.name)

    def draw_color(self, context, node):
        return (1,1,1,1)
