import os
import c4d
import math

# Be sure to use a unique ID obtained from www.plugincafe.com
PLUGIN_ID = 123456790

#----begin_resource_section----
from bootstrap4c4d import Description, Assignment, Group, Container

crumb_percent_slider = [
    Assignment("STEP", 1.0),
    Assignment("UNIT", "PERCENT"),
    Assignment("CUSTOMGUI", "REALSLIDER"),
    Assignment("MINSLIDER", 0.0),
    Assignment("MAXSLIDER", 100.0)
]

crumb_percent_slider_limit_min = [
    Assignment("MIN", 0.0)
]

crumb_percent_slider_limit_max = [
    Assignment("MAX", 100.0)
]

crumb_flag_group_open = Assignment("DEFAULT", 1)

settings_effect_strength = Description({
    "id": "SETTINGS_EFFECT_STRENGTH",
    "key": "REAL",
    "value": [
        *crumb_percent_slider,
        *crumb_percent_slider_limit_min,
        *crumb_percent_slider_limit_max
    ],
    "locales": {
        "strings_us": "Strength"
    }
})

settings_base_origin_object = Description({
    "id": "SETTINGS_BASE_ORIGIN_OBJECT",
    "key": "LINK",
    "value": [
        Assignment("ANIM", "OFF"),
        Description({
            "key": "ACCEPT", 
            "value": [
                Assignment("Obase", None)
            ]
        })
    ],
    "locales": {
        "strings_us": "Origin"
    }
})

settings_base_start_time = Description({
    "id": "SETTINGS_BASE_START_TIME",
    "key": "REAL",
    "value": [
        Assignment("UNIT", "TIME")
    ],
    "locales": {
        "strings_us": "Start Time"
    }
})

settings_base_target_offset = Description({
    "id": "SETTINGS_BASE_TARGET_OFFSET",
    "key": "VECTOR",
    "value": [
        Assignment("UNIT", "METER")
    ],
    "locales": {
        "strings_us": "Target Offset"
    }
})

settings_base_draw_debug_lines = Description({
    "id": "SETTINGS_BASE_DRAW_DEBUG_LINES",
    "key": "BOOL",
    "value": [
        Assignment("ANIM", "OFF")
    ],
    "locales": {
        "strings_us": "Draw Debug Lines"
    }
})

vector_xplus = Assignment(None, None, {
    "id": "VECTOR_XPLUS",
    "locales": {
        "strings_us": "X+"
    }
})
vector_xminus = Assignment(None, None, {
    "id": "VECTOR_XMINUS",
    "locales": {
        "strings_us": "X-"
    }
})
vector_yplus = Assignment(None, None, {
    "id": "VECTOR_YPLUS",
    "locales": {
        "strings_us": "Y+"
    }
})
vector_yminus = Assignment(None, None, {
    "id": "VECTOR_YMINUS",
    "locales": {
        "strings_us": "Y-"
    }
})
vector_zplus = Assignment(None, None, {
    "id": "VECTOR_ZPLUS",
    "locales": {
        "strings_us": "Z+"
    }
})
vector_zminus = Assignment(None, None, {
    "id": "VECTOR_ZMINUS",
    "locales": {
        "strings_us": "Z-"
    }
})

settings_base_up_vector = Description({
    "id": "SETTINGS_BASE_UP_VECTOR",
    "key": "LONG",
    "value": [
        Assignment("ANIM", "OFF"),
        Assignment("CYCLE", [
            vector_xplus,
            vector_xminus, 
            vector_yplus,
            vector_yminus,
            vector_zplus,
            vector_zminus
        ])
    ],
    "locales": {
        "strings_us": "Up Vector"
    }
})

settings_base_aim_vector = Description({
    "id": "SETTINGS_BASE_AIM_VECTOR",
    "key": "LONG",
    "value": [
        Assignment("ANIM", "OFF"),
        Assignment("CYCLE", [
            vector_xplus,
            vector_xminus, 
            vector_yplus,
            vector_yminus,
            vector_zplus,
            vector_zminus
        ])
    ],
    "locales": {
        "strings_us": "Aim Vector"
    }
})

