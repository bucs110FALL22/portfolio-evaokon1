article = "Today, President Biden promoted a goal to end hunger in the United States by 2030 as he delivered an address at the first White House conference on hunger since 1969, when President Richard M. Nixon pulled together a similar gathering. Biden said his administration is announcing $8 billion in public- and private-sector commitments to help reach the goal and said the push should be bipartisan and something for “the whole country to work on together. On Capitol Hill, the Senate moved a step closer Tuesday to avoiding a partial government shutdown after removing an energy-project permitting provision pushed by Sen. Joe Manchin III (D-W.Va.). Lawmakers are scrambling to pass a stopgap funding measure by Friday before leaving town."
substitutions = {"white house":"Pit of Despair",
    "allegedly":"totally",
    "bill":"snap I didn’t screenshot",
    "official":"puppy",
    "congressional":"spaaaaace",
    "republican":"piano accordionist",
    "democrat":"chromatic button accordionist",
    "senator": "magical wizard",
    "representative": "unmagical wizard",
    "secretary":"eating champion",
    "leaders":"goblins",
    "washington":"Mount Doom",
    "President": "you know, the guy"}
for key, value in substitutions.items():
  article = article.replace(key,value)
print(article)