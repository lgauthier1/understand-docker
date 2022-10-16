import click

@click.command()
@click.argument('project')
@click.option('--version', callback=lambda c, p, v: v if v else c.params['project'])
def cli(project, version):
  print(f'=> Hello python 3.7.2. !  {project} - {version}')

cli()
