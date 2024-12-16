import re

decision_ref_re = re.compile(r'<a\s+href="/decision/(?P<id>[^\?]+)')
ecli_re = re.compile(r'<p>(?P<ecli>ECLI:[A-Z]{2}:[A-Z]{5}:\d{4}:[A-Z0-9]{7})</p>')
decision_header_re = re.compile(r'<div class=\"decision-header\">\s+<p class="h4-like">(?P<chamber>Chambre criminelle|Chambre sociale|Première chambre civile|Troisième chambre civile|Première présidence \(Ordonnance\)|Deuxième chambre civile|Chambre commerciale financière et économique)\s+-?\s+(?P<formation>Formation [^\n]+)?(\s*</p>\s*<p class="h4-like h4-like--emphase">\s*(?P<publication>Publié au Bulletin)\s*</p>)?')
number_re = re.compile(r'Cour de cassation<br>\s*Pourvoi n°\s*(?P<number>[0-9-.]+)\s*</h1>')