import unittest
from pathlib import Path
import json
import os

from tp_regexps import regexps
from tp_regexps.decision import Decision


class TestRegexps(unittest.TestCase):

	def test_decision_ref(self):
		"""Récupération des références vers des décisions"""
		data_path = Path(__file__).parent / 'data' / 'ccass' / 'search_results.txt'
		with open(data_path, 'r', encoding='utf-8') as f:
			data = f.read()
		decisions_path = Path(__file__).parent / 'data' / 'ccass' / 'decisions.json'
		with open(decisions_path, 'r', encoding='utf-8') as f:
			decisions = json.load(f)
		found_decisions = []
		for m in regexps.decision_ref_re.finditer(data):
			found_decisions.append(m.group('id'))
		self.assertListEqual(decisions, found_decisions, 'List of decisions differs')

	@staticmethod
	def __iterate_on_decisions():
		decisions_path = Path(__file__).parent / 'data' / 'ccass'
		for filename in sorted(os.listdir(decisions_path)):
			if filename.endswith('.json'):
				id = filename[:-5]
				json_path = os.path.join(decisions_path, filename)
				html_path = os.path.join(decisions_path, filename[:-5] + '.html')
				if os.path.exists(html_path):
					with open(html_path, 'r', encoding='utf-8') as f:
						html_data = f.read()
					with open(json_path, 'r', encoding='utf-8') as f:
						json_data = f.read()
					reference_decision = Decision.from_json(json_data)
					html_decision = Decision.from_html(id, html_data)
					yield id, reference_decision, html_decision

	def test_ecli(self):
		"""Récupération du numéro ECLI"""
		for id, reference_decision, html_decision in self.__iterate_on_decisions():
			with self.subTest(id, id=id):
				self.assertEqual(reference_decision.ecli, html_decision.ecli, id)

	def test_chamber(self):
		"""Récupération de la chambre"""
		for id, reference_decision, html_decision in self.__iterate_on_decisions():
			with self.subTest(id, id=id):
				self.assertEqual(reference_decision.chamber, html_decision.chamber, id)
