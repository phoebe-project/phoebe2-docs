import pydoc
import os, sys
import re

def md_internal_link(matchobj):
    text = matchobj.group(0)
    path = text[4:-4]
    return "[{}]({}.md)".format(path, path)

def get_kind(item):
    kind = ''
    if pydoc.inspect.isclass(item):
        kind = 'class'
    elif pydoc.inspect.ismodule(item):
        kind = 'module'
    elif pydoc.inspect.ismethod(item):
        kind = 'method'
    elif pydoc.inspect.isfunction(item):
        kind = 'function'
    elif pydoc.inspect.isdatadescriptor(item):
        kind = 'property'

    return kind

def api_docs(item, skip=[], prefix='', subclass_of=None, write=True, members=[pydoc.inspect.ismethod, pydoc.inspect.isfunction, pydoc.inspect.isdatadescriptor]):
    def check_member(item):
        for member in members:
            if member(item):
                return True

        return False

    # item is either a module or class
    stored_fms = []

    for fm in pydoc.inspect.getmembers(item, check_member):
        output = list()

        if fm[0] in skip or (fm[0].startswith('_') and fm[0] != '__init__'):
            continue

        if pydoc.inspect.ismodule(fm[1]) or pydoc.inspect.isclass(fm[1]):
            stored_fms.append(fm[0])
            # don't write its own page, make a manual call to api_docs to do that... but we will create the link
            continue

        path = [p for p in prefix.split(".")+[item.__name__.split(".")[-1]] if len(p)]
        path_md = ".".join(["[{}]({}.md)".format(p, ".".join(path[:i+1])) for i,p in enumerate(path)])
        # print "***", path, path_md
        output.append("### {}.{} ({})\n\n".format(path_md, fm[0], get_kind(fm[1])))

        # Get the signature
        if pydoc.inspect.ismethod(fm[1]) or pydoc.inspect.isfunction(fm[1]):
            output.append ('```py\n')
            output.append('def %s%s\n' % (fm[0], pydoc.inspect.formatargspec(*pydoc.inspect.getargspec(fm[1]))))
            output.append ('```\n')

        # get the docstring
        if pydoc.inspect.getdoc(fm[1]):
            output.append('\n')
            docstring = pydoc.HTMLDoc().markup(pydoc.inspect.getdoc(fm[1]))
            docstring = re.sub(r"(?P<name>&lt;[0-9a-zA-Z_\.]*&gt;)", md_internal_link, docstring)
            output.append(docstring)

        output.append('\n')


        stored_fms.append(fm[0])

        if write:
            path = ".".join([p for p in prefix.split(".") if len(p)]+[item.__name__.split(".")[-1], fm[0]])

            filename = './api/{}.md'.format(path)
            print("writing {}".format(filename))
            f_method = open(filename, 'w')
            f_method.write("\n".join(output))
            f_method.close()

    if write:
        path = [p for p in prefix.split(".")+[item.__name__.split(".")[-1]] if len(p)]
        path_md = ".".join(["[{}]({}.md)".format(p, ".".join(path[:i+1])) for i,p in enumerate(path[:-1])])
        if len(path_md):
            path_md += ".{}".format(item.__name__.split(".")[-1])
        else:
            path_md = item.__name__.split(".")[-1]

        path = ".".join(path)
        filename_class = './api/{}.md'.format(path)
        print("writing {}".format(filename_class))
        f_class = open(filename_class, 'w')
        f_class.write("## {} ({})\n\n".format(path_md, get_kind(item)))
        if subclass_of is not None:
            f_class.write("{} is a subclass of {} and therefore also includes all [{} methods]({}.md)\n\n".format(item.__name__, subclass_of, subclass_of, subclass_of))
        for fm in stored_fms:
            path_fm = ".".join([p for p in prefix.split(".") if len(p)]+[item.__name__.split(".")[-1], fm])
            f_class.write("* [{}]({}.md)\n".format(fm, path_fm))
        f_class.close()

    return stored_fms


