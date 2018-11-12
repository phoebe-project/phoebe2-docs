import pydoc
import os, sys
# import re

def api_docs_for_class(cls, skip=[], subclass_of=None, write=True):
    stored_funcs = []
    for func in pydoc.inspect.getmembers(cls, pydoc.inspect.ismethod):
        output = list()

        if func[0] in skip or (func[0].startswith('_') and func[0] != '__init__'):
            continue

        output.append("### {}.{}\n".format(cls.__name__, func[0]))

        # Get the signature
        output.append ('```py\n')
        output.append('def %s%s\n' % (func[0], pydoc.inspect.formatargspec(*pydoc.inspect.getargspec(func[1]))))
        output.append ('```\n')

        # get the docstring
        if pydoc.inspect.getdoc(func[1]):
            output.append('\n')
            docstring = pydoc.HTMLDoc().markup(pydoc.inspect.getdoc(func[1]))
            output.append(docstring)

        output.append('\n')


        stored_funcs.append(func[0])

        if write:
            filename = './api/{}.{}.md'.format(cls.__name__, func[0])
            print("writing {}".format(filename))
            f_method = open(filename, 'w')
            f_method.write("\n".join(output))
            f_method.close()

    if write:
        filename_class = './api/{}.md'.format(cls.__name__)
        print("writing {}".format(filename_class))
        f_class = open(filename_class, 'w')
        f_class.write("## {} class (all public methods)\n\n".format(cls.__name__))
        if subclass_of is not None:
            f_class.write("{} is a subclass of {} and therefore also includes all [{} methods]({}.md)\n\n".format(cls.__name__, subclass_of, subclass_of, subclass_of))
        for func in stored_funcs:
            f_class.write("* [{}]({}.{})\n".format(func, cls.__name__, func))
        f_class.close()

    return stored_funcs


if __name__ == '__main__':
    import phoebe

    print("CREATING API DOCS FOR PHOEBE {}".format(phoebe.__version__))

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



    # funcs_ps = api_docs_for_class(phoebe.parameters.ParameterSet, skip=skip_ps)
    # funcs_bundle = api_docs_for_class(phoebe.Bundle, skip=skip_ps+funcs_ps, subclass_of='ParameterSet')
    #
    # funcs_param = api_docs_for_class(phoebe.parameters.Parameter, skip=skip_param)
    # funcs = api_docs_for_class(phoebe.parameters.IntParameter, skip=skip_param+funcs_param, subclass_of='Parameter')
    # funcs = api_docs_for_class(phoebe.parameters.BoolParameter, skip=skip_param+funcs_param, subclass_of='Parameter')
    # funcs = api_docs_for_class(phoebe.parameters.StringParameter, skip=skip_param+funcs_param, subclass_of='Parameter')
    # funcs = api_docs_for_class(phoebe.parameters.ChoiceParameter, skip=skip_param+funcs_param, subclass_of='Parameter')
    # funcs = api_docs_for_class(phoebe.parameters.SelectParameter, skip=skip_param+funcs_param, subclass_of='Parameter')
    # funcs_float_param = api_docs_for_class(phoebe.parameters.FloatParameter, skip=skip_param+funcs_param, subclass_of='Parameter')
    # funcs = api_docs_for_class(phoebe.parameters.FloatArrayParameter, skip=skip_param+funcs_param+funcs_float_param, subclass_of='FloatParameter')

    funcs_phoebe = api_docs_for_class(phoebe, skip=[], write=False)
    print funcs_phoebe
