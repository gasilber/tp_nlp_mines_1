from requests_html import HTMLSession

from tp_regexps import regexps


class Judilibre(object):

	base_url = "https://www.courdecassation.fr"

	base_search_url = (
		"{url}/recherche-judilibre?"
		"search_api_fulltext={search_api_fulltext}"
		"&date_du={date_du}"
		"&date_au={date_au}"
		"&judilibre_juridiction={juridiction}"
		"&op={op}"
		"&sort={sort}"
		"&items_per_page={items_per_page}"
		"&page={page}"
	)

	base_decision_url = (
		"{url}/decision/{id}"
	)

	user_agent = (
		"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
		" AppleWebKit/605.1.15 (KHTML, like Gecko)"
		" Version/18.0.1 Safari/605.1.15"
	)

	def __init__(self):
		self.juridiction = "cc"
		self.op = "Rechercher%20sur%20judilibre"
		self.date_du = ''
		self.date_au = ''
		self.search_api_fulltext = ''
		self.sort = 'date-desc'
		self.items_per_page = 30
		self.session = HTMLSession()

	def search(self, pages=1):
		html = list()
		for page in range(pages):
			url = self.base_search_url.format(
				url=self.base_url,
				search_api_fulltext=self.search_api_fulltext,
				date_du=self.date_du,
				date_au=self.date_au,
				juridiction=self.juridiction,
				op=self.op,
				sort=self.sort,
				items_per_page=self.items_per_page,
				page=page
			)
			html.append(self.get_html(url))
		return '\n'.join(html)

	def decision(self, id):
		url = self.base_decision_url.format(
			url=self.base_url,
			id=id
		)
		return self.get_html(url)

	def decisions(self, pages=1):
		html = self.search(pages)
		decisions = list()
		for m in regexps.decision_ref_re.finditer(html):
			decisions.append(m.group('id'))
		for f in decisions:
			print(f'"{f}",')
		return decisions

	def get_html(self, url):
		response = self.session.get(url)
		response.html.render()
		return response.html.html
