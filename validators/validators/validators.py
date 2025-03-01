import re

# Validate domain names. Only allow the following chars: a-z, A-Z, 0-9 and .-
def is_domain_allowed(domain):
    if not len(domain) > 3:
        return False

    if domain.startswith('.') or domain.startswith('-'):
        return False
    if domain.endswith('.') or domain.endswith('-'):
        return False
    if '--' in domain:
        return False
    if '..' in domain:
        return False

    if domain.find(".") == -1:
        return False

    pattern = re.compile(r"[a-zA-Z0-9.-]")
    for char in domain:
        if not re.match(pattern, char):
            return False

    return True

# Validate email address. Only allow the following chars: a-z, 0-9 and @.-
def is_email_allowed(self, email):
    # Check email length.
    if not len(email) > 6:
        return False
    if len(email) > 256:
        return False

    if email.count('@') != 1:
        return False
    if email.startswith('.') or email.startswith('@') or email.startswith('-'):
        return False
    if email.endswith('.') or email.endswith('@') or email.endswith('-'):
        return False

    # Split email in local part and domain part example [local part]@[domain part].
    splitted_email = email.split('@')
    local_part = splitted_email[0]
    domain_part = splitted_email[1]

    # Validate local part of email.
    if len(local_part) > 64:
        return False
    if local_part.startswith('.') or local_part.startswith('-'):
        return False
    if local_part.endswith('.') or local_part.endswith('-'):
        return False
    if '--' in local_part:
        return False
    if '..' in local_part:
        return False

    pattern = re.compile(r"[a-zA-Z0-9.+=_-]")
    for char in local_part:
        if not re.match(pattern, char):
            return False

    # Validate domain part of email.
    if self.is_domain_allowed(domain_part) != True:
        return False

    return True

# Validate account string. Only allow the following chars: A-Z and 0-9
def is_account_allowed(self, account):
    pattern = re.compile(r"[A-Z0-9]")

    for char in account:
        if not re.match(pattern, char):
            return False

    return True

# Validate openpgp public key fingerprint string. Only allow the following chars: A-Z, 0-9
def is_fingerprint_allowed(self, fingerprint):
    if fingerprint == None:
        return False

    # Fingerprint string should be 40 char.
    allowed_len = 40
    if len(fingerprint) != allowed_len:
        return False

    # Only allow A-Z, 0-9
    pattern = re.compile(r"[A-Z0-9]")
    for char in fingerprint:
        if not re.match(pattern, char):
            return False

    return True

