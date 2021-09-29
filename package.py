# -*- coding: utf-8 -*-

import utils


__metadata = utils.get_metadata('setup.cfg')

name = __metadata.get('name')

version = __metadata.get('version')

description = __metadata.get('version') or ''

build_command = 'pip install --target={install_path} {root}'

def commands():
    env.PYTHONPATH.append('{root}')
