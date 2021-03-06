import bpy
import platform
import time
from random import randint

# IMPORTA SPLINT COM ARMATURE

def ImportaSplintDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene


    if platform.system() == "Linux":

        dirScript = bpy.utils.user_resource('SCRIPTS')

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
#        section   = "\\Collection\\"
#        object    = "SPLINT"
        section   = "\\Object\\"
        object    = "SPLINT"

    if platform.system() == "Darwin":

        dirScript = bpy.utils.user_resource('SCRIPTS')

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Object\\"
        object    = "SPLINT"

    if platform.system() == "Windows":

        dirScript = 'C:/OrtogOnBlender/Blender280/2.80/scripts/'

        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
        section   = "\\Object\\"
        object    = "SPLINT"


#    if platform.system() == "Darwin":

#        dirScript = bpy.utils.user_resource('SCRIPTS')

#        blendfile = dirScript+"addons/OrtogOnBlender-master/objetos.blend"
#        section   = "\\Group\\"
#        object    = "SPLINT"


    filepath  = blendfile + section + object
    directory = blendfile + section
    filename  = object

    bpy.ops.wm.append(
        filepath=filepath,
        filename=filename,
        directory=directory)

class ImportaSplint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.importa_splint"
    bl_label = "Importa Splint"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        ImportaSplintDef(self, context)
        return {'FINISHED'}

bpy.utils.register_class(ImportaSplint)

# CRIA EMPTIES INTERMEDIÁRIOS

def CriaSplintDef(self, context):

    context = bpy.context
    obj = context.active_object
    scn = context.scene

    bpy.ops.object.select_all(action='DESELECT')

    a = bpy.data.objects['Tooth 8']
    b = bpy.data.objects['Tooth 25']

    bpy.ops.object.select_all(action='DESELECT')
    a.select_set(True)
    b.select_set(True)
    bpy.context.view_layer.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP1141"
    bpy.context.object.empty_display_size = .5

    '''
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP1141']

    bpy.ops.object.select_all(action='DESELECT')
    a.select_set(True)
    b.select_set(True)
    bpy.context.view_layer.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    '''

    # ----------------------------

    a = bpy.data.objects['Tooth 9']
    b = bpy.data.objects['Tooth 24']

    bpy.ops.object.select_all(action='DESELECT')
    a.select_set(True)
    b.select_set(True)
    bpy.context.view_layer.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP2131"
    bpy.context.object.empty_display_size = .5

    '''
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP2131']

    bpy.ops.object.select_all(action='DESELECT')
    a.select_set(True)
    b.select_set(True)
    bpy.context.view_layer.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    '''
    # ----------------------------

    a = bpy.data.objects['Tooth 11']
    b = bpy.data.objects['Tooth 22']

    bpy.ops.object.select_all(action='DESELECT')
    a.select_set(True)
    b.select_set(True)
    bpy.context.view_layer.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP2333"
    bpy.context.object.empty_display_size = .5

    '''
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP2333']

    bpy.ops.object.select_all(action='DESELECT')
    a.select_set(True)
    b.select_set(True)
    bpy.context.view_layer.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    '''
    # ----------------------------

    a = bpy.data.objects['Tooth 6']
    b = bpy.data.objects['Tooth 27']

    bpy.ops.object.select_all(action='DESELECT')
    a.select_set(True)
    b.select_set(True)
    bpy.context.view_layer.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP1343"
    bpy.context.object.empty_display_size = .5

    '''
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP1343']

    bpy.ops.object.select_all(action='DESELECT')
    a.select_set(True)
    b.select_set(True)
    bpy.context.view_layer.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    '''
    # ----------------------------

    a = bpy.data.objects['Tooth 14']
    b = bpy.data.objects['Tooth 19']

    bpy.ops.object.select_all(action='DESELECT')
    a.select_set(True)
    b.select_set(True)
    bpy.context.view_layer.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP2636"
    bpy.context.object.empty_display_size = .5

    '''
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP2636']

    bpy.ops.object.select_all(action='DESELECT')
    a.select_set(True)
    b.select_set(True)
    bpy.context.view_layer.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    '''
    # ----------------------------

    a = bpy.data.objects['Tooth 3']
    b = bpy.data.objects['Tooth 30']

    bpy.ops.object.select_all(action='DESELECT')
    a.select_set(True)
    b.select_set(True)
    bpy.context.view_layer.objects.active = a
    bpy.ops.view3d.snap_cursor_to_selected()

    bpy.ops.object.empty_add(type='SPHERE')
    bpy.context.object.name = "EMP1646"
    bpy.context.object.empty_display_size = .5

    '''
    a = bpy.data.objects['cm']
    b = bpy.data.objects['EMP1646']

    bpy.ops.object.select_all(action='DESELECT')
    a.select_set(True)
    b.select_set(True)
    bpy.context.view_layer.objects.active = a
    bpy.ops.object.parent_set()
    bpy.ops.object.select_all(action='DESELECT')
    '''
    # ---------------

    bpy.ops.object.importa_splint()

    # --------------

    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP1646']
    a.select_set(True)
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone1646']
    a.select_set(True)
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP1343']
    a.select_set(True)
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone1343']
    a.select_set(True)
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP1141']
    a.select_set(True)
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone1141']
    a.select_set(True)
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP2131']
    a.select_set(True)
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone2131']
    a.select_set(True)
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP2333']
    a.select_set(True)
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone2333']
    a.select_set(True)
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)

    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMP2636']
    a.select_set(True)
    bpy.ops.view3d.snap_cursor_to_selected()
    bpy.ops.object.select_all(action='DESELECT')
    a = bpy.data.objects['EMPbone2636']
    a.select_set(True)
    bpy.ops.view3d.snap_selected_to_cursor(use_offset=False)


