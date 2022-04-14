import typing as t
import os


class ConfigVarRequiredError(Exception):
    pass


def getenv(
    key: str, default: str = None, conv: t.Callable = str, required: bool = True
) -> t.Any:
    """If `default` is None, then the var is non-optional."""
    var = os.getenv(key, default)
    if var is None and required is True:
        raise ConfigVarRequiredError(
            f"Configuration variable '{key}' is required but was not provided."
        )
    elif var is not None:
        return conv(var)
    else:
        return None


# AES Cipher key.
AES_KEY = "6gZW4ARFINh4DR1uIzn12l7Mh1UF982L"


# The prefix used on every API endpoint in the project.
URL_PREFIX = getenv("URL_PREFIX", default="/pcui-mock")
