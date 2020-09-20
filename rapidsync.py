#!/usr/bin/env python3

# This file is part of the "upq" program used on springfiles.com to manage file
# uploads, mirror distribution etc. It is published under the GPLv3.
#
#Copyright (C) 2011 Matthias Ableitner (spring #at# abma #dot# de)
#
#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

# sf-sync: syncs file data with springfiles
# can be either initiaded by an updated file
# or maybe by the xml-rpc interface (or cron?)


from upqdb import UpqDB
import upqconfig

import sys
import logging

import json
import os
import upqjob
import upqdb

class rapidsync(upqjob.UpqJob):

	def rapidsync(self):
		from jobs import rapidsync
		j = rapidsync.Rapidsync("versionfetch", {})
		j.run()
		return j.run()
	def run(self):
		self.rapidsync()

handler = logging.StreamHandler()
handler.setFormatter(logging.Formatter("%(asctime)s %(levelname)-8s %(module)s.%(funcName)s:%(lineno)d %(message)s"))
logging.getLogger().addHandler(handler)
logging.getLogger().setLevel(logging.DEBUG)
logging.info("Started sf_sync")


upqconfig.UpqConfig(configfile="upq2.cfg")
upqconfig.UpqConfig().readConfig()
db = upqdb.UpqDB()
db.connect(upqconfig.UpqConfig().db['url'], upqconfig.UpqConfig().db['debug'])

s = rapidsync("rapidsync", dict())
s.run()

