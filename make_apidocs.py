import pydoc
import os, sys
# import re

def api_docs(item, skip=[], prefix='', subclass_of=None, write=True, members=[pydoc.inspect.ismethod, pydoc.inspect.isfunction]):
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
        output.append("### {}.{}\n".format(path_md, fm[0]))

        # Get the signature
        output.append ('```py\n')
        output.append('def %s%s\n' % (fm[0], pydoc.inspect.formatargspec(*pydoc.inspect.getargspec(fm[1]))))
        output.append ('```\n')

        # get the docstring
        if pydoc.inspect.getdoc(fm[1]):
            output.append('\n')
            docstring = pydoc.HTMLDoc().markup(pydoc.inspect.getdoc(fm[1]))
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
        kind = 'class' if pydoc.inspect.isclass(item) else 'module' if pydoc.inspect.ismodule(item) else ''
        f_class.write("## {} {} (all public {})\n\n".format(path_md, kind, 'members'))
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
               'undo', 'redo', 'get_history', 'enable_history', 'disable_history']

    skip_param = ['set_uniqueid']

    skip_phoebe = ['default_triple', 'devel_off', 'devel_on']
    skip_frontend = ['io', 'tabcomplete']

    skip_frontend_bundle = ['ArrayParameter',
                            'BaseNamespace', 'BoolParameter', 'ChoiceParameter',
                            'ConstraintParameter', 'DictParameter',
                            'FloatArrayParameter', 'FloatParameter',
                            'HierarchyParameter', 'HistoryParameter',
                            'IntArrayParameter', 'IntParameter',
                            'JobParameter', 'OrderedDict', 'Parameter',
                            'ParameterSet', 'SelectParameter', 'SocketIO',
                            'StrictVersion', 'StringParameter', 'TwigParameter',
                            'datetime', 'deepcopy', 'fnmatch',
                            'parameter_from_json', 'parse_json', 'send_if_client',
                            'update_if_client', 'ConstraintVar']

    skip_parameters = ['deepcopy', 'fnmatch', 'send_if_client', 'update_if_client']
    skip_units = ['add_enabled_equivalencies', 'add_enabled_units', 'def_physical_type', 'def_unit']


    fms_phoebe = api_docs(phoebe, skip=skip_phoebe)
    fms_frontend = api_docs(phoebe.frontend, skip=skip_frontend+fms_phoebe, prefix='phoebe', members=[pydoc.inspect.ismodule])
    fms_frontend_bundle = api_docs(phoebe.frontend.bundle, skip=skip_frontend_bundle+fms_phoebe, prefix='phoebe.frontend', members=[pydoc.inspect.isfunction, pydoc.inspect.isclass])
    fms_parameters = api_docs(phoebe.parameters, skip=skip_parameters+fms_phoebe, prefix='phoebe')

    fms_ps = api_docs(phoebe.parameters.ParameterSet, skip=skip_ps, prefix='phoebe.parameters')
    fms_bundle = api_docs(phoebe.Bundle, skip=skip_ps+fms_ps, subclass_of='phoebe.parameters.ParameterSet', prefix='phoebe.frontend')

    fms_param = api_docs(phoebe.parameters.Parameter, skip=skip_param, prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.IntParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.BoolParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.StringParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.ChoiceParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.SelectParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.ConstraintParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms_float_param = api_docs(phoebe.parameters.FloatParameter, skip=skip_param+fms_param, subclass_of='phoebe.parameters.Parameter', prefix='phoebe.parameters')
    fms = api_docs(phoebe.parameters.FloatArrayParameter, skip=skip_param+fms_param+fms_float_param, subclass_of='phoebe.parameters.FloatParameter', prefix='phoebe.parameters')
