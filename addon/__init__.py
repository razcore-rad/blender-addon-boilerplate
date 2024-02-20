from . import utils
from .dependencies import ensure_dependencies


bl_info = {
    "name": "ADDON NAME",
    "description": "ADDON DESCRIPTION",
    "author": "AUTHOR",
    "version": (0, 1),
    "blender": (4, 0, 0),
    "location": "View3D > Sidebar > Tool",
    "warning": "",  # used for warning icon and text in addons panel
    "doc_url": "",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "CATEGORY",
}

# All modules need to define:
# - `register(mods: list[types.ModuleType]) -> None`
# - `unregister(mods: list[types.ModuleType]) -> None`
mods = []


def register():
    ensure_dependencies(bl_info)
    # Import local modules here, e.g.:
    #
    # import .utils
    #
    # from . import core
    #
    # Finally store the imported modules in the `mods` list so we can de-register them. *Note* that order matters.
    # mods.extend([core, utils])
    utils.register(mods)


def unregister():
    utils.unregister(mods)
