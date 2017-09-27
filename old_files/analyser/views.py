from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader
from .models import Packages, Users, Volumes
from highcharts import Highchart

try: import cPickle
except: import pickle as cPickle
import pickle
import os.path as path
import re

def welcome(request):
    template = loader.get_template('welcome.html')
    context = {}
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "resources.txt"))

    with open(filepath, 'wb') as f:
        f.close()

    return HttpResponse(template.render(context, request))

def home(request):
    # Passing in the models and the different OSs in database
    basepath = path.dirname(__file__)
    object_types = ["Packages", "Users", "Volumes"]
    os_types = Packages.objects.order_by().values_list('os').distinct()
    template = loader.get_template('home.html')
    os_types_list = []

    with open(path.abspath(path.join(basepath, "..", "resources.txt")), 'wb') as f:
        f.close()

    for os in os_types:
        os_upper = os[0].capitalize()
        os_types_list.append(os_upper)

    context = {
        'os_types' : filter(None, os_types_list),
        'object_types' : object_types,
    }

    return HttpResponse(template.render(context, request))


def graph(request):
    # Initialize the os_types passed from the home page, the resource chosen to compare
    # And the chart options
    template = loader.get_template('analyser.html')
    compare_obj = ''
    os_types = []
    data_return = []
    options = {}
    table = []
    error = False
    basepath = path.dirname(__file__)
    filepath = path.abspath(path.join(basepath, "..", "resources.txt"))
    # As there are multiple HTTP requests being passed to the graph, look for the POST request with data in it and pass
    # it to the resource.txt file
    if request.method == 'POST' and request.POST.get('object[object]') != None and request.POST.getlist('os_types') != None:
        compare_obj = request.POST.get('object[object]')
        os_types = request.POST.getlist('os_types[]')

        with open(filepath, 'wb') as f:
            print(os_types, compare_obj)
            cPickle.dump((compare_obj, os_types), f, protocol=cPickle.HIGHEST_PROTOCOL)
    try:
        with open(filepath, 'rb') as f:
            compare_obj, os_types = pickle.load(f)
            f.close()
    except EOFError:
        if (error != True):
            error = True
        else:
            error = False
        print("EOFException occurred")

    data = []
    colors = ["#e31a1c", "#fb9a99", "#b2df8a", "#fdbf6f"]

    # Iterate through the nodes chosen to gather relevant data from the database based on the resource type
    # chosen for comparison
    for index, os in enumerate(os_types):
        if compare_obj == "packages":
            table_data = Packages.objects.filter(os=os).values_list('title', 'version', 'provider').distinct()
            data_return = ['Package', 'Package version', 'Provider']
            os_data = Packages.objects.filter(os=os).values_list('title', 'version').distinct()
            # The graph options are passed to the python-highcharts wrapper as a Python dictionary
            options = {
                'chart': {
                    'type': 'scatter',
                    'zoomType': 'xy',
                },
                'title': {
                    'text': 'Comparison of packages from different nodes'
                },
                'subtitle': {
                    'text': 'Data gathered from Puppet runs on selected nodes'
                },
                'xAxis': {
                    'title': {
                        'enabled': True,
                        'text': 'Nodes'
                    },

                    'categories': [x.title() for x in os_types],
                },
                'yAxis': {
                    'title': {
                        'text': 'Versions'
                    },
                    'max': 500,
                },
                'tooltip': {
                    'headerFormat': '<b>Package on {point.x}</b><br/>',
                    'pointFormat': 'Package name : {point.name}</b><br/>Version : {point.amount}'
                },
                'plotOptions': {
                    'scatter': {
                        'allowPointSelect': True,
                        'turboThreshold': 30000,
                        'showInLegend': False,
                        'marker': {
                            'enabled': True,
                            'states': {
                                'hover': {
                                    'fillColor': '#ec971f',
                                }
                            }
                        }
                    }
                }

            }
        if compare_obj == 'users':
            table_data = Users.objects.filter(os=os).values_list('title', 'uid', 'gid').distinct()
            os_data = Users.objects.filter(os=os).values_list('title', 'uid').distinct()
            data_return = ['User', 'UID', 'GID']
            options = {
                'chart': {
                    'type': 'scatter',
                    'zoomType': 'xy',
                },
                'title': {
                    'text': 'Comparison of users on different nodes'
                },
                'subtitle': {
                    'text': 'Data gathered from Puppet runs on selected nodes'
                },
                'xAxis': {
                    'title': {
                        'enabled': True,
                        'text': 'Nodes'
                    },

                    'categories': [x.title() for x in os_types],
                },
                'yAxis': {
                    'title': {
                        'text': 'User IDs'
                    },
                    'max': 1000,
                },
                'tooltip': {
                    'headerFormat': '<b>User on {point.x}</b><br/>',
                    'pointFormat': 'User name : {point.name}</b><br/>UID : {point.y}'
                },
                'plotOptions': {
                    'scatter': {
                        'allowPointSelect': True,
                        'turboThreshold': 30000,
                        'showInLegend': False,
                        'marker': {
                            'enabled': True,
                            'states': {
                                'hover': {
                                    'fillColor': '#ec971f',
                                }
                            }
                        }
                    }
                }
            }


        if compare_obj == 'volumes':
            table_data = Volumes.objects.filter(os=os).values_list('volume_name', 'available', 'capacity').distinct()
            os_data = Volumes.objects.filter(os=os).values_list('volume_name', 'available').distinct()
            data_return = ['Volume', 'Available space', 'Capacity']
            options = {
                'chart': {
                    'type': 'scatter',
                    'zoomType': 'xy',
                },
                'title': {
                    'text': 'Comparison of volume availability on different nodes'
                },
                'subtitle': {
                    'text': 'Data gathered from Puppet runs on selected nodes'
                },
                'xAxis': {
                    'title': {
                        'enabled': True,
                        'text': 'Nodes'
                    },

                    'categories': [x.title() for x in os_types],
                },
                'yAxis': {
                    'title': {
                        'text': 'Available space'
                    },
                    'max': 1000,
                },
                'tooltip': {
                    'headerFormat': '<b>Device on {point.x}</b><br/>',
                    'pointFormat': 'Device : {point.name}</b><br/>Volume available : {point.y} {point.amount}'
                },
                'plotOptions': {
                    'scatter': {
                        'allowPointSelect': True,
                        'turboThreshold': 30000,
                        'showInLegend': False,
                        'marker': {
                            'enabled': True,
                            'states': {
                                'hover': {
                                    'fillColor': '#ec971f',
                                }
                            }
                        }
                    }
                }

            }
        #   Before the data is absorbed by Highcharts, some transformations are required to normalise the data further
        for title, value in os_data:
            dict = {}
            dict["x"] = index
            if compare_obj == 'volumes':
                dict["y"] = float(value.split(' ', 1)[0])
                dict["amount"] = value.split(' ', 1)[1]
            elif compare_obj == 'packages':
                dict["amount"] = value
                value = re.split("[-+~_]", value[0])[0]
                value = value.replace(":", "0")
                value = ".".join(value.split('.', 2)[:2])
                value = re.split("[a-zA-Z]", value)[0]
                if (value != ""):
                    try:
                        dict["y"] = float(value)
                    except:
                        dict["y"] = int(float(value))
            elif compare_obj == 'users':
                dict["y"] = value
            dict["name"] = title
            dict["color"] = colors[index]
            data.append(dict)
        for title, value, value2 in table_data:
            dict = {}
            dict["os"] = os.title()
            dict["title"] = title
            if compare_obj == 'packages':
                dict["value"] = value[0]
            else:
                dict["value"] = value
            dict["value2"] = value2
            table.append(dict)

    # Initialising the Highcharts object
    chart = Highchart(width=850, height=600)

    # Setting the chart options and passing the data to the chart
    chart.set_dict_options(options)
    chart.add_data_set(data, 'scatter')

    chart_path = path.abspath(path.join(basepath, "templates", "chart"))

    chart.save_file(chart_path)

    # Returning the data to the template
    context = {
        'table_data': table,
        'data_return': data_return,
        'error': error,
    }

    return HttpResponse(template.render(context, request))
