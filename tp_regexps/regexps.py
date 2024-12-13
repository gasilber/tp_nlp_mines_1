import re

decision_ref_re = re.compile(r'<a\s+href="/decision/(?P<id>[^\?]+)')
ecli_re = re.compile(r'<p>(?P<ecli>ECLI:[A-Z]{2}:[A-Z]{5}:\d{4}:[A-Z0-9]{7})</p>')
decision_header_re = re.compile(r'<div class=\"decision-header\">\s+<p class="h4-like">(?P<chamber>Chambre [a-zA-Z0-9]+)\s+-\s+(?P<formation>Formation [^\n]+)')
