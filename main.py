# File Name : main.py
# GridLayout tutorial

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.core.window import Window
from kivy.graphics import Rectangle, Color, Line, InstructionGroup

Window.size = (500, 500)

class LayoutsApp(App):
    
    def __init__(self, **kwargs):
        super(LayoutsApp, self).__init__(**kwargs)
        self.fX = 0
        self.fY = 0
        self.rX = 0
        self.rY = 0
        self.IG_Float    = InstructionGroup()
        self.IG_Relative = InstructionGroup()
        self.flout = FloatLayout()
        self.rlout = RelativeLayout()
        self.Main_Layout = GridLayout(rows = 2)
        self.abtn1 = Button()
        self.abtn1.bind(on_press = self.Press_A1)
        self.abtn2 = Button()
        self.abtn2.bind(on_press = self.Press_A2)
        self.Flag_F = False
        self.fbtn1 = Button()
        self.fbtn1.bind(on_press   = self.Press_F1)
        self.fbtn1.bind(on_release = self.Release_F1)
        self.Flag_R = False
        self.rbtn1 = Button()
        self.rbtn1.bind(on_press   = self.Press_R1)
        self.rbtn1.bind(on_release = self.Release_R1)
        self.gbtn1 = Button()
        self.gbtn3 = Button()
        self.sbtn1 = Button()
        self.sbtn2 = Button()
        
    
    def build(self):
        #############################################
        # Main Window is a GridLayout
        # that is sized to maximum Window Dimens.
        # and a colored rectangle is painted onto
        # the GridLayout starting at (0, 0)
        
        Width_Max = Window.width
        Height_Max = Window.height
        self.Main_Layout.height = Height_Max
        self.Main_Layout.width = Width_Max
        self.Main_Layout.x = 0
        self.Main_Layout.y = 0
        with self.Main_Layout.canvas.before:
            Color(rgba = (1.0, 0.6, 0.6, 1))
            Rectangle(size = (Width_Max, Height_Max), pos = (0, 0))
        ftmp = Width_Max / 3
        x = int(ftmp)
        Xo = 0
        X1 = Xo + x
        X2 = X1 + x
        X3 = X2 + x
        ftmp = Height_Max / 2
        y = int(ftmp)
        Yo = 0
        Y1 = Yo + y
        Y2 = Y1 + y
        Width1 = X1 - Xo
        Height1 = Y1 - Yo
        ########################
        self.fX = Xo
        self.fY = Y1
        self.rX = X1
        self.rY = Y1
        #############################################
        # Colored Dotted Lined Rectangles are drawn
        # 6 of them for eacn of the Layout Backgrnd
        # FloatLayout
        # RelativeLayout
        # GridLayout
        # AnchorLayout
        # BoxLayout
        # StackLayout
        with self.Main_Layout.canvas.after:
            Color(rgba = (1.0, 0.0, 0.0, 1)) # RED
            Line(points = [(Xo+1),(Y1+1), (Xo+1),(Y2-1),\
                           (X1-1),(Y2-1), (X1-1),(Y1+1)],\
                 close = True, dash_length = 4, dash_offset = 4, width = 1)
        with self.Main_Layout.canvas.after:
            #Color(rgba = (0.0, 1.0, 1.0, 1)) # Light BLUE
            Color(rgba = (1.0, 0.0, 0.0, 1)) # RED
            Line(points = [(X1+1),(Y1+1), (X1+1),(Y2-1),\
                           (X2-1),(Y2-1), (X2-1),(Y1+1)],\
                 close = True, dash_length = 8, dash_offset = 8, width = 1)
        with self.Main_Layout.canvas.after:
            Color(rgba = (1.0, 0.0, 0.0, 1)) # RED
            Line(points = [(X2+1),(Y1+1), (X2+1),(Y2-1),\
                           (X3-0),(Y2-1), (X3-0),(Y1+1)],\
                 close = True, dash_length = 4, dash_offset = 4, width = 1)
        with self.Main_Layout.canvas.after:
            #Color(rgba = (1.0, 1.0, 0.0, 1)) # YELLOW
            Color(rgba = (1.0, 0.0, 0.0, 1)) # RED
            Line(points = [(Xo+1),(Yo+1), (Xo+1),(Y1-1),\
                           (X1-1),(Y1-1), (X1-1),(Yo+1)],\
                 close = True, dash_length = 8, dash_offset = 8, width = 1)
        with self.Main_Layout.canvas.after:
            #Color(rgba = (0.0, 1.0, 0.0, 1)) # GREEN
            Color(rgba = (1.0, 0.0, 0.0, 1)) # RED
            Line(points = [(X1+1),(Yo+1), (X1+1),(Y1-1),\
                           (X2-1),(Y1-1), (X2-1),(Yo+1)],\
                 close = True, dash_length = 4, dash_offset = 4, width = 1)
        with self.Main_Layout.canvas.after:
            Color(rgba = (1.0, 0.0, 1.0, 1)) # PURPLE
            Line(points = [(X2+1),(Yo+1), (X2+1),(Y1-1),\
                           (X3-0),(Y1-1), (X3-0),(Yo+1)],\
                 close = True, dash_length = 8, dash_offset = 8, width = 1)
        #############################################
        #############################################
        # The Main Widget GridLayout positions all
        # these 6 Layouts as you add_widget them
        # to the Main_Layout
        #############################################
        #############################################
        # FLOAT LAYOUT
        self.flout.width  = Width1
        self.flout.height = Height1
        self.Main_Layout.add_widget(self.flout)
        self.IG_Float.clear()
        self.IG_Float.add(Color(rgba = (0.7, 1.0, 0.7, 1)))
        self.IG_Float.add(Rectangle(size = (self.flout.width, self.flout.height), pos = (Xo, Y1)))
        self.flout.canvas.before.add(self.IG_Float)
        ######################
        self.fbtn1.text = 'F1'
        self.fbtn1.size_hint = (.3, .3)
        self.fbtn1.pos = ((Xo+30), (Y1+30))
        self.fbtn1.color = (0, 0, 0, 1)
        self.fbtn1.background_color = (1, 1, 0, 1)
        self.flout.add_widget(self.fbtn1)
        self.fbtn1.bind(on_touch_move = self.Move_F1)
        #############################################
        #############################################
        # RELATIVE LAYOUT
        self.rlout.width  = Width1
        self.rlout.height = Height1
        self.Main_Layout.add_widget(self.rlout)
        self.IG_Relative.clear()
        self.IG_Relative.add(Color(rgba = (0.6, 1.0, 0.6, 1)))
        self.IG_Relative.add(Rectangle(size = (self.rlout.width, self.rlout.height), pos = (0, 0)))
        self.rlout.canvas.before.add(self.IG_Relative)
        ######################
        self.rbtn1.text = 'R1'
        self.rbtn1.size_hint = (.3, .3)
        self.rbtn1.pos = (0, 0)
        self.rbtn1.color = (0, 0, 0, 1)
        self.rbtn1.background_color = (1, 1, 0, 1)
        self.rlout.add_widget(self.rbtn1)
        self.rbtn1.bind(on_touch_move = self.Move_R1)
        #############################################
        #############################################
        # GRID LAYOUT
        glout = GridLayout(cols = 2,
                           spacing = 10)
        self.Main_Layout.add_widget(glout)
        with glout.canvas.before:
            Color(rgba = (0.5, 1.0, 0.5, 1))
            #Rectangle(size = (Width1, Height1), pos = (X2, Y1))
            Rectangle(size = (glout.width, glout.height), pos = (X2, Y1))
        ######################
        self.gbtn1.text = 'G1'
        self.gbtn1.size_hint_x = None
        self.gbtn1.width = 100
        glout.add_widget(self.gbtn1)
        ######################
        gbtn2 = Button(text = 'G2')
        glout.add_widget(gbtn2)
        ######################
        self.gbtn3.text = 'G3'
        self.gbtn3.size_hint_x = None
        self.gbtn3.width = 100
        glout.add_widget(self.gbtn3)
        #############################################
        #############################################
        # ANCHOR LAYOUT
        alout = AnchorLayout(anchor_x = 'right',
                             anchor_y = 'top')
        self.Main_Layout.add_widget(alout)
        with alout.canvas.before:
            Color(rgba = (0.4, 1.0, 0.4, 1))
            #Rectangle(size = (Width1, Height1), pos = (Xo, Yo))
            Rectangle(size = (alout.width, alout.height), pos = (Xo, Yo))
        ######################
        self.abtn1.text = 'A1'
        self.abtn1.size_hint = (.5, .5)
        alout.add_widget(self.abtn1)
        ######################
        self.abtn2.text = 'A2'
        self.abtn2.size_hint = (.2, .2)
        alout.add_widget(self.abtn2)
        #############################################
        #############################################
        # BOX LAYOUT
        blout = BoxLayout(orientation = 'horizontal')
        self.Main_Layout.add_widget(blout)
        with blout.canvas.before:
            Color(rgba = (0.2, 1.0, 0.2, 1))
            #Rectangle(size = (Width1, Height1), pos = (X1, Yo))
            Rectangle(size = (blout.width, blout.height), pos = (X1, Yo))
        ######################
        bbtn1 = Button(text = 'B1')
        blout.add_widget(bbtn1)
        ######################
        bbtn2 = Button(text = 'B2', size_hint = (2, .3), pos_hint = {'y': .4})
        blout.add_widget(bbtn2)
        ######################
        bbtn3 = Button(text = 'B3')
        blout.add_widget(bbtn3)
        #############################################
        #############################################
        # STACK LAYOUT
        slout = StackLayout(orientation = 'rl-tb',
                            padding = 10)
        self.Main_Layout.add_widget(slout)
        with slout.canvas.before:
            Color(rgba = (0, 1, 0, 1))
            #Rectangle(size = (Width1, Height1), pos = (X2, Yo))
            Rectangle(size = (slout.width, slout.height), pos = (X2, Yo))
        ######################
        self.sbtn1.text = 'S1'
        self.sbtn1.size_hint = (.5, .2)
        slout.add_widget(self.sbtn1)
        ######################
        self.sbtn2.text = 'S2'
        self.sbtn2.size_hint = (.5, .4)
        slout.add_widget(self.sbtn2)
        ######################
        sbtn3 = Button(text = 'S3', size_hint = (.3, .2))
        slout.add_widget(sbtn3)
        ######################
        sbtn4 = Button(text = 'S4', size_hint = (.4, .3))
        slout.add_widget(sbtn4)
        #############################################
        #############################################
        return self.Main_Layout



    def Press_F1(self, instance):
        self.Flag_F = True
        return

    def Release_F1(self, instance):
        self.Flag_F = False
        return

    def Press_R1(self, instance):
        self.Flag_R = True
        return

    def Release_R1(self, instance):
        self.Flag_R = False
        return



    def Press_A1(self, instance):
        ####################################################################
        # For FloatLayout
        #
        # the Initial position of the Layout is relative to the
        # Main_Layout and the Rectangle is not relative to FloatLayout
        # but also drawn with coordinates relative to Main_Layout as well.
        #
        self.gbtn1.text = 'G1'
        self.gbtn3.text = 'G3'
        self.flout.x = self.fX
        self.flout.y = self.fY
        self.IG_Float.clear()
        self.IG_Float.add(Color(rgba = (1, 0, 0, 1)))
        self.IG_Float.add(Rectangle(size = (self.flout.width, self.flout.height), pos = self.flout.pos))
        self.flout.canvas.before.add(self.IG_Float)
        return

    def Press_A2(self, instance):
        ####################################################################
        # For RelativeLayout
        #
        # the Initial position of the Layout is relative to the Main_Layout
        # similar to FloatLayout...   But the Rectangle is drawn at (0, 0)
        #
        self.sbtn1.text = 'S1'
        self.sbtn2.text = 'S2'
        self.rlout.x = self.rX
        self.rlout.y = self.rY
        self.IG_Relative.clear()
        self.IG_Relative.add(Color(rgba = (0, 1, 1, 1)))
        self.IG_Relative.add(Rectangle(size = (self.rlout.width, self.rlout.height), pos = (0, 0)))
        self.rlout.canvas.before.add(self.IG_Relative)
        return





    def Move_F1(self, instance, touch):
    ############################################################################
    # for a FLOAT LAYOUT
    #
    # This is proof that as you move a WIDGET the Rectangle previously
    # painted inside of it DOES NOT MOVE with the moving Widget.
    #
    # even BUTTONs and LABELs do not move with the moving FloatLayout Widget
    #
    # You have to clear the previous Draw Rectangle Instruction
    # and Draw a new Rectangle at the new coordinates so it appears the
    # Rectangle moved with the widget even thought it didn't
    #
        if(self.Flag_F):
            ####################################################################
            # For FloatLayout
            #
            # the position of the FloatLayout and Rectangle are the same
            # coordinates relative to the Main_Layout
            #
            self.flout.x = touch.x
            self.flout.y = touch.y
            self.IG_Float.clear()
            self.IG_Float.add(Color(rgba = (1, 0, 0, 1)))
            self.IG_Float.add(Rectangle(size = (self.flout.width, self.flout.height), pos = self.flout.pos))
            self.flout.canvas.before.add(self.IG_Float)
            x1 = round(self.flout.x, 0)
            x2 = round(self.flout.y, 0)
            self.gbtn1.text = str(x1)
            self.gbtn3.text = str(x2)
            
            ####################################################################
            # For RelativeLayout
            #
            # the position of the RelativeLayout is relative to the Main_Layout
            #
            self.rlout.x = touch.x + self.rX + 5
            self.rlout.y = touch.y
            self.IG_Relative.clear()
            self.IG_Relative.add(Color(rgba = (0, 1, 1, 1)))
            self.IG_Relative.add(Rectangle(size = (self.rlout.width, self.rlout.height), pos = (0, 0)))
            self.rlout.canvas.before.add(self.IG_Relative)
            x1 = round(self.rlout.x, 0)
            x2 = round(self.rlout.y, 0)
            self.sbtn1.text = str(x1)
            self.sbtn2.text = str(x2)
        return
    
    
    
    def Move_R1(self, instance, touch):
    ############################################################################
    # for a RELATIVE LAYOUT
    #
    # BUTTONs and LABELs DO MOVE with the moving RelativeLayout Widget
    #
    # the touch.x and y values are relative to the bottom left corner of
    # the RelativeLayout Widget so the values are not the same screen values
    # you got for touch.x and y when touching a FloatLayout which were 
    # relative to the bottom left corner of the Main_Layout widget
    #
        if(self.Flag_R):
            self.flout.x = (touch.x - self.rX - 5) + self.rX
            self.flout.y = (touch.y) + self.rY
            self.IG_Float.clear()
            self.IG_Float.add(Color(rgba = (1, 0, 0, 1)))
            self.IG_Float.add(Rectangle(size = (self.flout.width, self.flout.height), pos = self.flout.pos))
            self.flout.canvas.before.add(self.IG_Float)
            x1 = round(self.flout.x, 0)
            x2 = round(self.flout.y, 0)
            self.gbtn1.text = str(x1)
            self.gbtn3.text = str(x2)

            ####################################################################
            # You can NOT move the RelativeLayout Widget with
            # the touch.x and y because the touch.x and y values are
            # relative to the moving widget's bottom left corner
            # and that is moving with the moving touch.x and y values
            #
            # self.rlout.x = touch.x + self.rX
            # self.rlout.y = touch.y + self.rY
            self.IG_Relative.clear()
            self.IG_Relative.add(Color(rgba = (0, 1, 1, 1)))
            self.IG_Relative.add(Rectangle(size = (self.rlout.width, self.rlout.height), pos = (0, 0)))
            self.rlout.canvas.before.add(self.IG_Relative)
            x1 = round(touch.x, 0)
            x2 = round(touch.y, 0)
            self.sbtn1.text = str(x1)
            self.sbtn2.text = str(x2)

        return



if __name__ == "__main__":
    LayoutsApp().run()


