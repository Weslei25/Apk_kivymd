import kivy
from kivymd.uix.card import MDCard
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.behaviors import FocusBehavior
from kivymd.uix.button import MDRaisedButton

from kivymd.app import MDApp
from kivy.lang import Builder


kivy.require('1.0.7')

KV = '''
Screen:
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Fala Tchouzen'
            left_action_items: [["menu", lambda x: x]]
            right_action_items: [["dots-vertical", lambda x: x]]
        TelaLogin:

<SenhaCard>:
    id: card
    orientation: 'vertical'
    size_hint: .7, .7
    pos_hint: {'center_x': .5, 'center_y': .5}

    MDBoxLayout:
        size_hint_y: .2
        padding: [25, 0, 25, 0]
        md_bg_color: app.theme_cls.primary_color

        MDLabel:
            text: 'Mudar senha'
            theme_text_color: 'Custom'
            text_color: 1, 1, 1, 1

        MDIconButton:
            pos_hint: {'center_x': .4, 'center_y': .5}
            theme_text_color: 'Custom'
            icon: 'close'
            text_color: 1, 1, 1, 1
            on_release: root.fechar()

    MDFloatLayout:
        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .8}
            size_hint_x: .9
            hint_text: 'Código enviado por email.'
            
        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .6}
            size_hint_x: .9
            hint_text: 'Nova senha:'

        MDTextField:
            pos_hint: {'center_x': .5, 'center_y': .4}
            size_hint_x: .9
            hint_text: 'Confirmar nova senha:'
        
        MDRaisedButton:
            pos_hint: {'center_x': .5, 'center_y': .2}
            size_hint_x: .9
            text: 'Recadastrar'

<TelaLogin>:
    MDIconButton:
        pos_hint: {'center_x': .5, 'center_y': .8}
        icon: 'account-circle'
        user_font_size: '80sp'
    MDTextField:
        size_hint_x: .9
        hint_text: 'Email:'
        pos_hint:{'center_x': .5, 'center_y': .6}
    MDTextField:
        size_hint_x: .9
        hint_text: 'Senha:'
        pos_hint: {'center_x': .5, 'center_y': .5}
    ButtoonFocus:
        size_hint_x: .9
        pos_hint: {'center_x': .5, 'center_y': .4}
        text: 'Login'
        focus_color: app.theme_cls.accent_color
        unfocus_color: app.theme_cls.primary_color
    
    MDLabel:
        pos_hint: {'center_x': .5, 'center_y': .3}
        text: "Esqueceu sua senha?"
        halign: 'center'
    MDTextButton:
        pos_hint: {'center_x': .5, 'center_y': .2}
        text: 'Clique aqui'
        on_release: root.abrir_card()

'''


class SenhaCard(MDCard):
    def fechar(self):
        self.parent.remove_widget(self)


class TelaLogin(FloatLayout):
    def abrir_card(self):
        try:
            self.add_widget(SenhaCard())
        except Exception as e:
            print('{}'.format(e))


class ButtoonFocus(MDRaisedButton, FocusBehavior):

    ...


class MyApp(MDApp):
    def build(self):
        self.theme_cls.primary_palette = 'Purple'
        self.theme_cls.accent_palette = 'Red'
        self.theme_cls.primary_hue = '700'

        try:
            return Builder.load_string(KV)
        except Exception as e:
            print('{}'.format(e))


MyApp().run()