class CriaSplint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.cria_splint"
    bl_label = "Cria Splint"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'SPLINT_pronto' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaSplintDef(self, context)

        bpy.ops.object.select_all(action='DESELECT')
        splint = bpy.data.objects['SPLINT']
        splint.select_set(True)
        context.view_layer.objects.active = splint

        bpy.ops.object.convert(target='MESH')
        bpy.context.object.name = "SPLINT_pronto"
        bpy.ops.object.select_all(action='DESELECT')

        objetos = ["Armature", "EMPbone1646", "EMPbone1343", "EMPbone1141", "EMPbone2131", "EMPbone2333", "EMPbone2636", "EMP1646", "EMP1343", "EMP1141", "EMP2131", "EMP2333", "EMP2636"]

        for item in objetos:
            bpy.ops.object.select_all(action='DESELECT')
            ObjAtual = bpy.data.objects[item]
            ObjAtual.select_set(True)
            context.view_layer.objects.active = ObjAtual
            bpy.ops.object.delete(use_global=False)

        SplintFinal = bpy.data.objects['SPLINT_pronto']
        SplintFinal.select_set(True)
        context.view_layer.objects.active = SplintFinal
        bpy.ops.object.collection_link(collection='Collection')

        return {'FINISHED'}

bpy.utils.register_class(CriaSplint)


def DuplicaMaxMandDef():

    bpy.ops.object.select_all(action='DESELECT')

    if bpy.data.objects.get("MaxillaMand") is not None:
        bpy.data.objects['MaxillaMand'].name = "Deletar"


    bpy.data.objects['ma'].select_set(True)
    bpy.data.objects['cm'].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects['ma']

    bpy.ops.object.duplicate()
    bpy.ops.object.join()
    NomeMaterial = "MaxillaMand"+time.strftime("%Y%m%d%H%M%S")

    bpy.context.object.name = "MaxillaMand"

    # Deleta todos os objetos
    for x in bpy.context.object.material_slots:
        bpy.context.object.active_material_index = 0
        bpy.ops.object.material_slot_remove()

    activeObject = bpy.data.objects["MaxillaMand"] #Set active object to variable
    mat = bpy.data.materials.new(name=NomeMaterial) #set new material to variable
    activeObject.data.materials.append(mat) #add the material to the object
    activeObject.active_material.diffuse_color = (randint(20, 100)*.01, randint(20, 100)*.01, randint(20, 100)*.01, 1)

    bpy.data.objects['ma'].hide_set(True)
    bpy.data.objects['cm'].hide_set(True)


