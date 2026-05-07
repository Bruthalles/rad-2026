import re

emails = ["teste@dominio.com", "errado@", "abc@xyz.org"]
pattern = r".+@+.\.."
for e in emails:
    print(e, bool(re.match(pattern, e)))
