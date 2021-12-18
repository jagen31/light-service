from flask import Flask, render_template, request
from subprocess import Popen, PIPE, STDOUT
import struct
import os

fmt = "BBB"
app = Flask(__name__)

p = Popen(['./lights'], stdout=PIPE, stdin=PIPE, stderr=PIPE)

@app.route('/', methods=('GET', 'POST'))
def create():
  if request.method == 'POST':
    print(request)
    r = int(request.json['r'])
    g = int(request.json['g'])
    b = int(request.json['b'])

    data = struct.pack(fmt, r, g, b)
    p.stdin.write(data)
    p.stdin.flush()

  return render_template('index.html')


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=8080)
