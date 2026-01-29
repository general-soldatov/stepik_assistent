import json
import os
import click
import subprocess
import logging
from app.creator.create import BuildProject, ImportProject
from app.config import config, create_division, PATH

@click.group()
def cli():
    pass

def division(func):
    def inner(*args, **kwargs):
        try:
            click.echo(create_division(config.data_prog['start']))
            func(*args, **kwargs)
            click.echo(create_division(config.data_prog["end"]))
        except Exception as e:
            # logging.ERROR(e)
            print(e)
    return inner

@cli.command("config", help="Update of config data")
@division
def configurate():
    click.echo('Load of program`s config')
    subprocess.run([config.app, PATH])
    click.echo('Update file succesfull')

@cli.command("prompt", help="Print of the prompt to AI-model")
@division
def prompt():
    click.echo(config.prompt)
    if not os.path.exists(config.path_ai):
        with open(config.path_ai, 'w', encoding='utf-8') as file:
            file.write('Insert your responsible from AI-model at json')

@cli.command("create", help="Create project's makefile")
@click.option("--path", prompt="Path", help="Check path to makefile", default=config.path_default)
@click.option("--ai_path", prompt="Path to AI", help="Path to AI-responsible from json", default=config.path_ai)
@division
def create(path, ai_path):
    project = BuildProject()
    if click.confirm(f"Do you want to add text to the project"):
        project.add_text()
    if click.confirm(f"Do you want to add AI-responsible to the project"):
        with open(ai_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            project.import_ai(data)
    if click.confirm(f"Do you want to add choice's test to the project"):
        project.add_choice()
    if click.confirm(f"Do you want to add sorting task to the project"):
        project.add_sorting()
    if click.confirm(f"Do you want to add matching task to the project"):
        project.add_matching()
    if click.confirm(f"Do you want to add program to the project"):
        project.add_program()
    project.export_to_yaml(path)

@cli.command("build", help="Build project from makefile")
@click.option("--path", prompt="Path", help="Check path to makefile", default=config.path_default)
@division
def build(path):
    data = ImportProject(path)
    data.create()

@cli.command("check", help="Check of test project from makefile")
@click.option("--path", prompt="Path", help="Check path to makefile", default=config.path_default)
@division
def check(path):
    data = ImportProject(path)
    data.check()

if __name__ == '__main__':
    cli()