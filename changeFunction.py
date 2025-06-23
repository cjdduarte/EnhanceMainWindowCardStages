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
from aqt import mw
from aqt import gui_hooks

from .column import _linkHandler
from .node import idToNode, renderDeckTree


# based on Anki 2.0.36 aqt/deckbrowser.py DeckBrowser._deckRow
def deckRow(self, node, depth, cnt):
    return node.htmlRow(self, depth, cnt)


# Intercepta o método original para usar a nova API
original_deckDueTree = None

def patched_deckDueTree(*args, **kwargs):
    """Substitui deckDueTree deprecated pela nova API deck_due_tree"""
    try:
        # Tenta usar a nova API recomendada
        return mw.col.sched.deck_due_tree(*args, **kwargs)
    except AttributeError:
        # Fallback para a função original se disponível
        if original_deckDueTree:
            return original_deckDueTree(*args, **kwargs)
        else:
            # Último recurso - árvore sem contadores
            return mw.col.decks.deck_tree()


def apply_deck_tree_patch():
    """Aplica patch para substituir deckDueTree deprecated"""
    global original_deckDueTree
    if mw and mw.col and hasattr(mw.col.sched, 'deckDueTree'):
        if original_deckDueTree is None:
            # Salva a função original
            original_deckDueTree = mw.col.sched.deckDueTree
            # Substitui pela nova implementação
            mw.col.sched.deckDueTree = patched_deckDueTree


# Hook para aplicar o patch quando o perfil for carregado
def on_profile_loaded():
    """Aplica patch quando o perfil do Anki é carregado"""
    apply_deck_tree_patch()


# Aplica o patch imediatamente se já tiver coleção carregada
apply_deck_tree_patch()

# Também aplica via hook para garantir que funcione em todas as situações
gui_hooks.profile_did_open.append(on_profile_loaded)


DeckBrowser._deckRow = deckRow
DeckBrowser._renderDeckTree = renderDeckTree
DeckBrowser._linkHandler = _linkHandler
