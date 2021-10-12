# -*- coding: utf-8 -*-

from rezutils import config


__metadata = config.get_metadata('setup.cfg')

name = __metadata.get('name')

version = __metadata.get('version')

description = __metadata.get('version') or ''

build_command = 'pip install --target={install_path} {root}'

tools = ["maya"]

def commands():
    env.PATH.prepend("{root}/bin")
