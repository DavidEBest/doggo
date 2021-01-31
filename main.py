from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from yaml import dump, safe_load
from jinja2 import Environment, FileSystemLoader, exceptions

app = FastAPI()

try:
    with open("app.yaml", "r") as stream:
        _data = safe_load(stream)
except yaml.YAMLError as exc:
    print(exc)

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)


def get_template(node_name: str):
    try:
        template = env.get_template('app/' + node_name + '.html')
    except exceptions.TemplateNotFound as exc:
        template = env.get_template('app/' + 'default.html')
    finally:
        return template


def get_card_data(node_name: str):
    data = None
    if 'cards' in _data:
        if node_name in _data['cards']:
            data = _data['cards'][node_name]
    elif node_name in _data:
        data = _data[node_name]

    return data


@app.get("/", response_class=HTMLResponse)
def read_path_main():
    template = env.get_template('admin/' + 'main.html')
    return template.render(data=_data)


@app.get("/admin", response_class=HTMLResponse)
def read_admin():
    template = env.get_template('admin/' + 'main.html')
    return template.render(data=_data)


@app.get("/{node_name}", response_class=HTMLResponse)
def read_path(node_name: str):
    data = get_card_data(node_name)
    if data is None:
        template = env.get_template('app/' + 'default.html')
        return template.render()

    common = None
    if 'common' in _data:
        common = _data['common']

    template = get_template(node_name)
    return template.render(data, common=common)
