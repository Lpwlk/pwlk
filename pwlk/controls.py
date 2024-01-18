from rich.table import Table
import argparse

def GetArgs(get_objects: bool = False, argtable: bool = True):

    '''GetArgs _summary_

    Args:
        get_objects (bool, optional): _description_. Defaults to False.
        argtable (bool, optional): _description_. Defaults to True.

    Returns:
        _type_: _description_
    '''
    # ? Edit this sub-routine as an arg type to parse multiple values at once using csv syntax
    # def intlist(arg): return list(map(int, arg.split(',')))
    
    parser = argparse.ArgumentParser(
        formatter_class = argparse.RawDescriptionHelpFormatter,
        epilog = 'Author : Pawlicki Loïc\n' + '─'*30 + '\n'
    )
    
    parser.add_argument('-flag', '--lflag_attr', default = 0,   type = int, metavar = '', action= 'store',  help = 'help_text')
    args = parser.parse_args()
    argtable = Table(title = 'Parsed arguments ref. table', title_justify = 'left', padding = (0,2))
    argtable.add_column(header = 'Argument', style = 'italic', justify='center')
    argtable.add_column(header = 'Flag', style = 'bold', justify='center')
    argtable.add_column(header = 'Default value', style = 'yellow', justify='left')
    argtable.add_column(header = 'Dtype', style = 'blue', justify='center')
    for arg in vars(args): argtable.add_row(f'--{arg}', f'-{arg[:1]}', f'{getattr(args, arg)}', f'{getattr(args, arg).__class__.__name__}')
    print(argtable)
    if get_objects:
        return args, argtable, parser
    else: 
        return args

if __name__ == '__main__':
    
    args, argtable, parser = GetArgs()
    args.print_help()