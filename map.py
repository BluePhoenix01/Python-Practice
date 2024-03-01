import argparse
import webbrowser, sys

# Get address from command line.
parser = argparse.ArgumentParser(description='Open the given address in maps.')
parser.add_argument('address', type=str, help='Address string from command line', default='950 Main St, Worcester, MA 01610', nargs='?')
args = parser.parse_args()
address = args.address

webbrowser.open('https://www.google.com/maps/place/' + address)
