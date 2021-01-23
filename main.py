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

@app.get("/", response_class=HTMLResponse)
def read_path_main():
    return read_path('main')

@app.get("/{path}", response_class=HTMLResponse)
def read_path(path: str):
    try:
        template = env.get_template(path + '.html')
    except exceptions.TemplateNotFound as exc:
        template = env.get_template('default.html')

    if path in _data:
        return template.render(_data[path])

    template = env.get_template('error.html')
    return template.render()
