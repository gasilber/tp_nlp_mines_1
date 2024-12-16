import re

decision_ref_re = re.compile(r'<a\s+href="/decision/(?P<id>[^\?]+)')
ecli_re = re.compile(r'<p>(?P<ecli>ECLI:[^<]+)</p>')
chamber_re = re.compile(r'<p class="h4-like">(?P<chamber>.*?)(-|\n.*<)', re.DOTALL)
formation_re = re.compile(r'<p class="h4-like">.*?(?P<formation>Formation .*?)\n\s*<', re.DOTALL)
publication_re = re.compile(r'<p class="h4-like h4-like--emphase">.*?(?P<publication>Publié .*?)\s*<', re.DOTALL)
number_re = re.compile(r'Pourvoi n°(?P<number>\d*-\d*\.\d*)', re.DOTALL)
date_re = re.compile(r'<h1>(?P<date>(\d|\d\d) .*? (19|20)\d\d)<br>')
solution_re = re.compile(r'2024(<br>\n )+(?P<solution>([rR][eE][jJ]|[cC][aA][sS]).*?)(<br>\n|\s)', re.DOTALL)