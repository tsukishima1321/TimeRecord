from count.models import timecount
import time
import datetime

def add_record(dic:dict):
    timezone_ = dic.get("timezone")
    writer_ = dic.get("writer")
    classroom_ = dic.get("classroom")
    timenow_ = datetime.datetime.now()
    try:
        timecount.objects.create(time=None,classroom=classroom_,writer=writer_,timezone=timezone_)
    except Exception as e:
        return -2
    return {"time":timenow_, 'timezone':timezone_, 'classroom':classroom_,'writer':writer_}
