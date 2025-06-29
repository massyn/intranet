import yaml
import os
import bcrypt
import jinja2

def render_jinja(template,output,**KW):
    os.makedirs(os.path.dirname(output),exist_ok = True)
    template_dir = '.'  # change this if your templates are somewhere else
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir)).get_template(template)
    result = env.render(**KW)
    print(f"Writing {output}")
    with open(output,'wt',encoding='utf-8') as q:
        q.write(result)

def generate_htpasswd(userlist,output):
    print(f"Generating {output}")
    with open(output,'wt',encoding='utf-8') as o:
        for username in userlist:
            password = userlist[username]

            hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            o.write(f"{username}:{hashed.decode()}\n")

def main(cfg):
    with open(cfg,'rt') as y:
        config = yaml.safe_load(y)

    #generate_htpasswd(config.get('users'),f"{OUTPUT}/.htpasswd")
    render_jinja('index.html',f"/usr/share/nginx/html/index.html",config = config)
    #render_jinja('Dockerfile',f"{OUTPUT}/Dockerfile",config = config)
    render_jinja('nginx.conf',f"/etc/nginx/nginx.conf",config = config)

main('config.yml')