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

from anki.decks import DeckManager
from anki.notes import Note
try:
    from anki.sched import Scheduler # type:ignore
except ModuleNotFoundError:
    from anki.scheduler import v3
from aqt.deckbrowser import DeckBrowser

from .column import _linkHandler
from .node import idToNode, renderDeckTree


# based on Anki 2.0.36 aqt/deckbrowser.py DeckBrowser._deckRow
def deckRow(self, node, depth, cnt):
    return node.htmlRow(self, depth, cnt)


DeckBrowser._deckRow = deckRow

DeckBrowser._renderDeckTree = renderDeckTree

DeckBrowser._linkHandler = _linkHandler
