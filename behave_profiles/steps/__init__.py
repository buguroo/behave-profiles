from . import _steps
from .i18n import languages
from .stepcollection.behave_stepcollection import define_steps

define_steps(r"^behave_profiles\.steps\.(?P<lang>[^\.]+)$",
             _steps,
             languages)
