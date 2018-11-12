### [Bundle](Bundle.md).disable_dataset

```py

def disable_dataset(self, dataset=None, **kwargs)

```



Disable a 'dataset'.  Datasets that are enabled will be computed
during :meth:`run_compute` and included in the cost function
during :meth:`run_fitting`.

If compute is not provided, the dataset will be disabled across all
compute options.

:parameter str dataset: name of the dataset
:parameter **kwargs: any other tags to do the filter
    (except dataset or context)
:return: :class:`phoebe.parameters.parameters.ParameterSet`
    of the disabled dataset

