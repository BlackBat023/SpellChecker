from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.spelling import Spelling

Builder.load_file('spell.kv')


class MyLayout(Widget):
    def submit(self):
        # Create instance of Spelling()
        s = Spelling()

        # Select language
        s.select_language('en_UK')

        # See the Languages
        # print(word.list_languages())
        word = self.ids.word_input.text

        spell = s.suggest(word)

        output = ''

        for item in spell:
            output = f'{output}\n{item}'

        self.ids.return_label.text = f'{output}'


class SpellChecker(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    SpellChecker().run()