[app]

# Title of your application
title = Pianopilot

# Package name
package.name = pianopilot

# Package domain (needed for android packaging)
package.domain = org.pianopilot

# Source code directory where main.py is located
source.dir = .

# Source files to include
source.include_exts = py,png,jpg,kv,atlas

# Application version
version = 0.1

# Application requirements (add any other python libraries your app needs here)
requirements = python3,kivy

# Icon path (matches the assets folder created earlier)
icon.filename = %(source.dir)s/assets/icon.png

# Supported orientation (portrait or landscape)
orientation = portrait

# Fullscreen setting (0 = false, 1 = true)
fullscreen = 0

[buildozer]

# Log level (2 = detailed debug output)
log_level = 2

# Display warning if buildozer is run as root
warn_on_root = 1
