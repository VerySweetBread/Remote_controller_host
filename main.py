from flask import Flask
from os import system as console
from subprocess import check_output as out_con

app = Flask(__name__)

mute = False
ctrl = "ctrl"  # Здесь путь до файла NirCmd.exe или просто имя файла, если находится в Path


def get_vol():
    return str(int(out_con(['get_vol'])))


@app.route('/')
def hello_world():
    return 'Success'


@app.route('/mon/<state>')
def mon(state):
    if state == 'off':
        console(f'{ctrl} monitor async_off')
        return "OK"
    elif state == 'on':
        console(f'{ctrl} sendkey ctrl press')
        return "OK"
    else:
        return "Invalid value"


@app.route('/brightness/<value>')
def brightness(value):
    console(f'{ctrl} setbrightness ' + value)
    return "OK"


@app.route('/ch_vol/<value>')
def ch_volume(value):
    value = int(value)
    val = str(int(65535 / 100 * value))
    console(f'{ctrl} changesysvolume ' + val)
    return get_vol()


@app.route('/set_vol/<value>')
def set_volume(value):
    value = int(value)
    val = str(int(65535 / 100 * value))
    console(f'{ctrl} setsysvolume ' + val)
    return get_vol()


@app.route('/get_vol')
def get_volume():
    return get_vol()


@app.route('/mute')
def mute():
    global mute
    mute = not mute
    if mute:
        console(f'{ctrl} mutesysvolume 1')
    else:
        console(f'{ctrl} mutesysvolume 0')
    return "OK"


@app.route('/media_key/<value>')
def m_key(value):
    console(f'{ctrl} sendkey ' + value + ' press')
    return "OK"


app.run("0.0.0.0")
