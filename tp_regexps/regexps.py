import re

decision_ref_re = re.compile(r'<a\s+href="/decision/(?P<id>[^\?]+)')
ecli_re = re.compile(r"<p>(?P<ecli>ECLI:[A-Z]{2}:[A-Z]+:\d{4}:[A-Z0-9]+)</p>")
chamber_re = re.compile(r'<p\s+class="h4-like">(?P<chamber>[^\n]+)')
formation_re = re.compile(r'<p\s+class="h4-like">.*\n\s*-\s*(?P<formation>.*)')
publication_re = re.compile(
    r'<p\s+class=".* h4-like--emphase">\n\s*(?P<publication>[^<^\n]*)'
)
number_re = re.compile(
    r"<title>Décision\s-\sPourvoi\sn°(?P<number>.*)\s\|\sCour\sde\scassation<\/title>"
)
date_re = re.compile(
    r"<h1>(?P<day>\d{1,2})\s(?P<month>[a-zA-Zéèô]*)\s(?P<year>\d{4})<br>"
)
