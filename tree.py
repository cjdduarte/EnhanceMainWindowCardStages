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

# from anki.utils import intTime
from anki.utils import int_time

from aqt import mw

from .consts import *

# Associate [column name][deck id name] to some value corresponding to
# the number of card of this deck in this column
values = dict()


def computeValues():
    # cutoff = intTime() + mw.col.get_config('collapseTime')
    cutoff = int_time() + mw.col.get_config('collapseTime')
    # print("cutoff: ", cutoff)

    today = mw.col.sched.today
    # print("today: ", today)
    tomorrow = today+1
    # yesterdayLimit = (mw.col.sched.dayCutoff-86400)*1000
    yesterdayLimit = (mw.col.sched.day_cutoff-86400)*1000
    # print("Yesterday limit is", yesterdayLimit)
    queriesCardCount = ([
        ("due tomorrow", f"queue in ({QUEUE_REV},{QUEUE_DAY_LRN}) and due = {tomorrow}", "", ""),

        # ("learning now from today", f"queue = {QUEUE_LRN} and due <= {cutoff}", "", ""),
        ("learning today from past", f"queue = {QUEUE_DAY_LRN} and due <= {today}", "", ""),
        # ("learning later today", f"queue = {QUEUE_LRN} and due > {cutoff}", "", ""),
        ("learning future", f"queue = {QUEUE_DAY_LRN} and due > {today}", "", ""),
        # ("learning today repetition from today", f"queue = {QUEUE_LRN}", f"left/1000", ""),
        ("learning today repetition from past", f"queue = {QUEUE_DAY_LRN}", f"left/1000", ""),
        # ("learning repetition from today", f"queue = {QUEUE_LRN}", f"mod%1000", ""),
        ("learning repetition from past", f"queue = {QUEUE_DAY_LRN}", f"mod%1000", ""),


        ("learning now from today", f"queue in ({QUEUE_LRN}, {QUEUE_PREVIEW}) and due <= {cutoff}", "", ""),
        # ("learning today from past", f"queue in ({QUEUE_DAY_LRN}, {QUEUE_PREVIEW}) and due <= {today}", "", ""),
        ("learning later today", f"queue in ({QUEUE_LRN}, {QUEUE_PREVIEW}) and due > {cutoff}", "", ""),
        # ("learning future", f"queue in ({QUEUE_DAY_LRN}, {QUEUE_PREVIEW}) and due > {today}", "", ""),
        ("learning today repetition from today", f"queue in ({QUEUE_LRN}, {QUEUE_PREVIEW})", f"left/1000", ""),
        # ("learning today repetition from past", f"queue in ({QUEUE_DAY_LRN}, {QUEUE_PREVIEW})", f"left/1000", ""),
        ("learning repetition from today", f"queue in ({QUEUE_LRN}, {QUEUE_PREVIEW})", f"mod%1000", ""),
        # ("learning repetition from past", f"queue in ({QUEUE_DAY_LRN}, {QUEUE_PREVIEW})", f"mod%1000", ""),


        ("review due", f"queue = {QUEUE_REV} and due <= {today}", "", ""),
        ("reviewed today", f"queue = {QUEUE_REV} and due>0 and due-ivl = {today}", "", ""),
        ("repeated today", f"revlog.id>{yesterdayLimit}", "", "revlog inner join cards on revlog.cid = cards.id"),
        
        ("unseen", f"queue = {QUEUE_NEW_CRAM}", "", ""),
        ("buried", f"queue = {QUEUE_USER_BURIED}  or queue = {QUEUE_SCHED_BURIED}", "", ""),
        ("suspended", f"queue = {QUEUE_SUSPENDED}", "", ""),
        ("cards", "", "", ""),
        ("undue", f"queue = {QUEUE_REV} and due >  {today}", "", ""),
        ("mature", f"queue = {QUEUE_REV} and ivl >= 21", "", ""),
        ("young", f"queue = {QUEUE_REV} and 0<ivl and ivl <21", "", ""),
    ])
    for name, condition, addend, table in queriesCardCount:
        if addend:
            element = f" sum({addend})"
        else:
            element = f" count(*)"
        if condition:
            condition = f" where {condition}"
        if not table:
            table = "cards"
        query = f"select did, {element} from {table} {condition} group by did"
        results = mw.col.db.all(query)
        # print("")
        # print("======================================")
        # print(f""" >>> {name} \n query:"{query}" """)
        # print(f"Results: {results}")
        values[name] = dict()
        for did, value in results:
            # print(f"did:{did} value:{value} name:{name}")
            values[name][did] = value


times = dict()


def computeTime():
    times.clear()
    for did, time in mw.col.db.all(f"select did,min(case when queue = {QUEUE_LRN} then due else null end) from cards group by did"):
        times[did] = time



    #   -- -3=user buried(In scheduler 2),
    #   -- -2=sched buried (In scheduler 2), 
    #   -- -2=buried(In scheduler 1),
    #   -- -1=suspended,
    #   -- 0=new, 1=learning, 2=review (as for type)
    #   -- 3=in learning, next rev in at least a day after the previous review
    #   -- 4=preview


# # Queue types
# CardQueue = NewType("CardQueue", int)
# QUEUE_TYPE_MANUALLY_BURIED = CardQueue(-3)
# QUEUE_TYPE_SIBLING_BURIED = CardQueue(-2)
# QUEUE_TYPE_SUSPENDED = CardQueue(-1)
# QUEUE_TYPE_NEW = CardQueue(0)
# QUEUE_TYPE_LRN = CardQueue(1)
# QUEUE_TYPE_REV = CardQueue(2)
# QUEUE_TYPE_DAY_LEARN_RELEARN = CardQueue(3)
# QUEUE_TYPE_PREVIEW = CardQueue(4)


        # ("learning now from today", f"queue = {QUEUE_LRN} and due <= {cutoff}", "", ""),
        # ("learning today from past", f"queue = {QUEUE_DAY_LRN} and due <= {today}", "", ""),
        # ("learning later today", f"queue = {QUEUE_LRN} and due > {cutoff}", "", ""),
        # ("learning future", f"queue = {QUEUE_DAY_LRN} and due > {today}", "", ""),
        # ("learning today repetition from today", f"queue = {QUEUE_LRN}", f"left/1000", ""),
        # ("learning today repetition from past", f"queue = {QUEUE_DAY_LRN}", f"left/1000", ""),
        # ("learning repetition from today", f"queue = {QUEUE_LRN}", f"mod%1000", ""),
        # ("learning repetition from past", f"queue = {QUEUE_DAY_LRN}", f"mod%1000", ""),