# AGPL-3.0 License
# Copyright (C) Arthur Milchior  2018 - 2023  <https://github.com/Arthur-Milchior>
# Copyright (C) Shigeyuki 2024 <http://patreon.com/Shigeyuki>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from anki.stats import (
    colLearn,
    colMature,
    colRelearn,
    colSusp,
    colUnseen,
    colYoung,
    colCum, # Added for completeness, as it was used in getColor
)

from .config import getUserOption
from .translations import tr, DEFAULT_LANG # Import tr and DEFAULT_LANG

# Default English headers and overlays (used if a key is missing or for default logic)
# These are kept in case some logic relies on them, but primary source is translations.py via keys

def getHeader(conf):
    """Gets the header for the column configuration.
    Prioritizes 'header_key' for translation.
    Falls back to legacy 'header' or the column's 'name' or the key itself.
    """
    header_key = conf.get("header_key")
    if header_key:
        return tr(header_key)
    
    # Fallback for legacy configurations or if key is somehow missing
    name = conf.get("name")
    if "header" in conf and conf["header"] is not None: # Legacy header field
        # This might be a direct string, or could be a key if user manually edited
        # For safety, try to treat as a potential key first, then direct string
        # We need access to the translation maps for this check, which is not ideal here.
        # Simplified: assume legacy header is a literal if header_key is not present.
        return str(conf["header"])
        
    return name # Default to the column name itself if no key or specific legacy header

def getOverlay(conf):
    """Gets the overlay for the column configuration.
    Prioritizes 'overlay_key' for translation.
    Falls back to legacy 'overlay' or a generic description or the key itself.
    """
    overlay_key = conf.get("overlay_key")
    if overlay_key:
        # For bar charts, overlay might be null in config, handle this
        if conf["name"] == "bar" and not tr(overlay_key): # Check if translation is empty
             return None 
        return tr(overlay_key)
    
    # Fallback for legacy configurations or if key is somehow missing
    name = conf.get("name")
    if "overlay" in conf and conf["overlay"] is not None: # Legacy overlay field
        # Similar to getHeader, assume legacy overlay is literal if overlay_key is not present.
        return str(conf["overlay"])

    if conf["name"] == "bar": # Bars might have null overlay explicitly
        return None
        
    # If no overlay_key and no legacy overlay, return a generic message or the name
    # Or, if you want to return the key if it was defined but not found by tr, that logic is in tr.
    # Here, if overlay_key was None, we wouldn't have the key to return.
    return f"Description for {name}" # Generic fallback if no specific overlay found

def getColor(conf):
    if "color" in conf and conf.get('color') is not None:
        return conf.get('color')
    name = conf.get('name', "")
    # Color logic based on keywords in the column's 'name' (not header/overlay)
    color_map = [
        ("learning", colRelearn),
        ("unseen", colUnseen),
        ("new", colLearn),
        ("suspend", colSusp),
        ("young", colYoung),
        ("mature", colMature),
        ("buried", colSusp),
        ("repeated", colCum)
    ]
    for word, color in color_map:
        if word in name.lower(): # Match case-insensitively for robustness
            return color
    return getUserOption("default column color", "grey")
