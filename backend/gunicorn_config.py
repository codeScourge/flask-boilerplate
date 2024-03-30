# serving app
bind = "0.0.0.0:8080"


# workers
workers = 3
threads = 6
worker_class = "gthread"


# Timeout settings
timeout = 30


# Logging
import os
if not os.path.exists("./logs"): os.mkdir("./logs")

accesslog = "./logs/gunicorn_access.log"
errorlog = "./logs/gunicorn_error.log"


# Other recommended settings
preload = True  # Load the application code before forking worker processes
max_requests = 1000  # Restart workers after handling this many requests
max_requests_jitter = 50  # Randomize the max_requests value
