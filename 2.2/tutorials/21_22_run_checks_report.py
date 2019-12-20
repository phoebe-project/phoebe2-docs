#!/usr/bin/env python
# coding: utf-8

# 2.1 - 2.2 Migration: run_checks
# ==============================

# PHOEBE 2.2 includes a more flexible output to [b.run_checks](../api/phoebe.frontend.bundle.Bundle.run_checks.md).
# 
# In PHOEBE 2.1, run_checks returned a boolean and a warning or error message.  Whenever the first error was reached, run_checks would immediately return `False` along with that first message.  Although this saved a bit of time, it often resulted in confusion as it was impossible to expose additional errors until fixing the first one.
# 
# Now, a [RunChecksReport](../api/phoebe.frontend.bundle.RunChecksReport.md) object is returned.  This object has a `.passed` attribute which can be used in the same way as the boolean returned in 2.1.  Additionally, if you print the returned object, you'll see a full list of all errors/warnings.
# 
# If any of your scripts had something like the following:
# 
# ```
# passed, message = b.run_checks()
# ```
# 
# you'll need to replace that with something like:
# 
# ```
# report = b.run_checks()
# passed = report.passed
# messages = [item.message for item in report.items]
# ```