group_effect = Group("GROUP_EFFECT", {
    "value": [
        crumb_flag_group_open,
        settings_effect_strength
    ],
    "locales": {
        "strings_us": "Effect"
    }
})

group_base = Group("GROUP_BASE", {
    "value": [
        crumb_flag_group_open,
        settings_base_origin_object,
        settings_base_target_offset,
        settings_base_draw_debug_lines,
        settings_base_start_time,
        settings_base_up_vector,
        settings_base_aim_vector
    ],
    "locales": {
        "strings_us": "Base"
    },
})

# squash and stretch
settings_squash_stretch_enable = Description({
    "id": "SETTINGS_SQUASH_STRETCH_ENABLE",
    "key": "BOOL",
    "value": [
        Assignment("ANIM", "OFF")
    ],
    "locales": {
        "strings_us": "Enable"
    }
})

settings_squash_stretch_stretch_strength = Description({
    "id": "SETTINGS_SQUASH_STRETCH_STRETCH_STRENGTH",
    "key": "REAL",
    "value": [
        *crumb_percent_slider,
        *crumb_percent_slider_limit_min
    ],
    "locales": {
        "strings_us": "Stretch Strength"
    }
})

settings_squash_stretch_squash_strength = Description({
    "id": "SETTINGS_SQUASH_STRETCH_SQUASH_STRENGTH",
    "key": "REAL",
    "value": [
        *crumb_percent_slider,
        *crumb_percent_slider_limit_min
    ],
    "locales": {
        "strings_us": "Squash Strength"
    }
})

group_squash_stretch = Group("GROUP_SQUASH_STRETCH", {
    "value": [
        crumb_flag_group_open,
        settings_squash_stretch_enable,
        settings_squash_stretch_stretch_strength,
        settings_squash_stretch_squash_strength
    ],
    "locales": {
        "strings_us": "Squash and Stretch"
    }
})

# physics descriptions
settings_physics_stiffness = Description({
    "id": "SETTINGS_PHYSICS_STIFFNESS",
    "key": "REAL",
    "value": crumb_percent_slider,
    "locales": {
        "strings_us": "Stiffness"
    }
})

settings_physics_mass = Description({
    "id": "SETTINGS_PHYSICS_MASS",
    "key": "REAL",
    "value": crumb_percent_slider,
    "locales": {
        "strings_us": "Mass"
    }
})

settings_physics_damping = Description({
    "id": "SETTINGS_PHYSICS_DAMPING",
    "key": "REAL",
    "value": crumb_percent_slider,
    "locales": {
        "strings_us": "Damping"
    }
})

settings_physics_gravity = Description({
    "id": "SETTINGS_PHYSICS_GRAVITY",
    "key": "VECTOR",
    "value": [
        Assignment("UNIT", "METER")
    ],
    "locales": {
        "strings_us": "Gravity"
    }
})

group_physics = Group("GROUP_PHYSICS", {
    "value": [
        crumb_flag_group_open,
        settings_physics_stiffness,
        settings_physics_mass,
        settings_physics_damping,
        settings_physics_gravity
    ],
    "locales": {
        "strings_us": "Base"
    },
})

root = Container("Tjiggle", {
    "value": [
        Assignment("NAME", "Tjiggle"),
        Assignment("INCLUDE", "Tbase"),
        Assignment("INCLUDE", "Texpression"),
        Group("GROUP_SETTINGS", {
            "value": [
                crumb_flag_group_open,
                group_effect,
                group_base,
                group_squash_stretch,
                group_physics
            ],
            "locales": {
                "strings_us": "Settings"
            }
        })
    ],
    "locales": {
        "strings_us": "Jiggle"
    }
})

#----end_resource_section----

