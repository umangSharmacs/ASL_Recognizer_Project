from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.checkbox import CheckBox
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.pagelayout import PageLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from set_hand_hist import get_hand_hist

#from fun_util import recognize
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

        wbcpermission_popup = Popup(title='Permission Denied',content=Label(text='Give Webcam Permission before proceeding further.'),size_hint=(None, None), size=(400, 400))
        
        main_layout = PageLayout()
        # Page 1-----SETTING UP HAND HIST
        layout1=BoxLayout(orientation='horizontal', padding=2)
        layout2=BoxLayout(orientation='vertical', spacing=10, padding=2)
        btn=Button(text='Set Your Hand histogram.',background_color=(53/255,92/255,125/255, 1), size_hint=(1,1), background_normal='')
        
        l=Label(text="""            -------------------INSTRUCTIONS------------------
         
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
        
        7. Swipe to the next page when you are done""", color=(1,0,1,1))
        
        webcam_permission_checkbox=CheckBox()
        webcam_permission_checkbox.bind(active=on_wbcpermission_active)
        btn.bind(on_press=set_hand_hist_button)
        layout2.add_widget(btn)
        layout2.add_widget(webcam_permission_checkbox)
        
        layout1.add_widget(layout2)
        #layout1.add_widget(webcam_permission_checkbox)
        layout1.add_widget(l)
        # Page 2------ RECOGNIZING GESTURES
        
        main_layout.add_widget(layout1)
        main_layout.add_widget(Button(text='world',background_color=(0,1,0,1)))
        main_layout.add_widget(Button(text='welcome to',background_color=(1,1,1,1)))
        main_layout.add_widget(Button(text='edureka',background_color=(0,1,1,1)))
        return main_layout
    
 
if __name__ == "__main__":
    SimpleApp().run()