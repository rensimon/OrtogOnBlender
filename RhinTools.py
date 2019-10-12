import bpy
from .PontosAnatomicos import *
from .FerrMedidas import *
from math import sqrt

import bmesh
from mathutils import Matrix, Vector
from time import gmtime, strftime

# PONTOS ANATOMICOS

class Medial_Canthus_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.medial_canthus_right_pt"
    bl_label = "Medial Canthus right"

    @classmethod
    def poll(cls, context):

        found = 'Medial Canthus right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Medial Canthus right', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Medial_Canthus_right_pt)

class Medial_Canthus_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.medial_canthus_left_pt"
    bl_label = "Medial Canthus left"

    @classmethod
    def poll(cls, context):

        found = 'Medial Canthus left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Medial Canthus left', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Medial_Canthus_left_pt)

class Radix_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.radix_pt"
    bl_label = "Radix"

    @classmethod
    def poll(cls, context):

        found = 'Radix' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Radix', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Radix_pt)

class Anterior_Nostril_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.anterior_nostril_left_pt"
    bl_label = "Anterior Nostril left"

    @classmethod
    def poll(cls, context):

        found = 'Anterior Nostril left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Anterior Nostril left', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Anterior_Nostril_left_pt)


class Anterior_Nostril_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.anterior_nostril_right_pt"
    bl_label = "Anterior Nostril right"

    @classmethod
    def poll(cls, context):

        found = 'Anterior Nostril right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Anterior Nostril right', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Anterior_Nostril_right_pt)


class Posterior_Nostril_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.posterior_nostril_left_pt"
    bl_label = "Posterior Nostril left"

    @classmethod
    def poll(cls, context):

        found = 'Posterior Nostril left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Posterior Nostril left', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Posterior_Nostril_left_pt)


class Posterior_Nostril_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.posterior_nostril_right_pt"
    bl_label = "Posterior Nostril right"

    @classmethod
    def poll(cls, context):

        found = 'Posterior Nostril right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Posterior Nostril right', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Posterior_Nostril_right_pt)

class Rhinion_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.rhinion_pt"
    bl_label = "Rhinion"

    @classmethod
    def poll(cls, context):

        found = 'Rhinion' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Rhinion', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Rhinion_pt)

class Alar_Groove_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.alar_groove_right_pt"
    bl_label = "Alar Groove right"

    @classmethod
    def poll(cls, context):

        found = 'Alar Groove right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Alar Groove right', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Alar_Groove_right_pt)

class Alar_Groove_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.alar_groove_left_pt"
    bl_label = "Alar Groove left"

    @classmethod
    def poll(cls, context):

        found = 'Alar Groove left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Alar Groove left', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Alar_Groove_left_pt)

class Supratip_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.supratip_pt"
    bl_label = "Supratip"

    @classmethod
    def poll(cls, context):

        found = 'Supratip' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Supratip', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Supratip_pt)

class Infratip_Lobule_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.infratip_lobule_pt"
    bl_label = "Infratip Lobule"

    @classmethod
    def poll(cls, context):

        found = 'Infratip Lobule' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Infratip Lobule', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Infratip_Lobule_pt)

class Alar_Rim_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.alar_rim_right_pt"
    bl_label = "Alar Rim right"

    @classmethod
    def poll(cls, context):

        found = 'Alar Rim right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Alar Rim right', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Alar_Rim_right_pt)

class Alar_Rim_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.alar_rim_left_pt"
    bl_label = "Alar Rim left"

    @classmethod
    def poll(cls, context):

        found = 'Alar Rim left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Alar Rim left', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Alar_Rim_left_pt)

class Columella_right_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.columella_right_pt"
    bl_label = "Columella right"

    @classmethod
    def poll(cls, context):

        found = 'Columella right' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Columella right', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Columella_right_pt)

class Columella_left_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.columella_left_pt"
    bl_label = "Columella left"

    @classmethod
    def poll(cls, context):

        found = 'Columella left' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CriaPontoDef('Columella left', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Columella_left_pt)


