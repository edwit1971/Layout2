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
from kivy.graphics import Rectangle, Color, Line


class LayoutsApp(App):
    def build(self):
        #############################################
        Main_Layout = GridLayout(rows = 2)
        Width_Max = Window.width
        Height_Max = Window.height
        Main_Layout.height = Height_Max
        Main_Layout.width = Width_Max
        Main_Layout.x = 0
        Main_Layout.y = 0
        with Main_Layout.canvas.before:
            Color(rgba = (0.5, 0.5, 0.5, 1))
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
        #############################################
        with Main_Layout.canvas.after:
            Color(rgba = (1.0, 0.0, 0.0, 1))
            Line(points = [(Xo+1),(Y1+1), (Xo+1),(Y2-1),\
                           (X1-1),(Y2-1), (X1-1),(Y1+1)],\
                 close = True, dash_length = 4, dash_offset = 4, width = 1)
        with Main_Layout.canvas.after:
            Color(rgba = (1.0, 1.0, 0.0, 1))
            Line(points = [(X1+1),(Y1+1), (X1+1),(Y2-1),\
                           (X2-1),(Y2-1), (X2-1),(Y1+1)],\
                 close = True, dash_length = 8, dash_offset = 8, width = 1)
        with Main_Layout.canvas.after:
            Color(rgba = (1.0, 0.0, 0.0, 1))
            Line(points = [(X2+1),(Y1+1), (X2+1),(Y2-1),\
                           (X3-0),(Y2-1), (X3-0),(Y1+1)],\
                 close = True, dash_length = 4, dash_offset = 4, width = 1)
        with Main_Layout.canvas.after:
            Color(rgba = (1.0, 1.0, 0.0, 1))
            Line(points = [(Xo+1),(Yo+1), (Xo+1),(Y1-1),\
                           (X1-1),(Y1-1), (X1-1),(Yo+1)],\
                 close = True, dash_length = 8, dash_offset = 8, width = 1)
        with Main_Layout.canvas.after:
            Color(rgba = (1.0, 0.0, 0.0, 1))
            Line(points = [(X1+1),(Yo+1), (X1+1),(Y1-1),\
                           (X2-1),(Y1-1), (X2-1),(Yo+1)],\
                 close = True, dash_length = 4, dash_offset = 4, width = 1)
        with Main_Layout.canvas.after:
            Color(rgba = (1.0, 1.0, 0.0, 1))
            Line(points = [(X2+1),(Yo+1), (X2+1),(Y1-1),\
                           (X3-0),(Y1-1), (X3-0),(Yo+1)],\
                 close = True, dash_length = 8, dash_offset = 8, width = 1)
        #############################################
        flout = FloatLayout()
        Main_Layout.add_widget(flout)
        with flout.canvas.before:
            Color(rgba = (0.1, 0.1, 0.1, 1))
            Rectangle(size = (flout.width, flout.height), pos = (Xo, Y1))
        ######################
        fbtn1 = Button(text = 'F1', size_hint = (.3, .3), pos = ((Xo+30), (Y1+30)))
        flout.add_widget(fbtn1)
        #############################################
        rlout = RelativeLayout()
        Main_Layout.add_widget(rlout)
        with rlout.canvas.before:
            Color(rgba = (0.2, 0.2, 0.2, 1))
            Rectangle(size = (Width1, Height1), pos = (0, 0))
        ######################
        rbtn1 = Button(text = 'R1', size_hint = (.3, .3), pos = (0, 0))
        rlout.add_widget(rbtn1)
        #############################################
        glout = GridLayout(cols = 2,
                           spacing = 10)
        Main_Layout.add_widget(glout)
        with glout.canvas.before:
            Color(rgba = (0.3, 0.3, 0.3, 1))
            Rectangle(size = (Width1, Height1), pos = (X2, Y1))
        ######################
        gbtn1 = Button(text = 'G1', size_hint_x = None, width = 50)
        glout.add_widget(gbtn1)
        ######################
        gbtn2 = Button(text = 'G2')
        glout.add_widget(gbtn2)
        ######################
        gbtn3 = Button(text = 'G3', size_hint_x = None, width = 50)
        glout.add_widget(gbtn3)
        #############################################
        alout = AnchorLayout(anchor_x = 'right',
                             anchor_y = 'top')
        Main_Layout.add_widget(alout)
        with alout.canvas.before:
            Color(rgba = (0.4, 0.4, 0.4, 1))
            Rectangle(size = (Width1, Height1), pos = (Xo, Yo))
        ######################
        abtn1 = Button(text = 'A1', size_hint = (.5, .5))
        alout.add_widget(abtn1)
        ######################
        abtn2 = Button(text = 'A2', size_hint = (.2, .2))
        alout.add_widget(abtn2)
        #############################################
        blout = BoxLayout(orientation = 'horizontal')
        Main_Layout.add_widget(blout)
        with blout.canvas.before:
            Color(rgba = (0.5, 0.5, 0.5, 1))
            Rectangle(size = (Width1, Height1), pos = (X1, Yo))
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
        slout = StackLayout(orientation = 'rl-tb',
                            padding = 10)
        Main_Layout.add_widget(slout)
        with slout.canvas.before:
            Color(rgba = (0.6, 0.6, 0.6, 1))
            Rectangle(size = (Width1, Height1), pos = (X2, Yo))
        ######################
        sbtn1 = Button(text = 'S1', size_hint = (.6, .2))
        slout.add_widget(sbtn1)
        ######################
        sbtn2 = Button(text = 'S2', size_hint = (.4, .4))
        slout.add_widget(sbtn2)
        ######################
        sbtn3 = Button(text = 'S3', size_hint = (.3, .2))
        slout.add_widget(sbtn3)
        ######################
        sbtn4 = Button(text = 'S4', size_hint = (.4, .3))
        slout.add_widget(sbtn4)
        #############################################
        return Main_Layout
    

if __name__ == "__main__":
    LayoutsApp().run()
    
