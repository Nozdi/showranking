from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.utils import simplejson
from ranks.models import Ranks
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def save_rank(request):
    success = False
    
    if request.method == 'POST':
        try:
            user_id = request.POST['id']
            username = request.POST['username']
            points = request.POST['points']
        except KeyError:
            pass
        else:
            points = int(points)
            rank, created = Ranks.objects.get_or_create(user_id=user_id)
            rank.username = username
            rank.points = points
            rank.save()
            success = True
    response = {'success': success}
    return HttpResponse(simplejson.dumps(response), mimetype='application/json')

def get_sorted(request):
    rankings = Ranks.objects.all().order_by('points')
    data = {}
    for ranking in rankings:
        data.update({'id':ranking.user_id,
            'username':ranking.username, 
            'points':ranking.points})
    return HttpResponse(simplejson.dumps(data), mimetype="application/json")

def get_rank(request):
    rankings = Ranks.objects.all().order_by('points')
    return render_to_response('rank.html', {'rankings': rankings}, context_instance=RequestContext(request))
