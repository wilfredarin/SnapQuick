from datetime import datetime
import time;


class snap_time():
	def record_time(self):
		no = datetime.now()
		return no

	def post_time(self):
		no = datetime.now()
		print(no.strftime("%c"))

	def stamp_time(self):
		ts = time.time()
		return (ts)







