import os

from django.core.exceptions import ImproperlyConfigured



def get_required(name : str) -> str:
    required = os.environ.get(name)
    if (required is None or required.strip() == ""):
        raise ImproperlyConfigured(f"The {name} environment variable is required")
    return required

def get_bool(name : str, default : bool)-> bool:
    item = os.environ.get(name)
    if item is None :
        return default
    match str(item).strip().lower() :
        case "true" : return True
        case "false" : return False
        case _: raise ImproperlyConfigured(f"The {name} environment variable should be true or false")

def get_list(name : str, default : list) -> list :
    raw_value = os.environ.get(name)
    if raw_value is None :
        return default
    value = str(raw_value).split(",")
    value = [host.strip() for host in value if host.strip() != ""]
    return value if len(value) > 0 else default

def five_diffrent_chars(key):
    chars = set(key)
    return len(chars)

def is_weak_secret(key):
    if(len(key) < 50 or key.startswith("django-insecure") or five_diffrent_chars(key) < 5) :
        return True
