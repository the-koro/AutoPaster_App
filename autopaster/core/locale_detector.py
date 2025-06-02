import os
import sys
import locale

def detect_locale():
    if hasattr(sys, "language"): return sys.language
    
    # Check which locales is available in "locales\\" folder
    localesavailable = [f.split(".")[0] for f in os.listdir("autopaster\\locales") if f.endswith(".txt")]

    # Get system locale (trimmed)
    system_locale = locale.getdefaultlocale()[0].split("_")[0]

    # Check if system locale is available in "locales\\" folder
    if system_locale in localesavailable:
        return system_locale
    else:
        return "en"