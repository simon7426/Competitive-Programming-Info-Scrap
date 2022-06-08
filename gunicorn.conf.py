bind = "0.0.0.0:8000"
workers = 3
# access_log_format = '%({X-Forwarded-For}i)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
accesslog = "access.log"
access_log_format = (
    "{'request_ip':'%({X-Forwarded-For}i)s','request_id':'%({X-Request-Id}i)s',"
    "'response_code':'%(s)s','request_method':'%(m)s','request_path':'%(U)s','request_querystring':'%(q)s',"
    "'request_timetaken':'%(D)s','response_length':'%(B)s'}"
)
