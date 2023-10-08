import re
import traceback

class NameTooShortError(Exception):
    def __init__(self, name):
        self.message = f"Name '{name}' is too short (less than 4 characters)."
        super().__init__(self.message)

class MustContainAtSymbolError(Exception):
    def __init__(self):
        self.message = "Email must contain @."
        super().__init__(self.message)

class InvalidDomainError(Exception):
    def __init__(self, domain):
        self.message = f"Invalid domain: '{domain}'. Must be one of .com, .bg, .org, .net."
        super().__init__(self.message)

def is_valid_name(name):
    return len(name) > 4

def is_valid_domain(domain):
    valid_domains = (".com", ".bg", ".net", ".org")
    return domain in valid_domains

def email_validator(mail):
    pattern = r"^([a-z0-9]+[a-z0-9\.\-\_]*)(@)([a-z\-]+)(\.[a-z]+)+$"
    match = re.match(pattern, mail)

    if match is None:
        raise MustContainAtSymbolError

    name, _, _, domain = match.groups()

    if not is_valid_name(name):
        raise NameTooShortError(name)

    if not is_valid_domain(domain):
        raise InvalidDomainError(domain)

    return "Email is valid"

input_prompt = "Enter an email address or type 'End' to finish: "
command = input(input_prompt)

while command != "End":
    try:
        validate = email_validator(command)
        print(validate)
    except Exception:
        print(traceback.format_exc())

    command = input(input_prompt)
