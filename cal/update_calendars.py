#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import glob
import os
from icalendar import Calendar, vDatetime
from datetime import datetime

# cal = Calendar()
for fp in glob.glob('./*.ics'):
	if os.path.isfile(fp):
		cal_contents = Calendar.from_ical(fp)
		for event in cal_contents.events:
			if datetime.now().astimezone() > event.decoded("dtstart"):
				cal_contents.events.remove(event)

		with open(fp, "wb") as f:
			f.write(cal_contents.to_ical())
			# print(f.read())
