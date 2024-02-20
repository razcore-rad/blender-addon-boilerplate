# Blender Addon Template

Minimal and opinionated template code for Blender Addon development.

## Structure

```sh
addon
├── dependencies.py # `ensure_dependencies()` utility function that uses `pip` & `requirements.txt` to install packages into the `addon/dependencies` local folder
├── __init__.py # addon entry point
├── paths.py # defines `ADDON_PATH`, a `Path` object that points to the current addon path folder
├── requirements.txt # see `dependencies.py` comment
└── utils.py # defines `[un]register(mods: list[types.ModuleType]) -> Node` helper methods, see the contents of `__info__.py` for further comments
```
