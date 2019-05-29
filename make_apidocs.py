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

    skip_ps = ['add_feedback', 'add_fitting', 'add_plugin', 'add_prior',
               'as_client', 'client_update', 'default_triple',
               'disable_prior', 'draw_from_posterior', 'draw_from_prior',
               'enable_prior', 'from_catalog', 'from_server', 'get_adjust',
               'get_feedback', 'get_fitting', 'get_plotting', 'get_plugin',
               'get_posterior', 'get_prior', 'remove_feedback', 'remove_fitting',
               'remove_history',
               'remove_plugin', 'remove_posterior', 'remove_prior',
               'run_fitting', 'run_plugin',
               'set_adjust', 'set_adjust_all', 'set_meta',
               'set_prior', 'ui', 'get_plotting_info',
               'undo', 'redo', 'get_history', 'enable_history', 'disable_history',
               'feedback', 'feedbacks', 'fitting', 'fittings', 'history', 'historys',
               'plugin', 'plugins', 'is_client']

    skip_param = ['set_uniqueid', 'feedback', 'fitting', 'history']

    skip_phoebe = ['default_triple', 'devel_off', 'devel_on',
                   'algorithms', 'backend', 'c',
                   'component', 'compute', 'constraint', 'constraints',
                   'dataset', 'dependencies', 'distortions', 'dynamics',
                   'hierarchy', 'libphoebe', 'u', 'utils', 'Bundle']

    skip_frontend = ['io', 'tabcomplete']

    skip_frontend_bundle = ['ArrayParameter',
                            'BaseNamespace', 'BoolParameter', 'ChoiceParameter',
                            'ConstraintParameter', 'DictParameter',
                            'FloatArrayParameter', 'FloatParameter',
                            'HierarchyParameter', 'HistoryParameter',
                            'IntArrayParameter', 'IntParameter',
                            'JobParameter',
                            'OrderedDict', 'Parameter',
                            'ParameterSet', 'SelectParameter', 'SocketIO',
                            'StrictVersion', 'StringParameter', 'TwigParameter',
                            'datetime', 'deepcopy', 'fnmatch',
                            'parameter_from_json', 'parse_json', 'send_if_client',
                            'update_if_client', 'ConstraintVar', 'cfit']

    skip_parameters = ['deepcopy', 'fnmatch', 'send_if_client', 'update_if_client',
                       'ConstraintVar', 'DictParameter',
                       'IntArrayParameter', 'TwigParameter', 'autofig', 'datetime',
                       'difflib', 'functools', 'itertools', 'json', 'logging',
                       'np', 'nparray', 'os', 'parameter_from_json', 'parse_json',
                       'random', 're', 'readline', 'requests', 'string', 'sympy',
                       'sys', 'tabcomplete', 'time', 'twighelpers', 'types', 'u',
                       'json', 'ujson', 'webbrowser', 'OrderedDict']

    skip_passbands = ['Inorm_bol_bb', 'c', 'cfit', 'glob', 'h', 'integrate',
                      'interpolate', 'json', 'k_B', 'libphoebe', 'logger', 'logging',
                      'marshal', 'np', 'os', 'parse_json', 'shutil', 'sigma_sb',
                      'sys', 'types', 'u', 'urllib', 'urllib2',
                      'init_passband', 'init_passbands',
                      'HTTPError', 'URLError', 'urlopen', 'urlretrieve', 'datetime']

    skip_parameters_type = ['deepcopy', 'download_passband', 'fnmatch',
                            'list_installed_passbands', 'list_online_passbands',
                            'list_passbands', 'parameter_from_json', 'parse_json',
                            'send_if_client', 'update_if_client']

    skip_parameters_compute = skip_parameters_type #+ ['jktebop', 'photodynam']
    skip_parameters_constraint = skip_parameters_type + ['keplers_third_law_hierarchical', 'etv', 'time_ephem', 'passband_ratio', 'ph_infconj', 'ph_perpass', 'ph_supconj', 'sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan', 'arctan2', 'abs', 'sqrt', 'roche_requiv_L1', 'roche_requiv_contact_L1', 'roche_requiv_contact_L23', 'roche_potential_contact_L1', 'roche_potential_contact_L23', 'roche_pot_to_fillout_factor', 'roche_fillout_factor_to_pot', 'requiv_to_pot_contact', 'pot_to_requiv_contact', 'esinw2per0', 'ecosw2per0', 't0_perpass_to_supconj', 't0_supconj_to_perpass', 't0_ref_to_supconj', 't0_supconj_to_ref', 'custom', 't0', 'teffratio']
    skip_parameters_dataset = skip_parameters_type + ['etv', 'etv_dep', 'etv_syn', 'lc_dep', 'lc_syn', 'lp_dep', 'lp_syn', 'mesh_dep', 'mesh_syn', 'orb_dep', 'orb_syn', 'rv_dep', 'rv_syn']
    skip_parameters_feature = skip_parameters_type + ['pulsation']
    skip_parameters_hierarchy = skip_parameters_type + []
    skip_parameters_setting = skip_parameters_type + []
    skip_parameters_system = skip_parameters_type + []

    skip_units = ['add_enabled_equivalencies', 'add_enabled_units', 'def_physical_type', 'def_unit']

    skip_passband = []

    fms_phoebe = api_docs(phoebe, skip=skip_phoebe, members=[pydoc.inspect.ismodule, pydoc.inspect.isfunction, pydoc.inspect.isclass])

    fms_frontend = api_docs(phoebe.frontend, skip=skip_frontend+fms_phoebe, prefix='phoebe', members=[pydoc.inspect.ismodule])
    fms_frontend_bundle = api_docs(phoebe.frontend.bundle, skip=skip_frontend_bundle+[s for s in fms_phoebe if s!='Bundle'], prefix='phoebe.frontend', members=[pydoc.inspect.isfunction, pydoc.inspect.isclass])
    fms_parameters = api_docs(phoebe.parameters, skip=skip_parameters+fms_phoebe, prefix='phoebe', members=[pydoc.inspect.ismodule, pydoc.inspect.isfunction, pydoc.inspect.isclass])
    fms_atm = api_docs(phoebe.atmospheres, skip=[], prefix='phoebe', members=[pydoc.inspect.ismodule])
    fms_passbands = api_docs(phoebe.atmospheres.passbands, skip=skip_passbands, prefix='phoebe.atmospheres', members=[pydoc.inspect.isfunction, pydoc.inspect.isclass])

    # TODO: include dependencies (need to cleanup their docs, match in same format, pull in code)
    # fms_deps = api_docs(phoebe.dependencies, skip=['unitsiau2015'], prefix='phoebe', members=[pydoc.inspect.ismodule], write=False)
    # fms_autofig = api_docs(phoebe.dependencies.autofig, skip=[], prefix='phoebe.dependencies', members=[pydoc.inspect.isfunction, pydoc.inspect.isclass, pydoc.inspect.ismethod, pydoc.inspect.isdatadescriptor], write=False)
    # classes for Axes, Figure, Mesh, Plot
    # fms_nparray = api_docs(phoebe.dependencies.nparray, skip=['LooseVersion', 'monkeypatch', 'np', 'os', 'version'], prefix='phoebe.dependencies', members=[pydoc.inspect.ismodule, pydoc.inspect.isfunction, pydoc.inspect.isclass, pydoc.inspect.ismethod, pydoc.inspect.isdatadescriptor], write=False)
    # fms_nparray_nparray = api_docs(phoebe.dependencies.nparray.nparray, skip=['OrderedDict'], prefix='phoebe.dependencies', members=[pydoc.inspect.isclass], write=False)
    # classes for Arange, Array, ArrayWrapper, Eye, Full, Geomspace, Linspace, Logspace, Ones, Zeros

    fms_component = api_docs(phoebe.parameters.component, skip=skip_parameters_type, prefix='phoebe.parameters')
    fms_compute = api_docs(phoebe.parameters.compute, skip=skip_parameters_compute, prefix='phoebe.parameters')
    fms_constraint = api_docs(phoebe.parameters.constraint, skip=skip_parameters_constraint, prefix='phoebe.parameters')
    fms_dataset = api_docs(phoebe.parameters.dataset, skip=skip_parameters_dataset, prefix='phoebe.parameters')
    fms_feature = api_docs(phoebe.parameters.feature, skip=skip_parameters_feature, prefix='phoebe.parameters')
    fms_hierarchy = api_docs(phoebe.parameters.hierarchy, skip=skip_parameters_hierarchy, prefix='phoebe.parameters')
    fms_setting = api_docs(phoebe.parameters.setting, skip=skip_parameters_setting, prefix='phoebe.parameters')
    fms_system = api_docs(phoebe.parameters.system, skip=skip_parameters_system, prefix='phoebe.parameters')

    fms_ps = api_docs(phoebe.parameters.ParameterSet, skip=skip_ps, prefix='phoebe.parameters')
    fms_bundle = api_docs(phoebe.frontend.bundle.Bundle, skip=skip_ps+[s for s in fms_ps if s not in ['__init__', 'open', 'load']], subclass_of='phoebe.parameters.ParameterSet', prefix='phoebe.frontend.bundle')

    fms_param = api_docs(phoebe.parameters.Parameter, skip=skip_param+['get_value'], prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.IntParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.BoolParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.StringParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.ChoiceParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.SelectParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.ConstraintParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.HierarchyParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms_float_param = api_docs(phoebe.parameters.FloatParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.FloatArrayParameter, skip=skip_param+fms_param+fms_float_param, subclass_of='phoebe.parameters.FloatParameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.JobParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')

    fms = api_docs(phoebe.atmospheres.passbands.Passband, skip=skip_passband, prefix='phoebe.atmospheres.passbands')