#----begin_id_section----
VECTOR_XPLUS = vector_xplus.GetId()
VECTOR_XMINUS = vector_xminus.GetId() 
VECTOR_YPLUS = vector_yplus.GetId()
VECTOR_YMINUS = vector_yminus.GetId()
VECTOR_ZPLUS = vector_zplus.GetId()
VECTOR_ZMINUS = vector_zminus.GetId()

# effect ids
SETTINGS_EFFECT_STRENGTH = settings_effect_strength.GetId()

# base ids
SETTINGS_BASE_ORIGIN_OBJECT = settings_base_origin_object.GetId()
SETTINGS_BASE_START_TIME = settings_base_start_time.GetId()
SETTINGS_BASE_TARGET_OFFSET = settings_base_target_offset.GetId()
SETTINGS_BASE_UP_VECTOR = settings_base_up_vector.GetId()
SETTINGS_BASE_AIM_VECTOR = settings_base_aim_vector.GetId()
SETTINGS_BASE_DRAW_DEBUG_LINES = settings_base_draw_debug_lines.GetId()

# squash stretch ids
SETTINGS_SQUASH_STRETCH_ENABLE = settings_squash_stretch_enable.GetId()
SETTINGS_SQUASH_STRETCH_STRETCH_STRENGTH = settings_squash_stretch_stretch_strength.GetId()
SETTINGS_SQUASH_STRETCH_SQUASH_STRENGTH = settings_squash_stretch_squash_strength.GetId()

# physics ids
SETTINGS_PHYSICS_STIFFNESS = settings_physics_stiffness.GetId()
SETTINGS_PHYSICS_MASS = settings_physics_mass.GetId()
SETTINGS_PHYSICS_DAMPING = settings_physics_damping.GetId()
SETTINGS_PHYSICS_GRAVITY = settings_physics_gravity.GetId()
#----end_id_section----

class DataContainer(object):
    
    def __init__(self, data):
        self.data = data

    @property
    def strength(self):
        return self.data[SETTINGS_EFFECT_STRENGTH]

    @strength.setter
    def strength(self, value):
        self.data[SETTINGS_EFFECT_STRENGTH] = value

    @property
    def originObject(self):
        return self.data[SETTINGS_BASE_ORIGIN_OBJECT]

    @property
    def targetOffset(self):
        return self.data[SETTINGS_BASE_TARGET_OFFSET]

    @targetOffset.setter
    def targetOffset(self, value):
        self.data[SETTINGS_BASE_TARGET_OFFSET] = value

    @property
    def drawDebugLines(self):
        return self.data[SETTINGS_BASE_DRAW_DEBUG_LINES]

    # time

    @property
    def startTime(self):
        return self.data[SETTINGS_BASE_START_TIME]

    @startTime.setter
    def startTime(self, value):
        self.data[SETTINGS_BASE_START_TIME] = value

    # up vector
    @property
    def upVector(self):
        return self.data[SETTINGS_BASE_UP_VECTOR]

    @upVector.setter
    def upVector(self, value):
        self.data[SETTINGS_BASE_UP_VECTOR] = value

    # aim vector
    @property
    def aimVector(self):
        return self.data[SETTINGS_BASE_AIM_VECTOR]

    @aimVector.setter
    def aimVector(self, value):
        self.data[SETTINGS_BASE_AIM_VECTOR] = value

    # squash stretch
    @property
    def squashStretchEnable(self):
        return self.data[SETTINGS_SQUASH_STRETCH_ENABLE]

    @property
    def squashStretchStretchStrength(self):
        return self.data[SETTINGS_SQUASH_STRETCH_STRETCH_STRENGTH]

    @squashStretchStretchStrength.setter
    def squashStretchStretchStrength(self, value):
        self.data[SETTINGS_SQUASH_STRETCH_STRETCH_STRENGTH] = value

    @property
    def squashStretchSquashStrength(self):
        return self.data[SETTINGS_SQUASH_STRETCH_SQUASH_STRENGTH]

    @squashStretchSquashStrength.setter
    def squashStretchSquashStrength(self, value):
        self.data[SETTINGS_SQUASH_STRETCH_SQUASH_STRENGTH] = value

    # physics

    @property
    def stiffness(self):
        return self.data[SETTINGS_PHYSICS_STIFFNESS]

    @stiffness.setter
    def stiffness(self, value):
        self.data[SETTINGS_PHYSICS_STIFFNESS] = value

    @property
    def mass(self):
        return self.data[SETTINGS_PHYSICS_MASS]

    @mass.setter
    def mass(self, value):
        self.data[SETTINGS_PHYSICS_MASS] = value

    @property
    def damping(self):
        return self.data[SETTINGS_PHYSICS_DAMPING]

    @damping.setter
    def damping(self, value):
        self.data[SETTINGS_PHYSICS_DAMPING] = value

    @property
    def gravity(self):
        return self.data[SETTINGS_PHYSICS_GRAVITY]

    @gravity.setter
    def gravity(self, value):
        self.data[SETTINGS_PHYSICS_GRAVITY] = value

