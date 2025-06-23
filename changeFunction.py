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

from .column import _linkHandler
from .node import idToNode, renderDeckTree


# based on Anki 2.0.36 aqt/deckbrowser.py DeckBrowser._deckRow
def deckRow(self, node, depth, cnt):
    return node.htmlRow(self, depth, cnt)


def getDeckTree():
    """Obter árvore de decks usando a nova API, com fallbacks para compatibilidade"""
    try:
        # Primeiro tenta usar a nova API recomendada
        return mw.col.sched.deck_due_tree()
    except AttributeError:
        # Fallback para versões mais antigas ou schedules diferentes
        try:
            # Tenta a função deprecated (para compatibilidade temporária)
            return mw.col.sched.deckDueTree()
        except AttributeError:
            # Último recurso - árvore sem contadores
            return mw.col.decks.deck_tree()


# Intercepta o método que chama _renderDeckTree para usar nossa nova função
def _renderPage(self, reuse=False):
    """Substituição para usar sched.deck_due_tree() ao invés de deckDueTree()"""
    # Armazena a árvore para uso em outros métodos
    self._tree = getDeckTree()
    
    # Chama a lógica original do corpo
    content = self._body()
    
    # Renderiza a página com o conteúdo
    self.web.stdHtml(
        content,
        css=["css/deckbrowser.css"],
        js=["js/deckbrowser.js", "js/vendor/jquery-ui.js"],
        context=self,
    )


def _body(self):
    """Método modificado para usar nossa árvore armazenada"""
    if hasattr(self, '_tree') and self._tree is not None:
        tree = self._tree
    else:
        # Fallback se _tree não estiver definido
        tree = getDeckTree()
    
    # Constrói o HTML da lista de decks usando nosso renderDeckTree customizado
    return f"""
<center>
<table cellspacing=0 cellpadding=3>
{self._renderDeckTree(tree)}
</table>

<br>
{self._drawButtons()}
</center>
"""


DeckBrowser._deckRow = deckRow
DeckBrowser._renderDeckTree = renderDeckTree
DeckBrowser._linkHandler = _linkHandler

# Substitui os métodos que chamam deckDueTree() deprecated
DeckBrowser._renderPage = _renderPage
DeckBrowser._body = _body
