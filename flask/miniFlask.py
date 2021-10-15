import traceback
import threading
import sys
import os
import json
import time
import datetime
import re
import logging
import time


from flask import Flask, request, jsonify
from datetime import date
from datetime import timedelta
from threading import Thread

app = Flask(__name__)


#CORS(app)
app.config['COMPRESS_MIMETYPES'] = set(['text/html', 'text/css', 'text/xml', 'application/json', 'application/javascript'])  
app.config['COMPRESS_LEVEL'] = 6
app.config['COMPRESS_MIN_SIZE'] = 500

import logging
import logging.handlers

def logSetting():
    log = logging.getLogger()
    log.setLevel(logging.DEBUG)

    formatter = logging.Formatter('[%(asctime)s][%(levelname)s] %(filename)s:%(funcName)s [line:%(lineno)d]\n %(message)s\n')

    log_max_size = 10 * 1024 * 1024
    log_file_count = 20
    fileHandler = logging.handlers.RotatingFileHandler(filename='./log/etl_log.log', maxBytes=log_max_size,
                                                   backupCount=log_file_count)

    streamHandler = logging.StreamHandler()

    fileHandler.setFormatter(formatter)
    streamHandler.setFormatter(formatter)

    log.addHandler(fileHandler)
    log.addHandler(streamHandler)

@app.route("/")
def hello():
    return "Hello World!"


if __name__ == "__main__":
    logSetting()
    logging.info("Etl API 서버 로딩 준비 중 ......")
    port = 8080
    try :
        if len(sys.argv) > 1:
            port = sys.argv[1]
    except Exception as e :        
        logging.error('인수값 에러 ',e)    
    
    app = app.run(host='0.0.0.0',port=port, debug=False,threaded=True)   