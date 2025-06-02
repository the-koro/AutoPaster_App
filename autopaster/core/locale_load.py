from autopaster.core.locale_detector import detect_locale
from autopaster.core.resource_load import resource_path

# Locale file format
# id=text
# id2=multiline
# \ multiline 2
# \ multiline 3
# \ etc
def load_text(id, language=detect_locale()):
    try:
        file_path = resource_path(f"autopaster/locales/{language}.txt")
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        result = []
        collecting = False
        prefix = id + "="
        
        for line in lines:
            stripped = line.rstrip("\n")
            if not collecting:
                if stripped.startswith(prefix):
                    result.append(stripped[len(prefix):].strip())
                    collecting = True
            else:
                if stripped.startswith("\\"):
                    result.append(stripped[1:].strip())
                else:
                    break  # закончили собирать multiline, выходим

        return "\n".join(result) if result else ""
    
    except Exception as e:
        print(e)
        return ""
