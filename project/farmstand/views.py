from project.settings import *
from django.shortcuts import render, render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.forms import inlineformset_factory
from farmstand.models import (Product,
                            Week,
                            Week_Product,
                            Season
)
from farmstand.forms import (UserForm,
                            UserProfileForm,
                            WeeklyProductForm,
                            WeekSelectorForm
)

def home(request):

    context_dict = []

    return render(request, 'farmstand/home.html', context_dict)

def products(request):

    product_list = Products.objects.all()

    context_dict = {'products': product_list}


    return render(request, 'farmstand/products.html', context_dict)

def register(request):

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # If it's a HTTP POST, we're interested in processing form data.
    if request.method == 'POST':
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Now we save the UserProfile model instance.
            profile.save()

            # Update our variable to tell the template registration was successful.
            registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'farmstand/register.html',
            {'user_form': user_form, 'profile_form': profile_form, 'registered': registered} )

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('/farmstand/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('farmstand/login.html', {}, context)

def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage.
    return HttpResponseRedirect('/farmstand/')

def weekly_products(request):
    # This view should show an empty form if no weekly_products records exist.
    # If records do exist, the form should show as pre-populated.
    # On POST, the records should be overwritten.
    if request.method == 'POST':
        form = WeeklyProductForm(data=request.POST)
        selection_set = request.POST.getlist('selection')
        w = Week.objects.get(pk=8)
        # For each item in selection, create
        # record in  week_product table.
        existing = [p for p in w.week_product_set.all().values_list('product_id', flat=True)]
        for selection in selection_set:
            p = Product.objects.get(pk=selection)
            wp = Week_Product.objects.get_or_create(
                product=p,week=w
                )
        for item in existing:
            if unicode(item) not in selection_set:
                p = Product.objects.get(pk=item)
                wp = Week_Product.objects.get_or_create(
                    product=p,week=w
                    )
                Week_Product.objects.filter(id=wp[0].id).delete()
        return HttpResponseRedirect('/farmstand/')
    else:
        # Assume week_id = 8
        # Get set of products associated with that week
        # from Week_Product
        week = Week.objects.get(pk=8)
        initial = {'selection':[p for p in week.week_product_set.all().values_list('product_id', flat=True)]}
        form = WeeklyProductForm(initial=initial)
        context_dict = {'form': form}
        return render(request, 'farmstand/weekly_products.html', context_dict)

def season_select(request):
    if request.GET.getlist('selection'):
        form = Week_SelectorForm
        context_dict = {'form': form}
        selection = request.GET.getlist('selection')
        print selection
    else:
        season = Season.objects.all()
        form = Week_SelectorForm
        context_dict = {'form': form}
    return render(request, 'farmstand/season_select.html', context_dict)

def inline_test(request):
    season = Season.objects.all()
    WeekInlineFormSet = inlineformset_factory(Season, Week, fields=('season', 'number',))
    formset = WeekInlineFormSet(queryset=season)
    form = WeekSelectorForm()
    context_dict = {'formset': formset, 'form': form}

    return render(request, 'farmstand/inline_test.html', context_dict)

def get_season_weeks(request):
    season = get_object_or_404(pk=request.GET('season', None))
    resp = ", ".join(Season.Week_set.values_list('number', flat=True))
    return HttpResponse(resp)
