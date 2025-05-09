from nicegui import ui

@ui.page('/')
def home():
    ui.label('NiceGUI rodando com Docker via Dockge!')

ui.run(host='0.0.0.0', port=8080)