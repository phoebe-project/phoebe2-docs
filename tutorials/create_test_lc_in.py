import phoebe
import numpy as np

b = phoebe.default_binary()
times=b.to_time(np.linspace(0,1,101))
b.add_dataset('lc', times=times)

b.run_compute()

fluxes = b.get_value('fluxes@model')

f = open('test.lc.in', 'w')
for t, fl in zip(times, fluxes):
    f.write('{} {} {}\n'.format(t, fl, 0.1))

f.close()
