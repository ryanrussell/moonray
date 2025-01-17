# -*- coding: utf-8 -*-
import os, sys

unittestflags = (['@run_all', '--unittest-xml']
                 if os.environ.get('BROKEN_CUSTOM_ARGS_UNITTESTS') else [])

name = 'moonray'

if 'early' not in locals() or not callable(early):
    def early(): return lambda x: x

@early()
def version():
    """
    Increment the build in the version.
    """
    _version = '13.4'
    from rezbuild import earlybind
    return earlybind.version(this, _version)

description = 'Moonray package'

authors = [
    'PSW Rendering and Shading',
    'moonbase-dev@dreamworks.com'
]

help = ('For assistance, '
        "please contact the folio's owner at: moonbase-dev@dreamworks.com")

if 'cmake' in sys.argv:
    build_system = 'cmake'
    build_system_pbr = 'cmake_modules'
else:
    build_system = 'scons'
    build_system_pbr = 'bart_scons-10'

variants = [
    ['os-CentOS-7', 'opt_level-optdebug', 'refplat-vfx2020.3', 'icc-19.0.5.281.x.2', 'amorphous-8', 'openvdb-8'],
    ['os-CentOS-7', 'opt_level-debug', 'refplat-vfx2020.3', 'icc-19.0.5.281.x.2', 'amorphous-8', 'openvdb-8'],
    ['os-CentOS-7', 'opt_level-optdebug', 'refplat-vfx2020.3', 'gcc-6.3.x.2', 'amorphous-8', 'openvdb-8'],
    ['os-CentOS-7', 'opt_level-debug', 'refplat-vfx2020.3', 'gcc-6.3.x.2', 'amorphous-8', 'openvdb-8'],
    ['os-CentOS-7', 'opt_level-optdebug', 'refplat-vfx2021.0', 'gcc-9.3.x.1', 'amorphous-8', 'openvdb-8'],
    ['os-CentOS-7', 'opt_level-debug', 'refplat-vfx2021.0', 'gcc-9.3.x.1', 'amorphous-8', 'openvdb-8'],
    ['os-CentOS-7', 'opt_level-optdebug', 'refplat-vfx2021.0', 'clang-13', 'gcc-9.3.x.1', 'amorphous-8', 'openvdb-8'],
    ['os-CentOS-7', 'opt_level-optdebug', 'refplat-vfx2022.0', 'gcc-9.3.x.1', 'amorphous-9', 'openvdb-9', 'imath-3'],
    ['os-CentOS-7', 'opt_level-debug', 'refplat-vfx2022.0', 'gcc-9.3.x.1', 'amorphous-9', 'openvdb-9', 'imath-3'],
]

conf_rats_variants = [
    ['os-CentOS-7', 'opt_level-optdebug', 'refplat-vfx2020.3', 'icc-19.0.5.281.x.2', 'amorphous-8', 'openvdb-8', 'python-2.7'],
    ['os-CentOS-7', 'opt_level-debug', 'refplat-vfx2020.3', 'icc-19.0.5.281.x.2', 'amorphous-8', 'openvdb-8', 'python-2.7'],
]

scons_targets = ['@install_include', '@install', '--no-cache'] + unittestflags
no_unit_targets = ['@install_include', '@install', '--no-cache']
proxy_targets = ['@rdl2proxy', '@install_SConscript']

sconsTargets = {
    'refplat-vfx2020.3': scons_targets,
    'refplat-vfx2021.0': scons_targets,
    'refplat-vfx2022.0': scons_targets,
}

requires = [
    'amorphous',
    'boost',
    'cuda-11.3.0.x',
    'embree-3.12.1.x.16',
    'mcrt_denoise-2.4',
    'mkl',
    'openexr',
    'openimageio-2<2.4',
    'opensubdiv-3.5.0.x.0',
    'openvdb',
    'optix-7.3.0.x',
    'random123-1.08.3',
    'scene_rdl2-11.4',
    'zlib-1.2.8.x.2'
]

private_build_requires = [
    build_system_pbr,
    'cppunit',
    'ispc-1.14.1.x',
    'python-2.7|3.7|3.9'
]

if build_system is 'cmake':
    def commands():
        prependenv('CMAKE_MODULE_PATH', '{root}/lib64/cmake')
        prependenv('CMAKE_PREFIX_PATH', '{root}')
        prependenv('SOFTMAP_PATH', '{root}')
        prependenv('RDL2_DSO_PATH', '{root}/rdl2dso')
        prependenv('LD_LIBRARY_PATH', '{root}/lib64')
        prependenv('PATH', '{root}/bin')
        prependenv('MOONRAY_CLASS_PATH', '{root}/coredata')
else:
    def commands():
        prependenv('SOFTMAP_PATH', '{root}')
        prependenv('RDL2_DSO_PATH', '{root}/rdl2dso')
        prependenv('LD_LIBRARY_PATH', '{root}/lib')
        prependenv('PATH', '{root}/bin')
        prependenv('MOONRAY_CLASS_PATH', '{root}/coredata')
    def pre_build_commands():
        env.REZ_BUILD_SCONS_ARGS.append('@install_include @install')

uuid = '355edd2d-293f-4725-afc4-73182082debd'

config_version = 0
