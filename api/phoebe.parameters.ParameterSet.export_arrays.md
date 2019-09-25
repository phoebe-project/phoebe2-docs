### [phoebe](phoebe.md).[parameters](phoebe.parameters.md).[ParameterSet](phoebe.parameters.ParameterSet.md).export_arrays (method)


```py

def export_arrays(self, fname, delimiter=' ', newline='\n', header='', footer='', comments='# ', encoding=None, **kwargs)

```



        Export arrays from [phoebe.parameters.Parameter.FloatArrayParameter](phoebe.parameters.Parameter.FloatArrayParameter.md)
        parameters to a file via `np.savetxt`.

        NEW IN PHOEBE 2.2

        Each parameter will have its array values as a column in the output
        file in a format that can be reloaded manually with `np.loadtxt`.

        Note: all parameters must be FloatArrayParameters and have the same
        shape.


        Arguments
        ------------
        `fname` (string or file object): passed to np.savetxt.
            If the filename ends in .gz, the file is automatically saved in
            compressed gzip format. loadtxt understands gzipped files
            transparently.
        `delimiter` (string, optional, default=' '): passed to np.savetxt.
            String or character separating columns.
        `newline` (string, optional, default='
'): passed to np.savetxt.
            String or character separating lines.
        `header` (string, optional): The header will automatically be appended
            with the twigs of the parameters making up the columns and then
            passed to np.savetxt.
            String that will be written at the beginning of the file.
        `footer` (string, optional): passed to np.savetxt.
            String that will be written at the end of the file.
        `comments` (string, optional, default='#'): passed to np.savetxt.
            String that will be prepended to the `header` and `footer` strings,
            to mark them as comments.
        `encoding` (None or string, optional, default=None): passed to np.savetxt.
            Encoding used to encode the outputfile. Does not apply to output
            streams. If the encoding is something other than ‘bytes’ or ‘latin1’
            you will not be able to load the file in NumPy versions &lt; 1.14.
            Default is ‘latin1’.
        `**kwargs`: all additional keyword arguments will be sent to
            [phoebe.parameters.ParameterSet.filter](phoebe.parameters.ParameterSet.filter.md).  The filter must result
            in all [phoebe.parameters.Parameter.FloatArrayParameter](phoebe.parameters.Parameter.FloatArrayParameter.md) objects
            with the same length, otherwise an error will be raised.


        Returns
        -----------
        * (string or file object) `fname`

        Raises
        -----------
        * TypeError: if not all parameters are of type
            [phoebe.parameters.Parameter.FloatArrayParameter](phoebe.parameters.Parameter.FloatArrayParameter.md) or no parameters
            are included in the filter.
        

