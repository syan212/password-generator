import secrets

from rich import print as rprint
from rich.console import Console

console = Console()

default_chars = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890-=[];\'#,./!"$%^&*()_+{}:@~<>?'


def generate_password(length: int, chars: list[str]) -> str:
    result = ''
    for _ in range(length):
        result += secrets.choice(chars)
    return result


length = console.input('[green]Enter length of password: [/]')
try:
    length = int(length)
except ValueError:
    rprint('[red]Error: length not a valid integer. Defaulting to 20.[/]')
    length = 20

use_default_chars = console.input('[green]Use default characters? ([/][light_green]y[/]/[red]n[/][green])[/] ').lower()

chars = (
    list(default_chars) if use_default_chars == 'y' else 
    list(console.input('[green]Enter custom characters: [/]')) if use_default_chars == 'n' else
    []
)

if not chars:
    rprint('Invalid option or no characters entered. Using default characters.')
    chars = list(default_chars)

rprint('[b green]Generated password[/]')
rprint(f'[b green]{generate_password(length, chars)}[/]')
