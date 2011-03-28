from django.http import HttpResponse
from pyofc2  import * 
from django.http import HttpResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from pyofc2  import * 
import random
import time
def chart_data(request):
    t = title(text=time.strftime('%a %Y %b %d'))
    b1 = bar()
    b1.values = range(9,0,-1)
    b2 = bar()
    b2.values = [random.randint(0,9) for i in range(9)]
    b2.colour = '#56acde'
    chart = open_flash_chart()
    chart.title = t    
    chart.add_element(b1)
    chart.add_element(b2)
    return HttpResponse(chart.render())
    
def bar_chart(request):

        #t = title(text=time.strftime('%a %Y %b %d'))
    t = title(text="Django Bar Chart")
    #b = bar_filled(colour="#FF4500")
    b = bar_glass(colour="#FF8000")
    b.fill_colour = "#FF4500"
    b.halo_size = 1
    b.dot_type = "solid_dot"

    b.on_show = bar_on_show(type="grow-up",cascade=0.5,delay=1)
    b.text = "visits"
    b.dot_size = 4
    b.values = range(30 ,0, -1)

    x = x_axis()
    y = y_axis()
    x.colour = "#cccccc"
    x.min, x.max, x.steps = 0, 30, 1
    y.min, y.max, y.steps = 0, 30, 1
    chart = open_flash_chart()
    chart.title = t
    chart.x_axis = x
    chart.y_axis = y
    chart.add_element(b)
    #t = {"on-show": {"type": "grow-up","cascade": 0.5,"delay": 1}}
    data = chart.render()

    return render_to_response('chart.html',
        {   'data':data
        },
        context_instance=RequestContext(request)
    )

    