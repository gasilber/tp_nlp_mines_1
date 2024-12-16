import re

decision_ref_re = re.compile(r'<a\s+href="/decision/(?P<id>[^\?]+)')
ecli_re = re.compile(r"<p>(?P<ecli>ECLI:[A-Z]{2}:[A-Z]+:\d{4}:[A-Z0-9]+)</p>")
chamber_re = re.compile(r'<p\s+class="h4-like">(?P<chamber>[^\n]+)')
formation_re = re.compile(r'<p\s+class="h4-like">.*\n\s*-\s*(?P<formation>.*)')
