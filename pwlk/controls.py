from rich.table import Table
from rich.console import Console
from rich.rule import Rule
from rich import print, inspect

import platform
import sys
import argparse

class Parser():
    def __init__(self, 
            formatter_class = argparse.RawDescriptionHelpFormatter, 
            description: str = 'Program & parsing options description', 
            epilog: str = f'Author : Pawlicki Loïc\n{'─'*30}\n'):
        '''__init__ Parsing object for improved parsing follow-up with internal 
                    parser object init depending on instance args

        Args:
            formatter_class (_type_, optional): formatter class from argparse module for parsing help format. Defaults to argparse.RawDescriptionHelpFormatter.
            description (str, optional): parsing help description. Defaults to 'Program & parsing options description'.
            epilog (_type_, optional): parsing help footer. Defaults to f'Author : Pawlicki Loïc\n{'─'*30}\n'.
        '''
        self.formatter_class = formatter_class
        self.description = description
        self.epilog = epilog
        self.parser = argparse.ArgumentParser(
                formatter_class = argparse.RawDescriptionHelpFormatter, 
                description = 'Program & parsing options description', 
                epilog = f'Author : Pawlicki Loïc\n{'─'*30}\n'
            )
        
    def add_arg(self,
                flag: str = '-d', 
                name: str = '--default_name', 
                default = 0, 
                metavar: str = '', 
                action: str = 'store', 
                help: str = 'help_text',
                *args):
        '''add_arg : Bypass method for the argparse.ArgumentParser().add_argument() method, includes additionnal arguments.
        
        Args:
            flag (str, optional): Argname shortcut for command line. Defaults to '-d'.
            name (str, optional): Argument variable name for access using ParserObject.name after calling get_args method. Defaults to '--default_name'.
            default (int, optional): Default value if no argument is provided. Defaults to 0 (int).
            metavar (str, optional): More infos on metavar on argparse module documentation. Defaults to ''.
            action (str, optional): See available actions on argparse module documentation. Defaults to 'store'.
            help (str, optional): Help text for argparse helper generator. Defaults to 'help_text'.
        '''
        self.parser.add_argument(flag, name, default=default, type=type(default), metavar=metavar, action=action, help=help, *args)

    def get_args(self, verbose: bool=True, return_table: bool=True, return_parser: bool=False):
        
        # > Parsing the object to store user args
        args = self.parser.parse_args()
        
        if return_table:
            
            # > Defining an argtable to display argname, associated flag, default and arg dtype
            argtable = Table(title = 'Parsed arguments ref. table', title_justify = 'left', padding = (0,2))
            argtable.add_column(header = 'Argument', style = 'italic', justify='center')
            argtable.add_column(header = 'Flag', style = 'bold', justify='center')
            argtable.add_column(header = 'Value', style = 'yellow', justify='left')
            argtable.add_column(header = 'Dtype', style = 'blue', justify='center')
            
            # > One-liner : adding a row for each given item(s) (Namespace parsing result)
            for arg in vars(args): argtable.add_row(f'--{arg}' , f'-{arg[:1]}' , f'{getattr(args, arg)}' , f'{getattr(args, arg).__class__.__name__}')
            if verbose: 
                console.print(argtable)     
            return args, argtable
        
        elif return_parser:
            return args, parser
        else:
            return args
            

def header(console: Console = Console()) -> Table:
    console.print(Rule(style = 'white'))
    header = Table(title='> Python script execution init ...', 
                   title_justify = 'left', 
                   border_style='white', 
                   min_width = 70, 
                   expand=True)
    header.add_column('Variable', style='yellow', header_style='bold yellow')
    header.add_column('Variable states', style='italic yellow', header_style='bold yellow')
    header.add_row('node.os',   f'{platform.uname().system}')
    header.add_row('node.name', f'{platform.uname().node}')
    header.add_row('sys.argv',  f'{repr(sys.argv)}')
    header.add_row('sys.path',  f'{sys.path[0]}')
    console.print(header)
    return header


if __name__ == '__main__':
    
    # inspect(argparse.ArgumentParser, methods=1)
    parser = argparse.ArgumentParser(formatter_class = argparse.RawDescriptionHelpFormatter, 
        description = 'Program & parsing options description', epilog = f'Author : Pawlicki Loïc\n{'─'*30}\n')
    
    parser.add_argument('-f', '--flag_attr', default = 0,   type = int, metavar = '', action= 'store',  help = 'help_text')
    
    console = Console()
    header = header(console)
    args, argtable, parser = GetArgs(parser, console)
print([arg for arg in vars(args)])