class Trichion_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.trichion_pt"
    bl_label = "Trichion"

    @classmethod
    def poll(cls, context):

        found = 'Trichion' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Trichion', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Trichion_pt)


class Submental_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.submental_pt"
    bl_label = "Submental"

    @classmethod
    def poll(cls, context):

        found = 'Submental' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Submental', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Submental_pt)


class Supraglabella_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.supraglabella_pt"
    bl_label = "Supraglabella"

    @classmethod
    def poll(cls, context):

        found = 'Supraglabella' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Supraglabella', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Supraglabella_pt)

class Glabella_pt(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.glabella_pt"
    bl_label = "Glabella"

    @classmethod
    def poll(cls, context):

        found = 'Glabella' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False

    def execute(self, context):
        CriaPontoDef('Glabella', 'Anatomical Points - Soft Tissue')
        TestaPontoCollDef()
        return {'FINISHED'}

bpy.utils.register_class(Glabella_pt)

# COPIA FACE

def CopiaFaceDef():
    bpy.context.object.name = "SoftTissueDynamic"
    bpy.ops.object.duplicate()
    bpy.context.object.name = "SoftTissueDynamic_COPY"

    FaceCopiada = bpy.data.objects['SoftTissueDynamic_COPY']
    FaceCopiada.hide_viewport=True

    FaceOriginal = bpy.data.objects['SoftTissueDynamic']
    FaceOriginal.select_set(True)
    bpy.context.view_layer.objects.active = FaceOriginal

class CopiaFace(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.copia_face"
    bl_label = "Copy Face"

    @classmethod
    def poll(cls, context):

        found = 'SoftTissueDynamic_COPY' in bpy.data.objects

        if found == False:
            return True
        else:
            if found == True:
                return False


    def execute(self, context):
        CopiaFaceDef()
        return {'FINISHED'}

bpy.utils.register_class(CopiaFace)


def CalculaDistsNarizDef():

    try:
        bpy.ops.object.mode_set(mode = 'OBJECT')
    except:
        print("Já em modo objeto.")

    try:
        ListaPontos = ['Tip of Nose', 'Subnasale','Radix', 'Anterior Nostril left', 'Posterior Nostril left', 'Anterior Nostril right', 'Posterior Nostril right','Rhinion', 'Alar Groove right', 'Alar Groove left', 'Supratip', 'Infratip Lobule', 'Alar Rim right', 'Alar Rim left', 'Columella right', 'Columella left']

        for i in ListaPontos:
    #            print("HÁ O NOME!", i.name)
            bpy.ops.object.select_all(action='DESELECT')

            ObjetoAtual = bpy.data.objects[i]
            ObjetoAtual.select_set(True)
            bpy.context.view_layer.objects.active = ObjetoAtual
            bpy.ops.object.duplicate()
            NovoNome = str(bpy.data.objects[i].name)+"_COPY_MEDIDAS"
            bpy.context.object.name = NovoNome
            bpy.ops.object.parent_clear(type='CLEAR_KEEP_TRANSFORM')
            bpy.ops.object.select_all(action='DESELECT')
    except:
        print("Erro ao tentar copiar os objetos.")

    try:

        print("TESTEEEEEEEEEEEE")
        print(bpy.data.objects["Radix_COPY_MEDIDAS"].name)
#        print(bpy.data.objects["Tip of Nose_COPY_MEDIDAS"].name)
        print(bpy.data.objects["Subnasale_COPY_MEDIDAS"].name)
        DistRadixTip = DistanciaObjetos("Radix_COPY_MEDIDAS", "Tip of Nose_COPY_MEDIDAS")
        DistTipSub = DistanciaObjetos("Radix_COPY_MEDIDAS", "Subnasale_COPY_MEDIDAS")
        print("DistRadixTip:", DistRadixTip)
        print("DistTipSub:", DistTipSub)

        ProporcaoNariz = DistRadixTip / DistTipSub
        print("ProporcaoNariz", ProporcaoNariz)

        bpy.types.Scene.rhin_prop_nariz = bpy.props.StringProperty \
            (
                name = "Nose Proportion",
                description = "Nose Proportion",
                default = str(round(ProporcaoNariz, 2))
            )
    except:
        print("Problemas ao calcular a proporção do nariz.")

    try:

        # CRIA PONTOS PARA CALCULAR ANGULO ESQUERDO
        bpy.ops.object.select_all(action='DESELECT')

        ObjetoAtual = bpy.data.objects["Posterior Nostril left_COPY_MEDIDAS"]
        ObjetoAtual.select_set(True)
        bpy.context.view_layer.objects.active = ObjetoAtual
        bpy.ops.object.duplicate()
        NovoNome = "Posterior Nostril left_ABAIXO"
        bpy.context.object.name = NovoNome
        bpy.ops.transform.translate(value=(0, 0, -80))
        bpy.ops.object.select_all(action='DESELECT')

        # CALCULA ANGULO
        AnguloNasolabial = CalculaAngulo("Anterior Nostril left_COPY_MEDIDAS", "Posterior Nostril left_COPY_MEDIDAS", "Posterior Nostril left_ABAIXO")

#        AnguloNasolabial = CalculaAngulo("Radix_COPY_MEDIDAS", "Tip of Nose_COPY_MEDIDAS", "Subnasale_COPY_MEDIDAS")

        bpy.types.Scene.rhin_angulo_nasolabial_esquerdo = bpy.props.StringProperty \
            (
                name = "Nasolabial Angle left",
                description = "Nasolabial Angle left",
                default = str(AnguloNasolabial) #+"º"
            )

        # Apaga objeto criados

        bpy.ops.object.select_all(action='DESELECT')
        ObjetoAtual = bpy.data.objects["Posterior Nostril left_ABAIXO"]
        ObjetoAtual.select_set(True)
        bpy.context.view_layer.objects.active = ObjetoAtual
        bpy.ops.object.delete(use_global=False)

    except:
        print("Não foi possível fazer o cálculo do ângulo nasolabial ESQUERDO.")


    try:

        # CRIA PONTOS PARA CALCULAR ANGULO DIREITO
        bpy.ops.object.select_all(action='DESELECT')

        ObjetoAtual = bpy.data.objects["Posterior Nostril right_COPY_MEDIDAS"]
        ObjetoAtual.select_set(True)
        bpy.context.view_layer.objects.active = ObjetoAtual
        bpy.ops.object.duplicate()
        NovoNome = "Posterior Nostril right_ABAIXO"
        bpy.context.object.name = NovoNome
        bpy.ops.transform.translate(value=(0, 0, -80))
        bpy.ops.object.select_all(action='DESELECT')

        # CALCULA ANGULO
        AnguloNasolabial = CalculaAngulo("Anterior Nostril right_COPY_MEDIDAS", "Posterior Nostril right_COPY_MEDIDAS", "Posterior Nostril right_ABAIXO")

#        AnguloNasolabial = CalculaAngulo("Radix_COPY_MEDIDAS", "Tip of Nose_COPY_MEDIDAS", "Subnasale_COPY_MEDIDAS")

        bpy.types.Scene.rhin_angulo_nasolabial_direito = bpy.props.StringProperty \
            (
                name = "Nasolabial Angle right",
                description = "Nasolabial Angle right",
                default = str(AnguloNasolabial) #+"º"
            )

        # Apaga objeto criados

        bpy.ops.object.select_all(action='DESELECT')
        ObjetoAtual = bpy.data.objects["Posterior Nostril right_ABAIXO"]
        ObjetoAtual.select_set(True)
        bpy.context.view_layer.objects.active = ObjetoAtual
        bpy.ops.object.delete(use_global=False)

    except:
        print("Não foi possível fazer o cálculo do ângulo nasolabial DIREITO.")


    try:

        # CALCULA ALAR RIM - COLUMELLA FACTOR - ESQUERDA
        AnteriorNostrilLeft = bpy.data.objects["Anterior Nostril left_COPY_MEDIDAS"].location[2]
        PosteriorNostrilLeft = bpy.data.objects["Posterior Nostril left_COPY_MEDIDAS"].location[2]

        NonstrilLeftMedia = (AnteriorNostrilLeft + PosteriorNostrilLeft) / 2

        AlarRimLeft = bpy.data.objects["Alar Rim left_COPY_MEDIDAS"].location[2]
        FatorAlarRimLeft = abs(AlarRimLeft - NonstrilLeftMedia)


        bpy.types.Scene.rhin_alar_rim_med_esquerdo = bpy.props.StringProperty \
            (
                name = "Alar Rim - Nonstrill",
                description = "Alar Rim - Nonstrill",
                default = str(round(FatorAlarRimLeft, 2))
            )


        ColumellaLeft = bpy.data.objects["Columella left_COPY_MEDIDAS"].location[2]
        FatorColumellaLeft = abs(ColumellaLeft - NonstrilLeftMedia)
        print("FatoColumellaLeft:", FatorColumellaLeft)

        bpy.types.Scene.rhin_columella_med_esquerdo = bpy.props.StringProperty \
            (
                name = "Columella - Nonstrill",
                description = "Columella - Nonstrill",
                default = str(round(FatorColumellaLeft, 2))
            )

    except:
        print("Não foi possível fazer o cálculo do fator Alar Rim-Columella - ESQUERDO.")

    try:

        # CALCULA ALAR RIM - COLUMELLA FACTOR - DIREITA
        AnteriorNostrilRight = bpy.data.objects["Anterior Nostril right_COPY_MEDIDAS"].location[2]
        PosteriorNostrilRight = bpy.data.objects["Posterior Nostril right_COPY_MEDIDAS"].location[2]

        NonstrilRightMedia = (AnteriorNostrilRight + PosteriorNostrilRight) / 2

        AlarRimRight = bpy.data.objects["Alar Rim right_COPY_MEDIDAS"].location[2]
        FatorAlarRimRight = abs(AlarRimRight - NonstrilRightMedia)


        bpy.types.Scene.rhin_alar_rim_med_direito = bpy.props.StringProperty \
            (
                name = "Alar Rim - Nonstrill",
                description = "Alar Rim - Nonstrill",
                default = str(round(FatorAlarRimRight, 2))
            )


        ColumellaRight = bpy.data.objects["Columella right_COPY_MEDIDAS"].location[2]
        FatorColumellaRight = abs(ColumellaRight - NonstrilRightMedia)
        print("FatoColumellaRight:", FatorColumellaRight)

        bpy.types.Scene.rhin_columella_med_direito = bpy.props.StringProperty \
            (
                name = "Columella - Nonstrill",
                description = "Columella - Nonstrill",
                default = str(round(FatorColumellaRight, 2))
            )

    except:
        print("Não foi possível fazer o cálculo do fator Alar Rim-Columella - DIREITO.")

    # APAGA Pontos criados

    try:
        for i in ListaPontos:
    #            print("HÁ O NOME!", i.name)
            bpy.ops.object.select_all(action='DESELECT')
            NomeAtual = str(bpy.data.objects[i].name)+"_COPY_MEDIDAS"
            ObjetoAtual = bpy.data.objects[NomeAtual]
            ObjetoAtual.select_set(True)
            bpy.context.view_layer.objects.active = ObjetoAtual
            bpy.ops.object.delete(use_global=False)
            bpy.ops.object.select_all(action='DESELECT')

    except:
        print("Houve algum problema ao deletar os pontos.")


class CalculaDistsNariz(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.dist_nariz"
    bl_label = "Nose dists"

    def execute(self, context):


        try:
            OriginalBool = bpy.data.collections['Anatomical Points - Soft Tissue'].hide_viewport

            if bpy.data.collections['Anatomical Points - Soft Tissue'].hide_viewport == True:
                print("XXXXXXXXXX")
                bpy.data.collections['Anatomical Points - Soft Tissue'].hide_viewport = False
        except:
            print("A coleção Anatomical Points - Soft Tissue não existe!")


        CalculaDistsNarizDef()

        try:

            if OriginalBool == False:
                bpy.data.collections['Anatomical Points - Soft Tissue'].hide_viewport = False
            else:
                bpy.data.collections['Anatomical Points - Soft Tissue'].hide_viewport = True
        except:
            print("A coleção Anatomical Points - Soft Tissue não existe!")


        return {'FINISHED'}


bpy.utils.register_class(CalculaDistsNariz)



class MostraOcultaPontos(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.rhin_mostra_oculta_pontos"
    bl_label = "Nose dists"

    def execute(self, context):

        try:
            if bpy.data.collections['Anatomical Points - Soft Tissue'].hide_viewport == False:
                print("HIDE FALSE")
                bpy.data.collections['Anatomical Points - Soft Tissue'].hide_viewport = True
            else: #bpy.data.collections['Anatomical Points - Soft Tissue'].hide_viewport == True:
                print("HIDE TRUE")
                bpy.data.collections['Anatomical Points - Soft Tissue'].hide_viewport = False
#                bpy.data.collections['Anatomical Points - Soft Tissue'].hide_viewport = False
        except:
            print("A coleção Anatomical Points - Soft Tissue não existe!")

        return {'FINISHED'}

bpy.utils.register_class(MostraOcultaPontos)


def GeraGuiaNarizDef():

    Rosto = bpy.data.objects["SoftTissueDynamic"]

    Pontos = ['Supraglabella', 'Glabella', 'Radix', 'Rhinion', 'Supratip', 'Tip of Nose', 'Columella', 'Subnasale', 'Upper Lip']

    coords = []

    for i in Pontos:
        VetorAtual = bpy.data.objects[i].location
        VetX = bpy.data.objects[i].location[0]
        VetY = bpy.data.objects[i].location[1]
        VetZ = bpy.data.objects[i].location[2]
        coords.append((VetX, VetY, VetZ))

    curveData = bpy.data.curves.new('myCurve', type='CURVE')
    curveData.dimensions = '3D'
    #    curveData.resolution_u = 6
    curveData.resolution_u = 36

    # map coords to spline
    polyline = curveData.splines.new('BEZIER')
    polyline.bezier_points.add(len(coords)-1)
    #    for i, coord in enumerate(coords):
    #        x,y,z = coord
    #        polyline.points[i].co = (x, y, z, 1)

    from bpy_extras.io_utils import unpack_list
    polyline.bezier_points.foreach_set("co", unpack_list(coords))

    # Apaga pontos
    bpy.ops.object.select_all(action='DESELECT')

    #for i in Pontos:
    #    bpy.data.objects[i].select_set(True)

    #bpy.ops.object.delete(use_global=False)

    bpy.data.collections['Anatomical Points - Soft Tissue'].hide_viewport = True

    # Cria Linha
    curveOB = bpy.data.objects.new('myCurve', curveData)

    # attach to scene and validate context
    scn = bpy.context.scene
    #   scn.objects.link(curveOB)
    bpy.context.collection.objects.link(curveOB)
    #scn.collection.objects.link(curveOB) # Esta opção faz com que o objeto criado vá para a Scene Collection!
    bpy.ops.object.select_all(action='DESELECT')
    bpy.context.view_layer.objects.active = curveOB
    curveOB.select_set(True)

    bpy.ops.object.editmode_toggle()
    bpy.ops.curve.select_all(action='SELECT')
    bpy.ops.curve.handle_type_set(type='AUTOMATIC')

    #bpy.ops.curve.make_segment()

    bpy.ops.object.editmode_toggle()

    bpy.ops.object.modifier_add(type='SHRINKWRAP')
    bpy.context.object.modifiers["Shrinkwrap"].target = Rosto
    bpy.context.object.modifiers["Shrinkwrap"].offset = 0.01
    bpy.context.object.modifiers["Shrinkwrap"].wrap_mode = 'ABOVE_SURFACE'

    #bpy.context.space_data.context = 'MODIFIER'
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Shrinkwrap")
    #bpy.context.space_data.context = 'DATA'
    bpy.context.object.data.bevel_depth = 4

    bpy.ops.object.modifier_add(type='REMESH')
    bpy.context.object.modifiers["Remesh"].octree_depth = 6
    bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'

    GuiaBaseNome = str("GuiaBase-"+strftime("%Y%m%d%H%M%S", gmtime()))
    bpy.context.object.name = GuiaBaseNome

    bpy.ops.object.select_all(action='DESELECT')
    Rosto.select_set(True)
    bpy.context.view_layer.objects.active = Rosto

    bpy.ops.object.duplicate()

    bpy.ops.object.modifier_add(type='REMESH')
    bpy.context.object.modifiers["Remesh"].mode = 'SMOOTH'
    bpy.context.object.modifiers["Remesh"].octree_depth = 8
    bpy.context.object.modifiers["Remesh"].scale = 0.99
    bpy.ops.object.modifier_apply(apply_as='DATA', modifier="Remesh")

    NomeFaceNova = str("FaceDelete-"+strftime("%Y%m%d%H%M%S", gmtime()))
    # strftime("%Y-%m-%d %H:%M:%S", gmtime()))

    bpy.context.object.name = NomeFaceNova

    bpy.ops.object.select_all(action='DESELECT')
    bpy.data.objects[NomeFaceNova].select_set(True)
    bpy.data.objects[GuiaBaseNome].select_set(True)
    bpy.context.view_layer.objects.active = bpy.data.objects[NomeFaceNova]

    bpy.ops.object.booleana_osteo_geral()



class GeraGuiaNariz(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.gera_guia_nariz"
    bl_label = "Nose Guide Generator"

    def execute(self, context):
        GeraGuiaNarizDef()
        return {'FINISHED'}

bpy.utils.register_class(GeraGuiaNariz)


def EsculturaGrabDef():

    context = bpy.context
    scn = context.scene

    bpy.context.space_data.shading.type = 'MATERIAL'
    bpy.ops.object.mode_set(mode = 'SCULPT')
    bpy.ops.wm.tool_set_by_id(name="builtin_brush.Grab")
    bpy.context.scene.tool_settings.sculpt.use_symmetry_x = False


class EsculturaGrab(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.escultura_grab"
    bl_label = "Change to Grab"

    @classmethod
    def poll(cls, context):
        o = context.object
        if o is None:
            return False
        else:
            if o.type == "MESH":
                if bpy.context.mode == 'OBJECT' or bpy.context.mode == 'SCULPT':
                    return True
                else:
                    return False
            else:
                return False

    def execute(self, context):
        EsculturaGrabDef()
        return {'FINISHED'}

bpy.utils.register_class(EsculturaGrab)


def EsculturaSmoothDef():

    context = bpy.context
    scn = context.scene

    bpy.context.space_data.shading.type = 'MATERIAL'
    bpy.ops.object.mode_set(mode = 'SCULPT')
    bpy.ops.wm.tool_set_by_id(name="builtin_brush.Smooth")
    bpy.context.scene.tool_settings.sculpt.use_symmetry_x = False

class EsculturaSmooth(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.escultura_smooth"
    bl_label = "Change to Smooth"

    @classmethod
    def poll(cls, context):
        o = context.object
        if o is None:
            return False
        else:
            if o.type == "MESH":
                if bpy.context.mode == 'OBJECT' or bpy.context.mode == 'SCULPT':
                    return True
                else:
                    return False
            else:
                return False

    def execute(self, context):
        EsculturaSmoothDef()
        return {'FINISHED'}

bpy.utils.register_class(EsculturaSmooth)


def EsculturaMaskDef():

    context = bpy.context
    scn = context.scene

    bpy.context.space_data.shading.type = 'MATERIAL'
    bpy.ops.object.mode_set(mode = 'SCULPT')
    bpy.ops.wm.tool_set_by_id(name="builtin_brush.Mask")
    bpy.context.scene.tool_settings.sculpt.use_symmetry_x = False

class EsculturaMask(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.escultura_mask"
    bl_label = "Change to Mask"

    @classmethod
    def poll(cls, context):
        o = context.object
        if o is None:
            return False
        else:
            if o.type == "MESH":
                if bpy.context.mode == 'OBJECT' or bpy.context.mode == 'SCULPT':
                    return True
                else:
                    return False
            else:
                return False

    def execute(self, context):
        EsculturaMaskDef()
        return {'FINISHED'}

bpy.utils.register_class(EsculturaMask)
