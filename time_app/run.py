import datetime
import tzlocal
import time

from flask import Flask
import datetime
app = Flask(__name__)


@app.route('/')

def hello_world():
    return 'Welcome to Qifeng Zeng\'s app! Add /time to see the current time of your time zone'

@app.route('/time')
def currenttime():
    seconds_offset = time.localtime().tm_gmtoff
    hours_offset = int(seconds_offset/60/60)
    if hours_offset>=0:
        timezone = 'UTC+'+str(hours_offset)
    else:
        timezone = 'UTC'+str(hours_offset)
    now_time = datetime.datetime.now()
    str_time = datetime.datetime.strftime(now_time, '%Y-%m-%d %H:%M:%S')
    output = 'You are at timezone '+timezone+ ' and your current time is ' + str_time
    print(output)
    return output

app.run(host='0.0.0.0',
        port=8080,
        debug=True
        )

