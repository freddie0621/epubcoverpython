

set chaine=COUVERTURE_

for %%1 in ("*.epub") do (
epubcover %%1  %chaine%%%~n1.jpg 600
)

