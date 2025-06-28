[app]
title = PDF Generator
package.name = pdfgen
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,pdf,ttf,xlsx
version = 1.0
requirements = python3,kivy,openpyxl,PyMuPDF,plyer
android.archs = armeabi-v7a
icon.filename = icon.png
entrypoint = main.py
orientation = portrait
android.permissions = WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 31
android.minapi = 21
android.ndk = 23b
android.useandroidx = True
android.enable_androidx = True
log_level = 2
android.entrypoint = org.kivy.android.PythonActivity

[buildozer]
log_level = 2
warn_on_root = 1