class DuplicaMaxMand(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.duplica_max_mand"
    bl_label = "Maxilla Mandible Duplication"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'MaxillaMand' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        DuplicaMaxMandDef()
        return {'FINISHED'}

bpy.utils.register_class(DuplicaMaxMand)


def VisualizaMaxMandDef():

    if bpy.data.objects.get("Splint_result") is not None:
        bpy.data.objects['Splint_result'].name = "SPLINT_ready"

    if bpy.data.objects.get("SPLINT_pronto") is not None:
        bpy.data.objects['SPLINT_pronto'].name = "SPLINT_del"

    if bpy.data.objects.get("MaxillaMand") is not None:
        bpy.data.objects['MaxillaMand'].name = "Deletar"

    bpy.data.objects['ma'].hide_set(False)
    bpy.data.objects['cm'].hide_set(False)


class VisualizaMaxMand(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.visualiza_max_mand"
    bl_label = "Maxilla Mandible View"
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        VisualizaMaxMandDef()
        return {'FINISHED'}

bpy.utils.register_class(VisualizaMaxMand)

class MessageNaoConstaSplintPronto(bpy.types.Operator):
    bl_idname = "object.dialog_operator_falta_splint_pronto"
    bl_label = "Doesn't have SPLINT_pronto, rename it!"

    def execute(self, context):
        message = ("Doesn't have SPLINT_pronto, rename it!")
        self.report({'INFO'}, message)
        return {'FINISHED'}

    def invoke(self, context, event):
        wm = context.window_manager
        return wm.invoke_props_dialog(self)

bpy.utils.register_class(MessageNaoConstaSplintPronto)

def BooleanSplintDef():

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['SPLINT_pronto'].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects['SPLINT_pronto']
    bpy.context.object.name = "Splint_usado"
    bpy.context.object.name = "Splint_usado"

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects['MaxillaMand'].select_set(True)
    bpy.data.objects['Splint_usado'].select_set(True)

    bpy.context.view_layer.objects.active = bpy.data.objects['MaxillaMand']
    bpy.ops.object.booleana_osteo_geral()
    bpy.context.object.name = "Splint_result"



class BooleanSplint(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.boolean_splint"
    bl_label = "Boolean Splint"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Splint_result' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):

        found = 'SPLINT_pronto' in bpy.data.objects

        if found == True:
            bpy.ops.object.duplica_max_mand()
            BooleanSplintDef()

        if found == False:
            bpy.ops.object.dialog_operator_falta_splint_pronto('INVOKE_DEFAULT')

        return {'FINISHED'}

bpy.utils.register_class(BooleanSplint)

def SplintMantemKeyStart(objeto, quadro):

    scn = bpy.context.scene
    obj = bpy.data.objects[objeto]

    animData = obj.animation_data
    action = animData.action
    fcurves = action.fcurves
    current_frame = scn.frame_current

    for i in fcurves:
        i.keyframe_points.insert(quadro, i.keyframe_points[0].co.y) # Primeiro keyframe
        i.keyframe_points[0].co.y += 0 # Atualiza a animação!
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

def SplintMantemKeyEnd(objeto, quadro):

    scn = bpy.context.scene
    obj = bpy.data.objects[objeto]

    animData = obj.animation_data
    action = animData.action
    fcurves = action.fcurves
    current_frame = scn.frame_current

    for i in fcurves:
        i.keyframe_points.insert(quadro, i.keyframe_points[1].co.y) # Primeiro keyframe
        i.keyframe_points[1].co.y += 0 # Atualiza a animação!
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

def SplintMaxilaOrigiMandFinalDef():

        context = bpy.context
        scn = context.scene

        SplintMantemKeyStart('ma', 110)
        SplintMantemKeyEnd('cm', 110)

        SplintMantemKeyEnd('ma', 120)
        SplintMantemKeyEnd('cm', 120)

        bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['Condyle Rotation Point'].select_set(True)
        context.view_layer.objects.active = bpy.data.objects['Condyle Rotation Point']
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                ctx = bpy.context.copy()
                ctx['area'] = area
                ctx['region'] = area.regions[-1]
        #        bpy.ops.view3d.view_selected(ctx)
                bpy.ops.view3d.snap_cursor_to_selected(ctx)
                break
                bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['cm'].select_set(True)
        context.view_layer.objects.active = bpy.data.objects['cm']


class SplintMaxilaOrigiMandFinal(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.splint_maxila_origi_mand_final"
    bl_label = "Splint Maxilla Origin Mandible Final"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Condyle Rotation Point' in bpy.data.objects

        if found == False:
            return False
        else:
            if found == True:
                return True

    def execute(self, context):
        SplintMaxilaOrigiMandFinalDef()
        return {'FINISHED'}

bpy.utils.register_class(SplintMaxilaOrigiMandFinal)


def SplintMandOrigiMaxilaFinalDef():

        context = bpy.context
        scn = context.scene

        SplintMantemKeyStart('cm', 110)
        SplintMantemKeyEnd('ma', 110)

        SplintMantemKeyEnd('ma', 120)
        SplintMantemKeyEnd('cm', 120)

        bpy.context.scene.tool_settings.transform_pivot_point = 'CURSOR'
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['Condyle Rotation Point'].select_set(True)
        context.view_layer.objects.active = bpy.data.objects['Condyle Rotation Point']
        bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                ctx = bpy.context.copy()
                ctx['area'] = area
                ctx['region'] = area.regions[-1]
        #        bpy.ops.view3d.view_selected(ctx)
                bpy.ops.view3d.snap_cursor_to_selected(ctx)
                break
                bpy.ops.wm.redraw_timer(type='DRAW_WIN_SWAP', iterations=1)

        bpy.ops.object.select_all(action='DESELECT')
        bpy.data.objects['cm'].select_set(True)
        context.view_layer.objects.active = bpy.data.objects['cm']


class SplintMandOrigiMaxilaFinal(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.splint_mand_origi_maxila_final"
    bl_label = "Splint Mandible Origin Maxilla Final"
    bl_options = {'REGISTER', 'UNDO'}

    @classmethod
    def poll(cls, context):

        found = 'Condyle Rotation Point' in bpy.data.objects

        if found == False:
            return False
        else:
            if found == True:
                return True

    def execute(self, context):
        SplintMandOrigiMaxilaFinalDef()
        return {'FINISHED'}

bpy.utils.register_class(SplintMandOrigiMaxilaFinal)
