import re

decision_ref_re = re.compile(r'<a\s+href="/decision/(?P<id>[^\?]+)')
ecli_re = re.compile(r'<p>(?P<ecli>ECLI:[A-Z]{2}:[A-Z]{5}:\d{4}:[A-Z0-9]{7})</p>')
