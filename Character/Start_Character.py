from Character.CharacterServer import CharacterServer
import configparser
import asyncio
import flask
import threading
import sys

config = configparser.ConfigParser()
config.read('../config.ini')
char_info = config['CHARACTER']


def flask_thread():
    app = flask.Flask(__name__)
    app.static_folder = 'static'
    app.config["DEBUG"] = False
    app.use_reloader = False

    cli = sys.modules['flask.cli']
    cli.show_server_banner = lambda *x: None

    @app.route('/kick_player/<UUID>', methods=['GET'])
    def kick_player(self, UUID):
        char.kick_player(UUID=UUID)

    app.run(host=char_info['Bindip'], port=char_info['APIPort'])


if __name__ == "__main__":
    char = CharacterServer()

    api = threading.Thread(target=flask_thread)
    api.start()
    loop = asyncio.get_event_loop()
    loop.run_forever()
    loop.close()