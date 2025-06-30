[app]
title = PDF Generator
package.name = pdfgen
package.domain = org.example
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,pdf,ttf,xlsx
version = 1.0
requirements = python3,kivy,openpyxl,PyMuPDF,plyer
orientation = portrait
entrypoint = main.py
icon.filename = icon.png
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Android Specific
android.api = 31
android.minapi = 21
android.ndk = 23b
android.ndk_path = 
android.sdk_path = 
android.useandroidx = 1
android.enable_androidx = 1
android.private_storage = 1
android.ndk_api = 21
p4a.branch = release-2022.12.20

[buildozer]
log_level = 2
warn_on_root = 1
