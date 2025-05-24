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

def conditionString(cond, string=None, parenthesis=False):
    """If the condition cond holds: return the string if it's not None, else the cond.
    If its not empty, add parenthesis around them
    """
    if not cond:
        return ""
    if string is not None:
        ret = str(string)
    else:
        ret = str(cond)
    if parenthesis:
        ret = f"(+{ret})"
    return ret


def nowLater(first, second=None):
    """A representation for the pair"""
    first = conditionString(first)
    second = conditionString(second, parenthesis=True)
    return first+second
