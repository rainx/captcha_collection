import sys
import os
import click

cur_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.insert(0, cur_path)

from guis.MainWindowUIExt import MainWindowUIExt
from PySide import QtGui
import sys


@click.command()
@click.option('--site', '-s', type=str, default="")
def cli(site):

    # load all sites
    sites_path = [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "sites"),
        os.path.join(os.path.expanduser('~'), '.captcha_collection_sites')
    ]

    site_mods = {}
    for path in sites_path:
        if os.path.isdir(path):
            # add path to system import path
            for file in os.listdir(path):
                fullpath = os.path.join(path, file)
                if fullpath.endswith('.py'):
                    new_mod = {}
                    exec(open(fullpath).read(), new_mod)
                    if 'site_name' in new_mod:
                        site_mods[new_mod['site_name']] = new_mod

    ####
    if site == "":
        site_mods_keys = list(site_mods.keys());
        click.echo("-" * 30)
        [click.echo("[%d] : %s" % (index, key)) for (index,key) in enumerate(site_mods_keys)]
        click.echo("-" * 30)
        index = click.prompt('Please enter a number to pick the site name', type=int)
        site = site_mods_keys[index]

    if site in site_mods:
        site_mod = site_mods[site]
    else:
        click.secho('No site mod found of this site name: %s' % site)
        sys.exit(-1)

    app = QtGui.QApplication(sys.argv)
    main_window = MainWindowUIExt(site_mod)
    main_window.show()
    app.exec_()

if __name__ == '__main__':
    cli();