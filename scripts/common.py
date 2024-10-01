import re 

def replace_special_characters(s):
    replacements = {
        'æ': 'ae',
        'Æ': 'Ae',
        'ø': 'o',
        'Ø': 'O',
        'å': 'aa',
        'Å': 'Aa'
    }
    
    def replace(match):
        return replacements[match.group(0)]
    
    return re.sub(r'æ|Æ|ø|Ø|å|Å', replace, s)

def append_content_to_end_of_file(file_path: str, content: str) -> None:
    with open(file_path) as file:
        lines = file.readlines()
        file.close()
        lines.insert(len(lines), '\n' + content)

        with open(file_path, 'w') as file:
            file.writelines(lines)
            file.close()