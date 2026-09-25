```ini
[app]

title = Pianopilot
package.name = pianopilot
package.domain = org.pianopilot

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1

# Do not pin python3 to 3.11.9.
# python-for-android will use its compatible Python recipe.
requirements = python3,kivy

icon.filename = %(source.dir)s/assets/icon.png

orientation = portrait
fullscreen = 0

# Android SDK / NDK Settings
android.api = 33
android.minapi = 24
android.ndk = 25b

[buildozer]

log_level = 2
warn_on_root = 1
```
