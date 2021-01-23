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
        template = env.get_template(node_name + '.html')
    except exceptions.TemplateNotFound as exc:
        template = env.get_template('default.html')
    finally:
        return template


@app.get("/", response_class=HTMLResponse)
def read_path_main():
    return read_path('main')


@app.get("/{node_name}", response_class=HTMLResponse)
def read_path(node_name: str):
    data = None
    if node_name in _data:
        data = _data[node_name]

    if data is None:
        template = env.get_template('error.html')
        return template.render()

    common = None
    if 'common' in _data:
        common = _data['common']

    template = get_template(node_name)
    return template.render(data, common=common)
