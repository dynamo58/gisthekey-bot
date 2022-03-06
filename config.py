STREAMER = "Gisthekey"		# streamer to keep track
PERIOD = 40					# delay between streamer status checks
	# this could be made way better via EventSub, but cba
	# maybe some time

# Do not change anything below, unless you know what you're doing!
# ... that is, stepping away from CLI flags and hardcoding the config

from sys import argv

DEVELOPMENT_MODE = "--dev" in argv
VERBOSE = "--verbose" in argv
LOGGING = "--log" in argv