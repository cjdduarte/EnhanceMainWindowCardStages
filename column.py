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

# from anki.lang import _
def _(str: str) -> str:
    return str


from aqt.deckbrowser import DeckBrowser
from aqt.qt import *
from aqt.utils import askUser

from .config import getUserOption, writeConfig



lastHandler = DeckBrowser._linkHandler


def _linkHandler(self, url):
    if ":" in url:
        (cmd, arg) = url.split(":")
        if cmd == "dragColumn":
            return columnHandler(self, arg)
    return lastHandler(self, url)


def columnHandler(self, arg):
    draggedDeckId, ontoDeckId = arg.split(",")
    draggedDeckId = int(draggedDeckId)
    ontoDeckId = int(ontoDeckId)
    columns = getUserOption("columns")
    columns.insert(draggedDeckId, columns.pop(ontoDeckId))
    writeConfig()
    self.show()





