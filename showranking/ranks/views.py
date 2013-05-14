from django.http import HttpResponse
from django.utils import simplejson
from ranks.models import Ranks

def save_rank(request):
    success = False
    if request.method == 'POST':
        json_request = simplejson.loads(request.raw_post_data)
        try:
            user_id = request.POST['id']
            username = request.POST['username']
            points = request.POST['points']
        except KeyError:
            pass
        else:
            points = int(points)
            rank = Ranks(user_id=user_id, username=username, points=points)
            rank.save()
            success = True
    response = {'success': success}
    return HttpResponse(simplejson.dumps(response), mimetype='application/json')