class Jiggle(c4d.plugins.TagData):
    """Jiggle"""
    
    def Init(self, node):
        """
        Called when Cinema 4D Initialize the TagData (used to define, default values)
        :param node: The instance of the TagData.
        :type node: c4d.GeListNode
        :return: True on success, otherwise False.
        """

        # data = node.GetDataInstance()
        data = DataContainer(node.GetDataInstance())

        data.strength = 1.0
        data.resultRotation = c4d.Vector(0, 0, 0)

        # time related
        self.previousFrame = 0
        data.targetOffset = c4d.Vector(0, 0, 100)
        data.startTime = 0.0

        # up vector
        data.upVector = VECTOR_YPLUS

        # aim vector
        data.aimVector = VECTOR_ZPLUS

        # squash stretch
        data.squashStretchStretchStrength = 0.0
        data.squashStretchSquashStrength = 0.0

        # physics related
        data.stiffness = 0.1
        data.mass = 0.9
        data.damping = 0.75
        data.gravity = c4d.Vector(0, -981.0, 0)

        self.Reset(node)

        c4d.EventAdd()

        return True

    @classmethod
    def GetFrame(cls, time, fps):
        return time.GetFrame(fps)

    @classmethod
    def CalculateTargetPosition(cls, origin, offset):
        if origin:
            return offset * origin.GetMg()

        return offset

    def GetHandleCount(self, op):
        """
        :param op: The host object of the tag.
        :type op: c4d.BaseObject
        :return:
        """

        return 1

    def GetHandle(self, op, i, info):
        """
        :param op: The host object of the tag.
        :type op: c4d.BaseObject
        :param i: Index of handle
        :type i: int
        :param info: Info of handle
        :type info: c4d.HandleInfo
        :return:
        """
        data = DataContainer(op.GetDataInstance())

        info.position = Jiggle.CalculateTargetPosition(data.originObject, data.targetOffset)
        info.type = c4d.HANDLECONSTRAINTTYPE_FREE

    def SetHandle(self, op, i, p, info):
        """
        :param op: The host object of the tag.
        :type op: c4d.BaseObject
        :param i: Index of handle
        :type i: int
        :param p: Handle Position
        :type p: c4d.Vector
        :param info: Info of handle
        :type info: c4d.HandleInfo
        :return:
        """
        data = DataContainer(op.GetDataInstance())

        data.targetOffset = p * ~data.originObject.GetMg()

    
    def Execute(self, tag, doc, op, bt, priority, flags):
        """
        Called by Cinema 4D at each Scene Execution, this is the place where calculation should take place.
        :param tag: The instance of the TagData.
        :type tag: c4d.BaseTag
        :param doc: The host document of the tag's object.
        :type doc: c4d.documents.BaseDocument
        :param op: The host object of the tag.
        :type op: c4d.BaseObject
        :param bt: The Thread that execute the this TagData.
        :type bt: c4d.threading.BaseThread
        :param priority: Information about the execution priority of this TagData.
        :type priority: EXECUTIONPRIORITY
        :param flags: Information about when this TagData is executed.
        :type flags: EXECUTIONFLAGS
        :return:
        """
        data = DataContainer(tag.GetDataInstance())
        fps = doc.GetFps()
        currentFrame = float(Jiggle.GetFrame(doc.GetTime(), fps))
        originMatrix = data.originObject.GetMg()
        originPosition = originMatrix.off
        projectedPosition = Jiggle.CalculateTargetPosition(data.originObject, data.targetOffset)

        if currentFrame > data.startTime:
            # only update if current frame is an increment by 1 of previous frame
            if currentFrame == self.previousFrame + 1.0:
                self.Update(tag, doc, op)
        else:
            self.Reset(tag)

        # blend position by strength
        targetPosition = c4d.utils.MixVec(projectedPosition, self.position, data.strength)

        # calculate matrix
        # calculate aim vector
        aim = c4d.Vector(targetPosition - originPosition).GetNormalized()

        # change up vector position
        if data.upVector == VECTOR_XPLUS:
            up = originMatrix.MulV(c4d.Vector(1.0, 0, 0))
        elif data.upVector == VECTOR_XMINUS:
            up = originMatrix.MulV(c4d.Vector(-1.0, 0, 0))
        elif data.upVector == VECTOR_YPLUS:
            up = originMatrix.MulV(c4d.Vector(0, 1.0, 0))
        elif data.upVector == VECTOR_YMINUS:
            up = originMatrix.MulV(c4d.Vector(0, -1.0, 0))
        elif data.upVector == VECTOR_ZPLUS:
            up = originMatrix.MulV(c4d.Vector(0, 0, 1.0))
        elif data.upVector == VECTOR_ZMINUS:
            up = originMatrix.MulV(c4d.Vector(0, 0, -1.0))

        side = up.Cross(aim).GetNormalized()
        # up = side.Cross(aim).GetNormalized()

        # calculate squash strech
        if data.squashStretchEnable:
            distance = c4d.Vector(targetPosition - originPosition).GetLength()

            maxDistance = data.targetOffset.GetLength()

            relativeDistance = distance - maxDistance

            try:
                squashStretchBias = abs(relativeDistance) / maxDistance
            except ZeroDivisionError:
                squashStretchBias = 0.0

            if relativeDistance > 0.0:
                squashStretchBias = squashStretchBias * data.squashStretchStretchStrength

                # stretch
                aim = aim * (1.0 + squashStretchBias)
                up = up * (1.0 - squashStretchBias)
                side = side * (1.0 - squashStretchBias)
            else:
                squashStretchBias = squashStretchBias * data.squashStretchSquashStrength

                # squash
                aim = aim * (1.0 - squashStretchBias)
                up = up * (1.0 + squashStretchBias)
                side = side * (1.0 + squashStretchBias)

        # change input order based on aim axis
        if data.aimVector == VECTOR_XPLUS:
            jiggleMatrix = c4d.Matrix(
                originPosition,
                aim,
                up,
                side
            )
        elif data.aimVector == VECTOR_XMINUS:
            jiggleMatrix = c4d.Matrix(
                originPosition,
                -aim,
                up,
                side
            )
        elif data.aimVector == VECTOR_YPLUS:
            jiggleMatrix = c4d.Matrix(
                originPosition,
                side,
                aim,
                up
            )
        elif data.aimVector == VECTOR_YMINUS:
            jiggleMatrix = c4d.Matrix(
                originPosition,
                side,
                -aim,
                up
            )
        elif data.aimVector == VECTOR_ZPLUS:
            jiggleMatrix = c4d.Matrix(
                originPosition,
                side,
                up,
                aim
            )
        elif data.aimVector == VECTOR_ZMINUS:
            jiggleMatrix = c4d.Matrix(
                originPosition,
                side,
                up,
                -aim
            )

        op.SetMg(jiggleMatrix)

        # finish execute
        self.previousFrame = currentFrame
        
        return c4d.EXECUTIONRESULT_OK

    def Draw(self, tag, op, bd, bh):
        data = DataContainer(tag.GetDataInstance())
        drawpass = bd.GetDrawPass()

        if not data.drawDebugLines:
            return True

        # draw target line
        targetPosition = Jiggle.CalculateTargetPosition(data.originObject, data.targetOffset)

        bd.SetPen(c4d.GetViewColor(c4d.VIEWCOLOR_XAXIS))
        bd.DrawLine(
            data.originObject.GetMg().off,
            targetPosition,
            0
        )

        # draw connection
        bd.SetPen(c4d.GetViewColor(c4d.VIEWCOLOR_YAXIS))
        bd.DrawLine(
            targetPosition,
            self.position,
            0
        )
        
        # draw current target
        bd.SetPen(c4d.GetViewColor(c4d.VIEWCOLOR_ZAXIS))
        bd.DrawLine(data.originObject.GetMg().off, self.position, 0)

        # bd.SetMatrix_Screen()
        # circlePosition = bd.WS(targetPosition)
        # bd.DrawCircle2D(circlePosition.x, circlePosition.y, 5.0)

        if drawpass == c4d.DRAWPASS_HANDLES:
            bd.SetMatrix_Screen()
            handleScreenSpace = bd.WS(Jiggle.CalculateTargetPosition(data.originObject, data.targetOffset))
            bd.SetPen(c4d.GetViewColor(c4d.VIEWCOLOR_OBJECTHIGHLIGHT))
            bd.DrawCircle2D(handleScreenSpace.x, handleScreenSpace.y, 8)

            plugins.TagData.Draw(self, tag, op, bd, bh)

        return True

    def Reset(self, tag):
        """
        Update loop.
        :param tag: The instance of the TagData.
        :type tag: c4d.BaseTag
        :return:
        """
        # print("Reset")

        data = DataContainer(tag.GetDataInstance())

        self.force = c4d.Vector(0, 0, 0)
        self.acceleration = c4d.Vector(0, 0, 0)
        self.velocity = c4d.Vector(0, 0, 0)
        self.position = Jiggle.CalculateTargetPosition(data.originObject, data.targetOffset)

    def Update(self, tag, doc, op):
        """
        Update loop.
        :param tag: The instance of the TagData.
        :type tag: c4d.BaseTag
        :param doc: The host document of the tag's object.
        :type doc: c4d.documents.BaseDocument
        :param op: The host object of the tag.
        :type op: c4d.BaseObject
        :return:
        """
        # print("Update")

        data = DataContainer(tag.GetDataInstance())

        targetPosition = Jiggle.CalculateTargetPosition(data.originObject, data.targetOffset)

        direction = targetPosition - self.position
        #direction = c4d.Vector(0, 0, 0)

        # calculate spring
        self.force = (direction * data.stiffness) + (data.gravity / 10.0 / float(doc.GetFps()))
        self.acceleration = self.force / data.mass
        self.velocity = self.velocity + (self.acceleration * (1.0 - data.damping))

        self.position = self.position + self.velocity + self.force


if __name__ == "__main__":
    # Retrieves the icon path
    directory, _ = os.path.split(__file__)
    fn = os.path.join(directory, "res", "tjiggle.png")

    # Creates a BaseBitmap
    bmp = c4d.bitmaps.BaseBitmap()
    if bmp is None:
        raise MemoryError("Failed to create a BaseBitmap.")

    # Init the BaseBitmap with the icon
    if bmp.InitWith(fn)[0] != c4d.IMAGERESULT_OK:
        raise MemoryError("Failed to initialize the BaseBitmap.")

    c4d.plugins.RegisterTagPlugin(id=PLUGIN_ID,
        str="Jiggle",
        info=c4d.TAG_EXPRESSION | c4d.TAG_VISIBLE | c4d.TAG_IMPLEMENTS_DRAW_FUNCTION,
        g=Jiggle,
        description="Tjiggle",
        icon=bmp
    )