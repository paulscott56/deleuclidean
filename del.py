from deliciousrec import *
import recommendations

delusers = initializeUserDict('chisimba')
delusers['pscott209'] = {}
fillItems(delusers)
print "done populating dataset"

user = 'pscott209'
rec = recommendations.topMatches(delusers, user)
print rec
