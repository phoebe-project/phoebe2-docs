### [phoebe](phoebe.md).[frontend](frontend.md).[Bundle](Bundle.md).enable_dataset

```py

def enable_dataset(self, dataset=None, **kwargs)

```



Enable a 'dataset'.  Datasets that are enabled will be computed
during :meth:`run_compute` and included in the cost function
during :meth:`run_fitting`.

If compute is not provided, the dataset will be enabled across all
compute options.

:parameter str dataset: name of the dataset
:parameter **kwargs: any other tags to do the filter
    (except dataset or context)
:return: :class:`phoebe.parameters.parameters.ParameterSet`
    of the enabled dataset

