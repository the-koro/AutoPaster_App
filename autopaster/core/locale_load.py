from autopaster.core.resource_load import resource_path

# Locale file format
# id=text
def load_text(id, language="en"):
    try:
        file_path = resource_path(f"autopaster/locales/{language}.txt")
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.startswith(id):
                    return line[len(id)+1:].strip()
            return ""
    except Exception as e:
        print(e)
        return ""