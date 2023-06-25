from var.args            import args
from controllers.request import req
from controllers.config  import *
import click

config = read_config()
arg    = [arg for arg in args]

@click.group()
def cli():
  pass

@cli.command(arg[0])
@click.option(args[arg[0]]['short'][0], args[arg[0]]['command'][0], help=args[arg[0]]['help'][0], type=args[arg[0]]['type'], required=args[arg[0]]['required'])
@click.option(args[arg[0]]['short'][1], args[arg[0]]['command'][1], help=args[arg[0]]['help'][1], type=args[arg[0]]['type'], required=args[arg[0]]['required'])
def user(user,auth):
  if not user and not auth:
    u = config['user']
    click.echo(f'Current user: {u}' if u != '' else 'No user - Access with your user')
  else:
    password = click.prompt('Password', hide_input=True)
    data = {
      'n': user,
      'a': auth,
      'p': password
    }
    res = req(data)
    print(res['message'])

@cli.command(arg[1])
@click.option(args[arg[1]]['short'][0], args[arg[1]]['command'][0], help=args[arg[1]]['help'][0], type=args[arg[1]]['type'], required=args[arg[1]]['required'])
@click.option(args[arg[1]]['short'][1], args[arg[1]]['command'][1], help=args[arg[1]]['help'][1], type=args[arg[1]]['type'], required=args[arg[1]]['required'])
@click.option(args[arg[1]]['short'][2], args[arg[1]]['command'][2], help=args[arg[1]]['help'][2], type=args[arg[1]]['type'], required=args[arg[1]]['required'])
@click.option(args[arg[1]]['short'][3], args[arg[1]]['command'][3], help=args[arg[1]]['help'][3], type=args[arg[1]]['type'], required=args[arg[1]]['required'])
@click.option(args[arg[1]]['short'][4], args[arg[1]]['command'][4], help=args[arg[1]]['help'][4], type=args[arg[1]]['type'], required=args[arg[1]]['required'])
@click.option(args[arg[1]]['short'][5], args[arg[1]]['command'][5], help=args[arg[1]]['help'][5], type=args[arg[1]]['type'], required=args[arg[1]]['required'])
def user(create,rename,delete,user,file,list):
  click.echo(list)