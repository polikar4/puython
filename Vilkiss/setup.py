# coding: utf-8

from cx_Freeze import setup, Executable

executables = [Executable('Ui_vilka_v1_2_1.py')]

options = {
    'build_exe': {
        'include_msvcr': True,
    }
}

setup(name='hello_world',
      version='0.0.2',
      description='My Hello World App!',
      executables=executables,
      options=options)