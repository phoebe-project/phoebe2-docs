### [phoebe](phoebe.md).[helpers](phoebe.helpers.md).process_acf_from_solution (function)


```py

def process_acf_from_solution(b, solution, nlags=None, burnin=None, lnprob_cutoff=None, adopt_parameters=None)

```



Compute the autocorrelation function from an emcee solution.

See also:
* [phoebe.helpers.process_acf](phoebe.helpers.process_acf.md)
* [phoebe.helpers.acf](phoebe.helpers.acf.md)
* [phoebe.helpers.acf_ci_bartlett](phoebe.helpers.acf_ci_bartlett.md)
* [phoebe.helpers.acf_ci](phoebe.helpers.acf_ci.md)

Arguments
--------------
* `b` ([phoebe.frontend.bundle.Bundle](phoebe.frontend.bundle.Bundle.md)): the Bundle
* `solution` (string): solution label
* `nlags` (int, optional, default=None): If not None, will override the
    value in the solution.
* `burnin` (int, optional, default=None): If not None, will override
    the value in the solution.
* `lnprob_cutoff` (float, optional, default=None): If not None, will override
    the value in the solution.
* `adopt_parameters` (list, optional, default=None): If not None, will
    override the value in the solution.

Returns
------------
* (dictionary, dictionary, float) dictionary with keys being the parameter twigs
    (or 'lnprobabilities') and values being the output of [phoebe.helpers.acf](phoebe.helpers.acf.md)
    (array with shape (nwalkers, nlags)), dictionary with keys being the
    parameter twigs (or 'lnprobabilities') and values being the output
    of [phoebe.helpers.acf_ci_bartlett](phoebe.helpers.acf_ci_bartlett.md), and float being the
    confidence intervale from [phoebe.helpers.acf_ci](phoebe.helpers.acf_ci.md).

