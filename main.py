import os
import fitz  # PyMuPDF
import openpyxl

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.modalview import ModalView

class PDFApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.label = Label(text="Single Name Entry or Select Excel File")
        self.text_input = TextInput(hint_text='Enter a single name (optional)', multiline=False)
        submit_button = Button(text='Generate from Name')
        submit_excel_button = Button(text='Generate from Excel File')
        submit_button.bind(on_press=self.generate_single_pdf)
        submit_excel_button.bind(on_press=self.open_file_chooser)
        layout.add_widget(self.label)
        layout.add_widget(self.text_input)
        layout.add_widget(submit_button)
        layout.add_widget(submit_excel_button)
        return layout

    def generate_single_pdf(self, instance):
        name = self.text_input.text.strip()
        if not name:
            self.show_popup("Error", "Please enter a name.")
            return
        self.create_pdf(name)

    def open_file_chooser(self, instance):
        chooser = FileChooserIconView(filters=['*.xlsx'])
        view = ModalView(size_hint=(0.9, 0.9))
        chooser.bind(on_submit=lambda chooser, selection, touch: self.load_excel(selection, view))
        view.add_widget(chooser)
        view.open()

    def load_excel(self, selection, view):
        view.dismiss()
        if not selection:
            return
        file_path = selection[0]
        try:
            wb = openpyxl.load_workbook(file_path)
            sheet = wb.active
            names = [row[0].value for row in sheet.iter_rows(min_row=2) if row[0].value]
            for name in names:
                self.create_pdf(name)
            self.show_popup("Success", f"PDFs created for {len(names)} names.")
        except Exception as e:
            self.show_popup("Error", f"Failed to read Excel file: {str(e)}")

    def create_pdf(self, name):
        try:
            pdf_template = "demo copy.pdf"
            if not os.path.exists(pdf_template):
                self.show_popup("Error", f"Template PDF '{pdf_template}' not found.")
                return
            output_dir = "pdfdow"
            os.makedirs(output_dir, exist_ok=True)
            output_pdf = os.path.join(output_dir, f"{name.replace(' ', '_')}.pdf")
            doc = fitz.open(pdf_template)
            page = doc[0]
            position = fitz.Point(200, 346)
            page.insert_text(position, name, fontsize=22, fontname="helv", color=(1, 0, 0))
            doc.save(output_pdf)
            doc.close()
            self.show_popup("Success", f"PDF created for '{name}' in folder 'pdfdow'.")
        except Exception as e:
            self.show_popup("Error", f"Failed to create PDF for {name}: {str(e)}")

    def show_popup(self, title, message):
        popup = Popup(title=title, content=Label(text=message), size_hint=(None, None), size=(400, 200))
        popup.open()

if __name__ == '__main__':
    PDFApp().run()