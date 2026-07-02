#!/usr/bin/env python
# coding: utf-8

# Advanced: Detaching from Run Compute
# ============================
# 
# Although experimental support for `detach` still exists, in PHOEBE 2.4+, it is preferred to use [b.export_compute](../api/phoebe.frontend.bundle.Bundle.export_compute.md) or [b.as_client](../api/phoebe.frontend.bundle.Bundle.as_client.md) to manage running scripts outside the main thread.
