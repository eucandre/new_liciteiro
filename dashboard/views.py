# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def dashboard_index(request):
  return render(request, "dashboard.html")
