import re
import io

def cleanup_email_by_regex(text):
        regex_pat = re.compile('.+Forwarded message.+([\n\r]+.+)+(<.+com>)', re.IGNORECASE)
        text = re.sub(regex_pat,'',text) 
        return text.strip() if text else ''
        # groups = re.search(regex_pat, text)
        # return groups.group(0) if groups else ''

def read_local_file(file_path):
        with io.open(file_path, mode="r", encoding="utf-8") as file:
            return file.read()

text = read_local_file("test_text.txt")
# print(text)
result = cleanup_email_by_regex(text)
print(result)
