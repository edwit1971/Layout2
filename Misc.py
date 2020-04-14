#############################################################
# File Name : Misc.py
#
#             BackgroundLabel Class
#             Change BackGround Color of Labels
#
#             ImageButton Class
#             create Images that have Button Properties
#
# Created :   March 2020 
#############################################################

from kivy.graphics           import Rectangle, Color, InstructionGroup
from kivy.uix.label          import Label
from kivy.uix.behaviors      import ButtonBehavior
from kivy.uix.scrollview     import ScrollView
from kivy.properties         import StringProperty
from kivy.uix.image          import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.floatlayout    import FloatLayout

##############################################################
##############################################################
class BackgroundLabel(Label):
    
    def __init__(self, **kwargs):
        super(BackgroundLabel, self).__init__(**kwargs)
        self.IG = InstructionGroup()
        self.background_color = (0, 0, 0, 1)
        self.color = (1, 1, 1, 1)

    def Set_Background_Color(self):
        self.opacity = 1
        self.IG.clear()
        self.IG.add(Color(rgba = (self.background_color)))
        self.IG.add(Rectangle(size = (self.size), pos = (self.pos)))
        self.canvas.before.add(self.IG)

##############################################################
##############################################################
# Instantiate a ScrollableLabel Object
# set ParentLayout
# Define the Size and Poition of ScrollWindow
# Define the text and FontSize for ScrollLabel
# Call Set_ScrollWindow()
class ScrollableLabel(ScrollView):
    def __init__(self, **kwargs):
        super(ScrollableLabel, self).__init__(**kwargs)
        ######################################
        self.ParentLayout = FloatLayout()
        self.ScrollWindow = RelativeLayout()
        self.ScrollLabel  = Label()
        self.text         = StringProperty('')
        ######################################
        self.ScrollWindow.size_hint = (None, None)
        ######################################
    
    def Set_ScrollWindow(self):
        self.ScrollWindow.clear_widgets()
        self.clear_widgets()
        self.width  = self.ScrollWindow.width
        self.height = self.ScrollWindow.height
        self.x = 0
        self.y = 0
        self.do_scroll_x = False
        self.do_scroll_y = True
        self.ParentLayout.add_widget(self.ScrollWindow)
        self.ScrollWindow.add_widget(self)
        self.ScrollLabel.halign = 'left'
        self.ScrollLabel.valign = 'top'
        self.ScrollLabel.padding_x = 6
        self.ScrollLabel.padding_y = 4
        self.ScrollLabel.x = 0
        self.ScrollLabel.y = 0
        self.ScrollLabel.size_hint = (None, None)
        self.ScrollLabel.size = (self.width, 0)
        self.ScrollLabel.text_size = (self.width, None)
        self.ScrollLabel.color = (0, 0, 0, 1)
        self.ScrollLabel.texture_update()
        self.ScrollLabel.height = self.ScrollLabel.texture_size[1]
        self.add_widget(self.ScrollLabel)

##############################################################
##############################################################
class ImageButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(ImageButton, self).__init__(**kwargs)

##############################################################
##############################################################