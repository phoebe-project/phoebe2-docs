### flip\_constraint
```py

def flip_constraint(self, twig=None, solve_for=None, **kwargs)

```



Flip an existing constraint to solve for a different parameter

:parameter str twig: twig to filter the constraint
:parameter solve_for: twig or actual parameter object of the new
    parameter which this constraint should constraint (solve for).
:type solve_for: str or :class:`phoebe.parameters.parameters.Parameter
:parameter **kwargs: any other tags to do the filter
    (except twig or context)

