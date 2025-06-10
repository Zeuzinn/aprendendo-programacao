import secrets
import string as s
from secrets import SystemRandom as Sr

# Senha aleatória segura com pontuação
print("".join(Sr().choices(s.ascii_letters + s.digits + s.punctuation, k=8)))

# Senha aleatória segura sem pontuação
print("".join(Sr().choices(s.ascii_letters + s.digits, k=8)))

random= secrets.SystemRandom()


