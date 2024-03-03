from django.shortcuts import render, redirect, get_object_or_404
from .models import TeamMembers
from .forms import TeamForm
from Tickets.models import *
from Tickets.forms import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.db.models import Count
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def Agents(request):
	agents = TeamMembers.objects.all()
	offer = CreateOffer.objects.values('agent').annotate(Count('agent'))
	addendum = CreateAddendum.objects.values('agent').annotate(Count('agent'))
	listing = CreateListing.objects.values('agent').annotate(Count('agent'))
	mls_attachments = CreateMLSsheet.objects.values('agent').annotate(Count('agent'))
	mls_search = CreateSearch.objects.values('agent').annotate(Count('agent'))
	dotloop = CreateDotloop.objects.values('agent').annotate(Count('agent'))

	a = offer.values_list('agent','agent__count')
	b = addendum.values_list('agent', 'agent__count')
	c = listing.values_list('agent','agent__count')
	d = mls_attachments.values_list('agent', 'agent__count')
	e = mls_search.values_list('agent','agent__count')
	f = dotloop.values_list('agent', 'agent__count')

	for agent in agents:
		for count in a:
			if agent.id == count[0]:
				agent.offer = count[1]
		for count in b:
			if agent.id == count[0]:
				agent.addendum = count[1]
		for count in c:
			if agent.id == count[0]:
				agent.listing = count[1]
		for count in d:
			if agent.id == count[0]:
				agent.mls_attachments = count[1]
		for count in e:
			if agent.id == count[0]:
				agent.mls_search = count[1]
		for count in f:
			if agent.id == count[0]:
				agent.dotloop = count[1]
		agent.save()
	return render(request, 'agents.html', {'encabezado':"Team", "agents":agents})

@login_required
def AddAgent(request):
	if request.method == "POST":
		form = TeamForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('agents')
	else:
		form = TeamForm()
	return render(request, 'addagent.html', {'form':form, 'encabezado':'Add Agent'})
	
@login_required
def AgentInfo(request, agent_id):
	agent = get_object_or_404(TeamMembers, pk = agent_id)
	return render(request, 'agentinfo.html',{'encabezado':agent.name, 'agent':agent})
@login_required
def requested(request, agent_id):
	agent = get_object_or_404(TeamMembers, pk = agent_id)
	offers = CreateOffer.objects.filter(agent=agent_id)
	addendums = CreateAddendum.objects.filter(agent=agent_id)
	listings = CreateListing.objects.filter(agent=agent_id)
	mlssheets = CreateMLSsheet.objects.filter(agent=agent_id)
	mls_searches = CreateSearch.objects.filter(agent=agent_id)
	dotloops = CreateDotloop.objects.filter(agent=agent_id)
	return render(request,'requested.html',{'encabezado':f"Requested by {agent.name}",'offers':offers,
					'addendums':addendums,'listings':listings,'mlssheets':mlssheets,'mls_searches':mls_searches,
					'dotloops':dotloops})
@login_required
def pendings(request, agent_id):
	agent = get_object_or_404(TeamMembers, pk = agent_id)
	offers = CreateOffer.objects.filter(agent=agent_id, completed__isnull = True)
	addendums = CreateAddendum.objects.filter(agent = agent_id, completed__isnull = True)
	listings = CreateListing.objects.filter(agent = agent_id, completed__isnull = True)
	mlssheets = CreateMLSsheet.objects.filter(agent = agent_id, completed__isnull = True)
	mls_searches = CreateSearch.objects.filter(agent = agent_id, completed__isnull = True)
	dotloops = CreateDotloop.objects.filter(agent = agent_id, completed__isnull = True)
	return render(request, 'pendings.html', {'encabezado':f"Pending requests of {agent.name}", "offers":offers,
		'addendums':addendums,'listings':listings, 'mlssheets':mlssheets,'mls_searches':mls_searches, 'dotloops':dotloops})
@login_required
def completed(request, agent_id):
	agent = get_object_or_404(TeamMembers, pk = agent_id)
	offers = CreateOffer.objects.filter(agent=agent_id, completed__isnull = False)
	addendums = CreateAddendum.objects.filter(agent=agent_id, completed__isnull = False)
	listings = CreateListing.objects.filter(agent=agent_id, completed__isnull = False)
	mlssheets = CreateMLSsheet.objects.filter(agent=agent_id, completed__isnull = False)
	mls_searches = CreateSearch.objects.filter(agent=agent_id, completed__isnull = False)
	dotloops = CreateDotloop.objects.filter(agent=agent_id, completed__isnull = False)
	return render(request, 'completed.html', {'encabezado':f"Completed requests of {agent.name}", 'offers':offers,
		'addendums':addendums, 'listings':listings, 'mlssheets':mlssheets, 'mls_searches':mls_searches, 'dotloops':dotloops})