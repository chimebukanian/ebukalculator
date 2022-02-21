from kivy.config import Config
Config.set('kivy', 'keyboard_mode', 'systemandmulti')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class EbukalculatorApp(App):
    def build(self):
        self.icon='C:/Users/c/kviy_folder/kivyimages/PicsArt_12-27-10.23.41.png'
        self.operators= ["/", "*", "+", "-"]
        self.dividetimes=['/', '*']
        main_layout=BoxLayout(orientation="vertical")
        self.solution=TextInput(multiline=True, readonly=True, halign="right", font_size=55)
        main_layout.add_widget(self.solution)

        buttons=[
            ["7", "8", "9", "del"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]

        for row in buttons:
            h_layout=BoxLayout(size_hint=(1, 0.7))
            for label in row: 
                if label=="del":    
                    delbtn=Button(text=label, pos_hint={"center_x":0.5, 'center_y':.5})
                    delbtn.bind(on_press=self.delfun)
                    h_layout.add_widget(delbtn)
                else:    
                    button= Button(text=label, pos_hint={"center_x":0.5, 'center_y':0.5})
                    button.bind(on_press=self.on_button_press)
                    h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        eqlayout=BoxLayout(size_hint=(1, .7))
        equals_button=Button(text="=", pos_hint={"center_x":0.5, "center_y":0.5},)
        equals_button.bind(on_press=self.on_solution)
        eqlayout.add_widget(equals_button)
        
        div_button=Button(text="/", pos_hint={'center_x':.5, 'center_y':.5}, size_hint=(.333, 1))
        div_button.bind(on_press=self.on_button_press)
        eqlayout.add_widget(div_button)

        main_layout.add_widget(eqlayout)
        return main_layout

    def on_button_press(self, instance):
        current=self.solution.text
        button_text=instance.text

        if button_text=="C":
            self.solution.text=""
        else:
           new_text=current + button_text
           self.solution.text=new_text

    def on_solution(self, instance):
        text=self.solution.text
        if text:
            if text==text[-1]:
                return 
            elif text[0] in self.dividetimes and text[1]:
                self.solution.text="can't solve"
                return
            else:
                textlength=len(text)
                for i in range(textlength):
                    if text[i]=="/" and text[i+1]=='0':
                        self.solution.text="nothing is divisble by 0"
                        return
                    elif text[i] in self.operators and text[i+1] in self.dividetimes:
                        self.solution.text="can't solve"
                        return   
                        
                    elif text[i]=='+' and text[i+1]=='-':
                        text=text[:i]+text[i+1:]
                        

                    elif  text[i]=='-' and text[i+1]=='+':
                        text=text[i+1] + text[i+2:]
                        
                        
                    elif text[i]=='+' and text[i+1]=='+' or text[i]=='-' and text[i+1]=='-':
                        text=text[:i]+text[i+1:]

            solution=str(eval(self.solution.text))
            self.solution.text=text + '\n' + solution
    
    def delfun(self, instance):
        current=self.solution.text

        if not current:
            return
        if current=="can't solve":
            self.solution.text='' 
            return
        self.solution.text=current[:-1]
        

if __name__== "__main__":
        app=EbukalculatorApp()
        app.run()