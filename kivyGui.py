from kivy.config import Config
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '1000')

from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from set_hand_hist import get_hand_hist
from kivy.graphics import *

import cv2 as cv
import os,sys
# from kivy.core.window import Window

from fun_util import recognize



class SimpleApp(App):
    
    webcam_permission=False

    def build(self):
        def set_hand_hist_button(instance):
            print(self.webcam_permission)
            #get_hand_hist(self.webcam_permission)
            # for pop up
            if get_hand_hist(self.webcam_permission)=='No permission Given':
                wbcpermission_popup.open()

        def on_wbcpermission_active(checkbox, value):
            if value:
                #print('The checkbox', checkbox, 'is active')
                self.webcam_permission=True
            else:
                #print('The checkbox', checkbox, 'is inactive')
                self.webcam_permission=False
        def fun_util_button(instance):
            #pass
            recognize()

        def show_gestures_function(instance):
            img=cv.imread(os.path.join(sys.path[0], "full_img.jpg"))
            cv.imshow("Recognizable gestures",img)

        wbcpermission_popup = Popup(title='Permission Denied',content=Label(text='Give Webcam Permission before proceeding further.'),size_hint=(None, None), size=(400, 400))
        
        main_layout = PageLayout()
        # Page 1-----SETTING UP HAND HIST
        layout1=BoxLayout(orientation='horizontal', padding=2)
        # with layout1.canvas:
        #     Color(45/255,20/255,44/255) 
        #     Rectangle(pos=(0, 0), size=Window.size)
        layout2=BoxLayout(orientation='vertical', spacing=10, padding=2)
        btn=Button(text='Set Your Hand histogram.',background_color=(128/255,19/255,54/255,1), size_hint=(1,1), background_normal='')
        
        l=Button(text="""            
        INSTRUCTIONS FOR SETTING THE HAND HISTOGRAM
         
        1. Allow webcam permission by clicking the 
        checkbox on your bottom right and then press
        the button on the top left.
        2. A window will appear with 50 squares (5x10).
        3. Put your hand in those squares.
        Make sure your hand covers all the squares.
        4. Press 'c'. One other window will appear "Thresh" 
        showing only white patches corresponding
        to the parts of the image which has 
        your skin color. 
        5. In case you are not successful then 
        move your hand a little bit and press 'c' again. 
        Repeat this until you get a good histogram.
        6. After you get a good histogram press 's' 
        to save the histogram. All the windows close.
        
        7. Swipe to the next page when you are done""", color=(238/255,69/255,64/255,1), background_color=(45/255,20/255,44/255,1),background_normal='', background_down='')
        

        webcam_permission_checkbox=CheckBox()
        webcam_permission_checkbox.bind(active=on_wbcpermission_active)
        btn.bind(on_press=set_hand_hist_button)
        layout2.add_widget(btn)
        layout2.add_widget(webcam_permission_checkbox)
        
        layout1.add_widget(layout2)
        #layout1.add_widget(webcam_permission_checkbox)
        layout1.add_widget(l)
        
        main_layout.add_widget(layout1)
        # Page 2------ RECOGNIZING GESTURES
        
        layout3=BoxLayout(orientation='horizontal', padding=2)
        layout4=BoxLayout(orientation='vertical', spacing=10, padding=2)
        l1=Button(text="""            
        INSTRUCTIONS FOR MAKING GESTURES
         
        1. The accuracy of recognized gesture depends upon
        the histogram made so please set an accurate histogram.
        2. Press the button on the left to open the application
        window.
        3. Make your gesture inside the neon-green space provided.
        4. Hold the gesture for '15 frames' inorder to get it 
        displayed on the screen.
        5. Check upon the thresh window in order to make better 
        gestures.
        6. Indorder to stop the recognition process press the 
        key 's' from your keyboard.
        7. Once the recognition is stopped close the recognition tabs.
        """, color=(238/255,69/255,64/255,1), background_color=(45/255,20/255,44/255,1),background_normal='', background_down='')
        fun_util_buttonn=Button(text='Press here',background_color=(81/255,10/255,50/255,1), size_hint=(1,1), background_normal='')
        show_gestures=Button(text='Show Recognizable Gestures',background_color=(81/255,10/255,50/255,1), size_hint=(1,1), background_normal='')
        fun_util_buttonn.bind(on_press=fun_util_button)
        show_gestures.bind(on_press=show_gestures_function)
        layout4.add_widget(fun_util_buttonn)
        layout4.add_widget(show_gestures)
        layout3.add_widget(layout4)
        layout3.add_widget(l1)
        main_layout.add_widget(layout3)
        main_layout.add_widget(Button(text="""
        PROJECT DEVELOPED BY
        

        Umang Sharma         101983043

        Suryansh Bhardwaj    101983044

        Prakhar Srivastava   101983045


        Students of 3COE20

        Under the guidance of Komal Gill
       
        """, color=(1,1,1,1), background_color=(199/255,44/255,65/255,1),background_normal='', background_down=''))
        
        return main_layout
    
 
if __name__ == "__main__":
    SimpleApp().run()
