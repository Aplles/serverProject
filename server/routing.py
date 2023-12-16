from jinja2 import Environment, FileSystemLoader, TemplateNotFound
from server.const import BASE_DIR

env = Environment(loader=FileSystemLoader(f"{BASE_DIR}\\templates"))
env_server = Environment(loader=FileSystemLoader(f"{BASE_DIR}\\server\\templates"))


def path(url, views):
    return url, views


def render(request, template_name, context=None):
    if not context:
        context = {}
    try:
        template = env.get_template(template_name)
    except TemplateNotFound:
        template = env_server.get_template(template_name)
    return request, template.render(context)
