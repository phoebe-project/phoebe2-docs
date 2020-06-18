### [phoebe](phoebe.md).[frontend](phoebe.frontend.md).[bundle](phoebe.frontend.bundle.md).[RunChecksReport](phoebe.frontend.bundle.RunChecksReport.md).get_items (function)


```py

def get_items(self, fail=None)

```



Access the underlying [phoebe.frontend.bundle.RunChecksItem](phoebe.frontend.bundle.RunChecksItem.md) items,
with optional ability to filter by the `fail` argument of each item.

See also:
* [phoebe.frontend.bundle.RunChecksReport.items](phoebe.frontend.bundle.RunChecksReport.items.md)

Arguments
----------
* `fail` (bool or None, optional, default=None): filter for items
    with a particular value for `fail` or None to return all.
    See [phoebe.frontend.bundle.RunChecksItem.fail](phoebe.frontend.bundle.RunChecksItem.fail.md).

Returns
---------
* (list) list of [phoebe.frontend.bundle.RunChecksItem](phoebe.frontend.bundle.RunChecksItem.md) objects.

