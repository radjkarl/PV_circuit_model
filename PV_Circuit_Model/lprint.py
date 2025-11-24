import inspect

separator = "| "
def lprint(*args):
    """
    drop-in replacement for print()
    creating clickable log prints
    """
    frame,filename,line_number,function_name,lines,index = inspect.stack()[1]
    print('File "{}", line {}, in {} {}'.format(filename, line_number,function_name, separator), *args)