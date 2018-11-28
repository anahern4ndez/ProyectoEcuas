import sys
from cx_Freeze import setup,Executable

additional_mods = ['numpy.core._methods', 'numpy.lib.format']
setup(
    name = "Simulador",
    version = "1.0",
    description = "Resolves by ODE a system of spring-mass to modelate the move respect time of the x displacement of a building floor",
    options = {'build_exe': {'includes':additional_mods}},
    executables = [Executable("main.py")])
