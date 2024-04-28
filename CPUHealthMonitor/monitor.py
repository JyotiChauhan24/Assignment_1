from flask import Flask, render_template
import psutil

app = Flask(__name__)


def get_cpu_usage():
    return psutil.cpu_percent(interval=1)


@app.route('/')
def index():
    cpu_usage = get_cpu_usage()
    return render_template('CPUmonitor.html', cpu_usage=cpu_usage)


if __name__ == '__main__':
    app.run(debug=True)