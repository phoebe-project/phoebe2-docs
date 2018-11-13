### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[constraint](phoebe.parameters.constraint.md).custom

```py

def custom(b, *args, **kwargs)

```



[NOT IMPLEMENTED]

args can be
- 2 ConstraintParameters (or parameters which need param.to_constraint()) (lhs, rhs)
- 2 parsable strings (lhs, rhs)
- single parsable string (lhs, rhs = args[0].split('=')

:raise NotImplementedError: because it isn't

