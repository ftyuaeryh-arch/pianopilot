[app]

# (str) Title of your application
title = Pianopilot

# (str) Package name
package.name = pianopilot

# (str) Package domain (needed for android package identifier)
package.domain = org.pianopilot

# (str) Source code directory
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3==3.11.11,kivy==2.3.1

# (str) Icon of the application
icon.filename = %(source.dir)s/assets/icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (int) Fullscreen mode, 0 or 1
fullscreen = 0

# =============================================================================
# Android SDK / NDK Settings
# =============================================================================

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 24

# (str) Android NDK version to use
android.ndk = 25b

# (list) The Android architectures to build for
android.archs = arm64-v8a

# (str) Core recipe mapping configuration to force clean 3.11 builds
p4a.branch = master

# =============================================================================
# Buildozer Settings
# =============================================================================

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
