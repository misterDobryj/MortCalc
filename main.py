from kivymd.app import MDApp
from kivymd.uix.label import MDLabel


class MortCalcApp(MDApp):
    def build(self):
        return MDLabel(text="Привет, Это ипотечный калькулятор", halign="center")


MortCalcApp().run()
