[app]
# (str) Title of your application
title = Ganesh Festival Greeting

# (str) Package name
package.name = ganeshgreet

# (str) Package domain (needed for android/ios packaging)
package.domain = org.ganeshgreet
 # (str) Application version
version = 0.1
requirements = python3,kivy==2.2.0
p4a.branch = release-2024.01.21
android.permissions = INTERNET, ACCESS_NETWORK_STATE

# (str) Android manifest tags to add
android.manifest_adds = 
    <uses-feature android:name="android.hardware.camera" />

# (str) Source file(s) which will be used to generate your APK
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas
# (bool) Enable audio (default yes)
audio.enable = true

# (bool) Enable images (default yes)
images.enable = true

# (bool) Enable video (default yes)
video.enable = true

# (bool) Use automatic retina display (high-density displays) support
android.private_libs = .

# (str) Build directory (set automatically)
build_dir = ./.buildozer

# (str) Distribute directory (set automatically)
dist_dir = ./dist

# (list) Android SDK version to use
android.sdk_version = 30

# (int) Android NDK version to use
android.ndk_version = r21e

# (bool) Enable multithreading if needed
android.use_ndk = False

# (str) Java compiler (default is auto-detected)
android.java_compiler = javac

# (bool) Use specific JDK for android building
android.jdk = /usr/lib/jvm/java-8-openjdk-amd64/bin/javac

# (int) Minimum API level to target (default is 16)
android.api = 30
android.archs=arm64-v8a

# (str) Android packaging mode, 'debug' or 'release'
android.package.mode = debug

# (bool) Build with KivyMD
kivy.mdmode = True

# (list) List of Python files that should be excluded from the build process
source.exclude_exts = spec.pyo,pyc,class

# (str) Name of your python file where main application is defined
main.pysource = main.py
