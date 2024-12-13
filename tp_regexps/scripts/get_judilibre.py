import argparse
import os
import sys
from pathlib import Path

from tp_regexps.decision import Decision
from tp_regexps.judilibre import Judilibre


def download(filename, data):
	with open(filename, 'w') as f:
		f.write(data)
	print(f"wrote to {filename}")


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("operation", choices=(
		'search', 'decision', 'decisions', 'read_decision',
		'write_test_decisions', 'parse_html_decision',
		'parse_html_decisions'
	))
	parser.add_argument("param1", default=None, nargs='?')
	parser.add_argument("-d", "--download", default=False, action='store_true')
	parser.add_argument("-f", "--force", default=False, action='store_true')
	args = parser.parse_args()

	judilibre = Judilibre()

	if args.operation == 'search':
		count = int(args.param1) if args.param1 else 0
		if count > 0:
			pages = count // judilibre.items_per_page
			remaining = count % judilibre.items_per_page
			if remaining > 0:
				pages += 1
		else:
			pages = 1
		data = judilibre.search(pages)
		if args.download:
			download("search.html", data)
		else:
			print(data)
	elif args.operation == 'decision':
		id = args.param1
		if id is None:
			print("ERROR: missing decision id", file=sys.stderr)
			return 1
		data = judilibre.decision(id)
		if args.download:
			download(f"{id}.html", data)
		else:
			print(data)
	elif args.operation == 'write_test_decisions':
		path = args.param1
		if path is None:
			print("ERROR: missing test decisions path", file=sys.stderr)
			return 1
		for filename in os.listdir(path):
			if filename.endswith(".html"):
				id = filename[:-5]
				if id == '6757dc458b75c64649d25972':
					print(f"skip {id}")
					continue
				html_filename = os.path.join(path, filename)
				with open(html_filename, 'r') as f:
					html_data = f.read()
				html_decision = Decision.from_html(id, html_data)
				json_filename = Path(path) / f"{id}.json"
				if not os.path.exists(json_filename) or args.force:
					with open(json_filename, 'w') as f:
						f.write(html_decision.to_json())
						print(f"wrote to {json_filename}")
	elif args.operation == 'read_decision':
		path = args.param1
		if path is None:
			print("ERROR: missing decision path", file=sys.stderr)
			return 1
		with(open(path, 'r')) as f:
			data = f.read()
		decision = Decision.from_json(data)
		print(decision.to_json())
	elif args.operation == 'parse_html_decision':
		path = args.param1
		if path is None:
			print("ERROR: missing decision path", file=sys.stderr)
			return 1
		with open(path, 'r') as f:
			html_data = f.read()
		id = os.path.basename(path)[:-5]
		html_decision = Decision.from_html(id, html_data)
		print(html_decision.to_json())
	elif args.operation == 'parse_html_decisions':
		path = args.param1
		if path is None:
			print("ERROR: missing decisions path", file=sys.stderr)
			return 1
		for filename in os.listdir(path):
			if filename.endswith(".html"):
				html_path = os.path.join(path, filename)
				with open(html_path, 'r') as f:
					html_data = f.read()
				id = filename[:-5]
				html_decision = Decision.from_html(id, html_data)
				print(html_decision.to_json())
	elif args.operation == 'decisions':
		count = int(args.param1) if args.param1 else 0
		if count > 0:
			pages = count // judilibre.items_per_page
			remaining = count % judilibre.items_per_page
			if remaining > 0:
				pages += 1
		else:
			pages = 1
		decisions = judilibre.decisions(pages)
		if args.download:
			for id in decisions:
				decision = judilibre.decision(id)
				download(f"{id}.html", decision)
		else:
			print(decisions)
	return 0
