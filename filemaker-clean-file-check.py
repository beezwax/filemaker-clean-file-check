#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Check if byte at offset 0x800 in a file is set to 0xAC
"""

import os

class TerminalColors:
	RED = '\033[91m'
	BOLD = '\033[1m'
	END = '\033[0m'


def print_error (msg: str):
	"""
	Print an error string with emphasis.
	"""
	print (TerminalColors.RED + TerminalColors.BOLD + msg + TerminalColors.END)


def check_byte_0x800(path: str) -> bool:
	'''
	Check if byte at offset 0x800 (2048 decimal) is set to 0xAC.
	Returns True if the byte equals 0xAC, False otherwise.
	Raises FileNotFoundError if file doesn't exist.
	Raises ValueError if file is too small.
	'''
	if not os.path.exists(path):
		raise FileNotFoundError(f"'{path}' does not exist")

	if not os.access(path, os.R_OK):
		raise PermissionError(f"'{path}' is not readable")

	if os.path.isdir(path):
		raise IsADirectoryError(f"'{path}' is a directory")

	file_size = os.path.getsize(path)
	if file_size < 0x801:
		raise ValueError(f"'{path}' is too small (needs at least 196608 bytes, has {file_size})")

	with open(path, 'rb') as f:
		f.seek(0x800)
		byte_value = f.read(1)
		return byte_value[0]


if __name__ == '__main__':
	import sys
	
	if len(sys.argv) < 2:
		print("Usage: python3 filemaker-clean-file-check.py <file_path>")
		print ()
		sys.exit(1)
	
	file_path = sys.argv[1]
	
	try:
		result = check_byte_0x800(file_path)
		print ()
		if result == 0xAC:
			print(f"✓ Byte at 0x800 is 0xAC")
			print ("This file was closed normally.")
			print ()
		elif result == 0:
			print(f"✗ Byte at 0x800 is 0x{result:02X} (expected 0xAC)")
			print_error ("FILE NOT CLOSED CLEANLY")
			print ("This file should be checked more closely for problems, or use a backup instead.")
			print ()
			sys.exit(1)
		else:
			print(f"✗ Byte at 0x800 is 0x{result:02X} and is not a valid flag")
			print_error ("THIS FILE IS PROBABLY DAMAGED OR NOT A FMP12 FILE")
			sys.exit(2)

	except Exception as e:
		print(f"Error: {e}")
		sys.exit(3)

	sys.exit (0)
