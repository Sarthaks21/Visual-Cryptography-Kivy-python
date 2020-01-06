import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
import mail
import EncDec
from firebase import firebase
import json
import SENDB
import RECEIVERB


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        self.cols = 1

        super(MyGrid, self).__init__(**kwargs)
##        self.inside = GridLayout()
##        self.inside.cols = 2
##        
##        self.inside.add_widget(Label(text = 'First Name'))
##        self.name = TextInput(multiline = False)
##        self.inside.add_widget(self.name)
##
##        self.inside.add_widget(Label(text = 'Last Name'))
##        self.lastname = TextInput(multiline = False)
##        self.inside.add_widget(self.lastname)
##
##        self.inside.add_widget(Label(text = 'Email: '))
##        self.email = TextInput(multiline = False)
##        self.inside.add_widget(self.email)
##
##        self.add_widget(self.inside)

        self.submit = Button(text = "Send", font_size = 40, size = (40, 40),size_hint =(.2, .2), pos = (100,150))
        self.submit.bind(on_press = self.pressedSend)
        self.add_widget(self.submit)

        self.submit2 = Button(text = "Receive", font_size = 40, size = (40, 40),size_hint =(.2, .2), pos = (100, 300))
        self.submit2.bind(on_press = self.pressedReceive)
        self.add_widget(self.submit2)


    def pressedSend(self, instance):
        app.screen_manager.current = "SendPage"
        
    def pressedReceive(self, instance):
        app.screen_manager.current = "ReceivePage"
        
        
class sendPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 3
        self.cols = 2
        
        self.add_widget(Label(text = 'Enter receivers email id:'))
        self.name = TextInput(multiline = False, height = 5, size_hint = (0.9, 0.9))
        self.add_widget(self.name)

        self.add_widget(Label(text = 'Enter image path:'))
        self.imPath = TextInput(multiline = False, height = 5, size_hint = (0.9, 0.9))
        self.add_widget(self.imPath)
        

        self.submit = Button(text = "Submit", font_size = 40, size = (40, 40), pos = (100,150))
        self.submit.bind(on_press = self.abcd)
        self.add_widget(self.submit)
        
    def abcd(self, instance):
        ab = self.name.text
        pth = self.imPath.text
        #print(ab, pth)
        SENDB.bfunc(ab, pth)
        


        

class receivePage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.rows = 3
    
        self.add_widget(Label(text = 'Enter the decryption key received through email:'))
        self.name = TextInput(multiline = False, height = 25)
        self.add_widget(self.name)

        self.submit = Button(text = "Decode", font_size = 40, size = (100, 100), pos = (100,150))
        self.submit.bind(on_press = self.abcd)
        self.add_widget(self.submit)
        
    def abcd(self, instance):
        ab = self.name.text
        RECEIVERB.reFun(ab)
        #print(ab)



class MyApp(App):
    def build(self):
        #return MyGrid()
        self.screen_manager = ScreenManager()
        
        self.mygrid = MyGrid()
        screen = Screen(name = "Home")
        screen.add_widget(self.mygrid)
        self.screen_manager.add_widget(screen)

        self.sendpage = sendPage()
        screen = Screen(name = "SendPage")
        screen.add_widget(self.sendpage)
        self.screen_manager.add_widget(screen)

        self.receivepage = receivePage()
        screen = Screen(name = "ReceivePage")
        screen.add_widget(self.receivepage)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == '__main__':
    app = MyApp()
    app.run()
