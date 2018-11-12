### Bundle.run_constraint

```py

def run_constraint(self, twig=None, return_parameter=False, **kwargs)

```



Run a given 'constraint' now and set the value of the constrained
parameter.  In general, there shouldn't be any need to manually
call this - constraints should automatically be run whenever a
dependent parameter's value is change.

:parameter str twig: twig to filter for the constraint
:parameter **kwargs: any other tags to do the filter
    (except twig or context)
:return: the resulting value of the constraint
:rtype: float or units.Quantity

