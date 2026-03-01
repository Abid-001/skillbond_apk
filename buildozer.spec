[app]

# App identity
title         = SkillBond
package.name  = skillbond
package.domain = com.skillbond

# Source
source.dir    = .
source.include_exts = py,png,jpg,kv,atlas,ttf

# Version
version       = 1.0

# Requirements — Python 3.10.11 | Kivy 2.3.0 | KivyMD 2.0.1 | Pillow latest
requirements  = python3,
                kivy==2.3.0,
                kivymd==2.0.1,
                sdl2_ttf==2.0.15,
                pillow,
                certifi

# Android settings
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api         = 33
android.minapi      = 21
android.ndk         = 25b
android.archs       = arm64-v8a, armeabi-v7a

# App icon and splash (optional — add your own icon.png)
# icon.filename     = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/splashscreen.png

# Orientation
orientation = portrait

# Fullscreen (0 = show status bar)
fullscreen    = 0

# Android gradle
android.gradle_dependencies =

# Log level
log_level     = 2

[buildozer]
log_level = 2
warn_on_root = 1
