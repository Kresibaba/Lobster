from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Projects, RNList
from .forms import NewProjectForm, NonRadioactiveParameters, RadioactiveParameters
from .choices import *
from .nonrad_calcs import density_calculation


@login_required
def home(request, *args):
    projects = Projects.objects.filter(author=request.user.username).all().order_by('-create_date')

    if request.method == 'POST':

        # Adding projects to the database
        if 'add_project' in request.POST:

            form = NewProjectForm(request.POST)

            if form.is_valid():
                r = Projects(name=form.cleaned_data['project_name'],
                             author=request.user.username, status='Completed')
                r.save()
                l = RNList()
                form = NewProjectForm()
                return render(request, 'lobster/home.html', {'form': form, 'projects': projects, })

            else:
                form = NewProjectForm(request.POST or None)
                return render(request, 'lobster/home.html', {'form': form, 'projects': projects, })

        # Removing projects from the database
        elif 'remove_project' in request.POST:
            r = Projects.objects.get(pk = request.POST['remove_project'])
            r.delete()
            form = NewProjectForm()
            return render(request, 'lobster/home.html', {'form' : form, 'projects' : projects, })

    # Rendering all user's projects
    elif request.method =='GET':
        form = NewProjectForm()
        return render(request, 'lobster/home.html', {'form': form, 'projects': projects, })

# Login view
def login(request):
    return render(request, 'lobster/login.html')

# Logout view
def logout(request):
    return render(request, 'lobster/logout.html')

# Non radiological parameters
def nonradData(request, projects_id, *args):

    # Assigning a selected project
    curr_project = get_object_or_404(Projects.objects.filter(author=request.user.username).all(), pk = projects_id)

    # Saving a current project id to the session db
    request.session['curr_project_id'] = curr_project.pk

    if request.method == "GET":

        # Setting initial values from the database
        data = {'waste_type': curr_project.waste_type,
                'weight_net': curr_project.weight_net,
                'volume_net': curr_project.volume_net
        }

        form = NonRadioactiveParameters(initial=data)
        return render(request, 'lobster/nonradData.html', {'form': form}, )

    elif request.method == "POST":
        form = NonRadioactiveParameters(request.POST)

        if form.is_valid():
            waste_type = form.cleaned_data['waste_type']
            weight_net = form.cleaned_data['weight_net']
            volume_net = form.cleaned_data['volume_net']

            # Density calculation
            density_net = density_calculation(weight = weight_net, volume = volume_net)

            # Saving data to the database
            curr_project.waste_type = waste_type
            curr_project.weight_net = weight_net
            curr_project.volume_net = volume_net
            curr_project.density_net = density_net
            curr_project.save()

            # Return render(request, 'lobster/radData.html', {'form': form},)
            return redirect('/radData')

        else:
            return render(request, 'lobster/nonradData.html', {'form': form},)

# Radiological parameters view
def radData(request, *args):
    form = RadioactiveParameters(request.POST)
    print(request.session['curr_project_id'])

    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        #
        # try:
        #     del request.session['current_project_id']
        # except KeyError:
        #     pass

        pass

    return render(request, 'lobster/radData.html', {'form':form})




