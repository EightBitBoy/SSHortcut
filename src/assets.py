from pathlib import Path


def get_asset_directory():
    return Path(Path(__file__), 'assets')


def get_tray_icon():
    return get_asset_directory().open('icon_tray.png')