if __name__ == '__main__':
    import phoebe

    print("CREATING API DOCS FOR PHOEBE VERSION: {}".format(phoebe.__version__))

    skip_ps = ['default_triple',
               'set_meta',
               'get_plotting_info',
               'URLError']

    skip_param = ['set_uniqueid']

    skip_phoebe = ['default_triple', 'devel_off', 'devel_on',
                   'algorithms', 'backend', 'c',
                   'component', 'compute', 'constraint', 'constraints',
                   'feature',
                   'dataset', 'dependencies', 'dynamics',
                   'hierarchy', 'libphoebe', 'u', 'utils', 'Bundle']

    skip_frontend = ['io', 'tabcomplete']

    skip_frontend_bundle = ['ArrayParameter',
                            'BaseNamespace', 'BoolParameter', 'ChoiceParameter',
                            'ConstraintParameter', 'DictParameter',
                            'FloatArrayParameter', 'FloatParameter',
                            'HierarchyParameter',
                            'IntArrayParameter', 'IntParameter',
                            'JobParameter',
                            'URLError',
                            'OrderedDict', 'Parameter', 'ParameterSetInfo',
                            'ParameterSet', 'SelectParameter', 'SocketIO',
                            'StrictVersion', 'StringParameter', 'TwigParameter',
                            'datetime', 'deepcopy', 'fnmatch',
                            'parameter_from_json', 'parse_json', 'send_if_client',
                            'update_if_client', 'ConstraintVar', 'cfit']

    skip_parameters = ['deepcopy', 'fnmatch', 'send_if_client', 'update_if_client',
                       'ConstraintVar', 'DictParameter', 'ParameterSetInfo',
                       'IntArrayParameter', 'TwigParameter', 'autofig', 'datetime',
                       'difflib', 'functools', 'itertools', 'json', 'logging',
                       'np', 'nparray', 'os', 'parameter_from_json', 'parse_json',
                       'random', 're', 'readline', 'requests', 'string', 'sympy',
                       'sys', 'tabcomplete', 'time', 'twighelpers', 'types', 'u',
                       'json', 'ujson', 'webbrowser', 'OrderedDict', 'corner',
                       'dyplot', 'distl']

    skip_passbands = ['c', 'cfit', 'glob', 'h', 'integrate',
                      'interpolate', 'json', 'k_B', 'libphoebe', 'logger', 'logging',
                      'marshal', 'np', 'os', 'parse_json', 'shutil', 'sigma_sb',
                      'sys', 'types', 'u', 'urllib', 'urllib2',
                      'init_passband', 'init_passbands', 'Table',
                      'HTTPError', 'URLError', 'urlopen', 'urlretrieve', 'datetime']

    skip_parameters_type = ['deepcopy', 'download_passband', 'fnmatch',
                            'list_installed_passbands', 'list_online_passbands',
                            'list_passbands', 'parameter_from_json', 'parse_json',
                            'send_if_client', 'update_if_client']

    skip_parameters_compute = skip_parameters_type + ['phase_mask_inds', 'photodynam']
    skip_parameters_constraint = skip_parameters_type + ['keplers_third_law_hierarchical', 'etv', 'time_ephem', 'passband_ratio', 'ph_infconj', 'ph_perpass', 'ph_supconj', 'sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', 'arctan2', 'abs', 'sqrt', 'roche_requiv_L1', 'roche_requiv_contact_L1', 'roche_requiv_contact_L23', 'roche_potential_contact_L1', 'roche_potential_contact_L23', 'roche_pot_to_fillout_factor', 'roche_fillout_factor_to_pot', 'requiv_to_pot_contact', 'pot_to_requiv_contact', 'esinw2per0', 'ecosw2per0','esinw2ecc', 'ecosw2ecc', 't0_perpass_to_supconj', 't0_supconj_to_perpass', 't0_ref_to_supconj', 't0_supconj_to_ref', 'custom', 't0']
    skip_parameters_dataset = skip_parameters_type + ['etv']
    skip_parameters_figure = skip_parameters_type + ['common']
    skip_parameters_feature = skip_parameters_type + ['phase_mask_inds', 'pulsation']
    skip_parameters_hierarchy = skip_parameters_type + []
    skip_parameters_setting = skip_parameters_type + []
    skip_parameters_solver = skip_parameters_type + ['phase_mask_inds']
    skip_parameters_system = skip_parameters_type + []
    skip_parameters_server = skip_parameters_type + []

    skip_units = ['add_enabled_equivalencies', 'add_enabled_units', 'def_physical_type', 'def_unit']

    skip_distortions_roche = ['BinaryRoche', 'd2BinaryRochedx2', 'dBinaryRochedr',
                              'dBinaryRochedx', 'dBinaryRochedy', 'dBinaryRochedz',
                              'Lag1', 'sqrt', 'sin', 'cos', 'acos', 'atan2', 'trunc', 'pi']

    skip_distortions_rotstar = []

    skip_passband = ['save_asdf', 'save_pickle', 'save_fits', 'load_asdf', 'load_pickle', 'load_fits', 'compute_blended_response']

    fms_phoebe = api_docs(phoebe, skip=skip_phoebe, members=[pydoc.inspect.ismodule, pydoc.inspect.isfunction, pydoc.inspect.isclass])

    fms_frontend = api_docs(phoebe.frontend, skip=skip_frontend+fms_phoebe, prefix='phoebe', members=[pydoc.inspect.ismodule])
    fms_frontend_bundle = api_docs(phoebe.frontend.bundle, skip=skip_frontend_bundle+[s for s in fms_phoebe if s not in ['Bundle', 'RunChecksItem', 'RunChecksReport']], prefix='phoebe.frontend', members=[pydoc.inspect.isfunction, pydoc.inspect.isclass])
    fms_parameters = api_docs(phoebe.parameters, skip=skip_parameters+fms_phoebe, prefix='phoebe', members=[pydoc.inspect.ismodule, pydoc.inspect.isfunction, pydoc.inspect.isclass])
    fms_atm = api_docs(phoebe.atmospheres, skip=[], prefix='phoebe', members=[pydoc.inspect.ismodule])
    fms_passbands = api_docs(phoebe.atmospheres.passbands, skip=skip_passbands, prefix='phoebe.atmospheres', members=[pydoc.inspect.isfunction, pydoc.inspect.isclass])
    fms_helps = api_docs(phoebe.helpers, skip=[], prefix='phoebe', members=[pydoc.inspect.isfunction])

    # TODO: include dependencies (need to cleanup their docs, match in same format, pull in code)
    # fms_deps = api_docs(phoebe.dependencies, skip=['unitsiau2015'], prefix='phoebe', members=[pydoc.inspect.ismodule], write=False)
    # fms_autofig = api_docs(phoebe.dependencies.autofig, skip=[], prefix='phoebe.dependencies', members=[pydoc.inspect.isfunction, pydoc.inspect.isclass, pydoc.inspect.ismethod, pydoc.inspect.isdatadescriptor], write=False)
    # classes for Axes, Figure, Mesh, Plot
    # fms_nparray = api_docs(phoebe.dependencies.nparray, skip=['LooseVersion', 'monkeypatch', 'np', 'os', 'version'], prefix='phoebe.dependencies', members=[pydoc.inspect.ismodule, pydoc.inspect.isfunction, pydoc.inspect.isclass, pydoc.inspect.ismethod, pydoc.inspect.isdatadescriptor], write=False)
    # fms_nparray_nparray = api_docs(phoebe.dependencies.nparray.nparray, skip=['OrderedDict'], prefix='phoebe.dependencies', members=[pydoc.inspect.isclass], write=False)
    # classes for Arange, Array, ArrayWrapper, Eye, Full, Geomspace, Linspace, Logspace, Ones, Zeros

    fms_component = api_docs(phoebe.parameters.component, skip=skip_parameters_type, prefix='phoebe.parameters')
    fms_compute = api_docs(phoebe.parameters.compute, skip=skip_parameters_compute, prefix='phoebe.parameters')
    fms_compute = api_docs(phoebe.parameters.solver, skip=skip_parameters_solver, members=[pydoc.inspect.ismodule], prefix='phoebe.parameters')
    fms_compute = api_docs(phoebe.parameters.solver.estimator, skip=skip_parameters_solver, prefix='phoebe.parameters.solver')
    fms_compute = api_docs(phoebe.parameters.solver.optimizer, skip=skip_parameters_solver, prefix='phoebe.parameters.solver')
    fms_compute = api_docs(phoebe.parameters.solver.sampler, skip=skip_parameters_solver, prefix='phoebe.parameters.solver')
    fms_compute = api_docs(phoebe.parameters.figure, skip=skip_parameters_figure, members=[pydoc.inspect.ismodule], prefix='phoebe.parameters')
    fms_compute = api_docs(phoebe.parameters.figure.dataset, skip=skip_parameters_figure, prefix='phoebe.parameters.figure')
    fms_compute = api_docs(phoebe.parameters.figure.distribution, skip=skip_parameters_figure, prefix='phoebe.parameters.figure')
    fms_compute = api_docs(phoebe.parameters.figure.solution, skip=skip_parameters_figure, prefix='phoebe.parameters.figure')
    fms_constraint = api_docs(phoebe.parameters.constraint, skip=skip_parameters_constraint, prefix='phoebe.parameters')
    fms_dataset = api_docs(phoebe.parameters.dataset, skip=skip_parameters_dataset, prefix='phoebe.parameters')
    fms_feature = api_docs(phoebe.parameters.feature, skip=skip_parameters_feature, prefix='phoebe.parameters')
    fms_hierarchy = api_docs(phoebe.parameters.hierarchy, skip=skip_parameters_hierarchy, prefix='phoebe.parameters')
    fms_setting = api_docs(phoebe.parameters.setting, skip=skip_parameters_setting, prefix='phoebe.parameters')
    fms_system = api_docs(phoebe.parameters.system, skip=skip_parameters_system, prefix='phoebe.parameters')
    fms_system = api_docs(phoebe.parameters.server, skip=skip_parameters_server, prefix='phoebe.parameters')

    fms_ps = api_docs(phoebe.parameters.ParameterSet, skip=skip_ps, prefix='phoebe.parameters')
    fms_rci = api_docs(phoebe.frontend.bundle.RunChecksItem, skip=['__init__'], prefix='phoebe.frontend.bundle')
    fms_rcr = api_docs(phoebe.frontend.bundle.RunChecksReport, skip=['__init__'], prefix='phoebe.frontend.bundle')
    fms_bundle = api_docs(phoebe.frontend.bundle.Bundle, skip=skip_ps+[s for s in fms_ps if s not in ['__init__', 'open', 'load']], subclass_of='phoebe.parameters.ParameterSet', prefix='phoebe.frontend.bundle')

    fms_param = api_docs(phoebe.parameters.Parameter, skip=skip_param+['get_value'], prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.IntParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.BoolParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.StringParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.ChoiceParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.SelectParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.ConstraintParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.DistributionParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.DictParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.HierarchyParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms_float_param = api_docs(phoebe.parameters.FloatParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.FloatArrayParameter, skip=skip_param+fms_param+fms_float_param, subclass_of='phoebe.parameters.FloatParameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.UnitParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.JobParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')

    fms = api_docs(phoebe.atmospheres.passbands.Passband, skip=skip_passband, prefix='phoebe.atmospheres.passbands')

    fms = api_docs(phoebe.distortions, prefix='phoebe', members=[pydoc.inspect.ismodule])
    fms = api_docs(phoebe.distortions.roche, skip=skip_distortions_roche, prefix='phoebe.distortions', members=[pydoc.inspect.isfunction])
    fms = api_docs(phoebe.distortions.rotstar, skip=skip_distortions_rotstar, prefix='phoebe.distortions', members=[pydoc.inspect.isfunction])
