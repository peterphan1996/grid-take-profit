import argparse
from rich import print
from rich.pretty import pprint
from rich.console import Console
from rich.table import Table
from coinmarket import get_crypto_price
from grid import fibonacci_grid

# Create the parser
parser = argparse.ArgumentParser()

# Add the arguments
parser.add_argument('-price', type=float, help='The price value')
parser.add_argument('-line', type=int, help='The line value', default=8)
parser.add_argument('-amount', type=int, required=True, help='The amount value')
parser.add_argument('-symbol', type=str, help='The symbol of the cryptocurrency')

# Parse the arguments
args = parser.parse_args()

# Get the values
price = args.price
line = args.line
amount = args.amount
crypto_id = args.symbol

if crypto_id is not None and price is None:
    price = get_crypto_price(crypto_id)
    print(f'The current price of {crypto_id} in USDT is: {price}.\nThis price will be used as the base grid line.\n\n')
elif price is None and crypto_id is None:
    print('Please provide a price or a symbol')
    exit()

# Call this function with argument from running app.py -price=100 -lines=5
# pprint(result, expand_all=True)
result = fibonacci_grid(price, line, amount)

table=Table(title=f"Take profit by grid ({line} lines)")
table.add_column("Line",style="yellow")
table.add_column("Price",style="cyan")
table.add_column("Amount", style="bright_green")

for index, (price, amount) in enumerate(result['price_by_amount'].items()):
    formatted_price = f"{price:.10f}"
    formatted_amount = f"{amount:.10f}"
    table.add_row(f"#{index+1}", formatted_price, formatted_amount)

console=Console(log_time=False)
console.print(table)
console.log(f"[green]Average profit price:[/green]  [yellow]{result['average_price']:.10f}[/yellow]")
console.log(f"[green]Percentage change:[/green]  [yellow]{result['percentage_change']}%[/yellow]")

