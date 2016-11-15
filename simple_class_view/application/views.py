import urllib
import json
import datetime

from django.shortcuts import render, redirect
from django.template import RequestContext, loader
from django.http import HttpResponse
from django.template.defaulttags import register

from rest_framework.views import APIView


@register.filter
def date_format(val,value):
    date = datetime.datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    return date.strftime('%b %d %Y')

class BaseHandler(APIView):
    def __init__(self, request=None, response=None):
        self.data = {}
        
    def render(self, request, template_path):
        if "error" in request.session:
            self.data["error"] = request.session["error"]

        template = loader.get_template(template_path)
        return HttpResponse(template.render(RequestContext(request, self.tv)))

class FrontPageHandler(BaseHandler):
    def get(self, request, *args, **kwargs):
        
        url = "API endpoint - for example: http://www.programmableweb.com/category/all/apis"
        response = urllib.urlopen(url).read()
        data = json.loads(response)

        self.data['key'] = data["key"]
        
        return self.render(request, 'index.html')