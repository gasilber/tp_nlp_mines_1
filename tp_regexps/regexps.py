import re

decision_ref_re = re.compile(r'<a\s+href="/decision/(?P<id>[^\?]+)')
ecli_re = re.compile(r"(?P<ecli>ECLI:[A-Z]+:[A-Z]+:\d{4}:[A-Z0-9]+)")
chamber_re = re.compile(r'class="h4-like">(?P<chamber>.*)')
formation_re = re.compile(r"TODO")
publication_re = re.compile(r"TODO")
number_re = re.compile(r"TODO")
decision_date_re = re.compile(r"TODO")
solution_re = re.compile(r"TODO")
content_re = re.compile(r"TODO")
texts_re = re.compile(r"TODO")