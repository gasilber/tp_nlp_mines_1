import re

decision_ref_re = re.compile(r'<a\s+href="/decision/(?P<id>[^\?]+)')
ecli_re = re.compile(r"(?P<ecli>ECLI:[A-Z]+:[A-Z]+:\d{4}:[A-Z0-9]+)")
