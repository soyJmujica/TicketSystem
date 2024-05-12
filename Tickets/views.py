from django.shortcuts import render, redirect, get_object_or_404
from .models import CreateOffer, CreateAddendum, CreateListing, CreateMLSsheet, CreateSearch,CreateDotloop
from .forms import OfferForm, AddendumForm, ListingForm, MLSsheetForm, SearchForm, DotloopForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from datetime import datetime
# Create your views here.

def home(request):
	return render(request, 'home.html', {'encabezado':'Create a Ticket'})

def offer(request):
	if request.method == "POST":
		form = OfferForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = OfferForm()
	return render(request, 'offer.html', {'form':form, 'encabezado':'Offer Request'})

@login_required
def pendingoffer(request):
	offers = CreateOffer.objects.filter(completed__isnull = True)
	return render(request, 'pendingoffer.html', {'offers':offers,'encabezado':'Offers Pending to be done'})

@login_required
def detailoffer(request, offer_id):
	offer = get_object_or_404(CreateOffer,pk=offer_id)
	return render(request, 'offerdetails.html',{'offer':offer, 'encabezado':offer.address})
@login_required
def completedoffer(request, offer_id):
	offer = get_object_or_404(CreateOffer,pk=offer_id)
	if request.method == "POST":
		offer.completed = datetime.now()
		offer.completed_by = request.user
		offer.save()
		return redirect('pending offers')
	return render(request, 'offerdetails.html',{'offer':offer, 'encabezado':offer.address})	

def addendum(request):
	if request.method == "POST":
		form = AddendumForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = AddendumForm()
	return render(request, 'addendum.html',{'form':form, 'encabezado':'Addendum Request'})

@login_required
def pendingaddendum(request):
	addendums = CreateAddendum.objects.filter(completed__isnull = True)
	return render(request, 'pendingaddendum.html', {'addendums':addendums, 'encabezado':'Pending Addendums'})

@login_required
def detailaddendum(request, addendum_id):
	addendum = get_object_or_404(CreateAddendum, pk = addendum_id)
	return render(request, 'addendumdetails.html', {'encabezado':addendum.addendum, 'addendum':addendum})

@login_required
def completedaddendum(request, addendum_id):
	addendum = get_object_or_404(CreateAddendum, pk = addendum_id)
	if request.method == "POST":
		addendum.completed = datetime.now()
		addendum.completed_by = request.user
		addendum.save()
		return redirect('addendum details', addendum_id = addendum.id)
	return render(request, 'addendumdetails.html', {'encabezado':addendum.addendum, 'addendum':addendum})



def listing(request):
	if request.method == "POST":
		form = ListingForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = ListingForm()
	return render(request,'listing.html', {'form':form, 'encabezado':"Listing Request"})

@login_required
def pendinglisting(request):
	listings = CreateListing.objects.filter(completed__isnull = True)
	return render(request, 'pendinglisting.html', {'listings':listings,
		"encabezado":"Listings Pending to be Done"})

@login_required
def detaillisting(request,listing_id):
	listing = get_object_or_404(CreateListing,pk = listing_id)
	return render(request, 'listingdetails.html',{'listing':listing, 'encabezado':listing.address})
@login_required
def completedlisting(request, listing_id):
	listing = get_object_or_404(CreateListing,pk = listing_id)
	if request.method == 'POST':
		listing.completed = datetime.now()
		listing.completed_by = request.user
		listing.save()
		return redirect('listing details', listing_id=listing.id)
	return render(request, 'pendinglisting.html', {'listings':listings,"encabezado":"Listings Pending to be Done"})

def mlssheet(request):
	if request.method == 'POST':
		form = MLSsheetForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = MLSsheetForm()
	return render(request,'mlssheet.html',{'form':form,'encabezado':'MLS Sheet / Attachment Request'})

@login_required
def pendingmlssheet(request):
	mlssheets = CreateMLSsheet.objects.filter(completed__isnull = True)
	return render(request,'pendingmlssheet.html',{'mlssheets':mlssheets,
		'encabezado':'MLS Sheets / Attachments to be Done'})

@login_required
def detailsmlssheet(request, mlssheet_id):
	mlssheet=get_object_or_404(CreateMLSsheet, pk=mlssheet_id)
	return render(request, 'mlssheetdetails.html',{'mlssheet':mlssheet, 'encabezado':mlssheet.address})

@login_required
def completedmlssheet(request, mlssheet_id):
	mlssheet=get_object_or_404(CreateMLSsheet, pk=mlssheet_id)
	if request.method == 'POST':
		mlssheet.completed = datetime.now()
		mlssheet.completed_by = request.user
		mlssheet.save()
		return redirect('mlssheet details', mlssheet_id=mlssheet.id)
	return render(request, 'mlssheetdetails.html',{'mlssheet':mlssheet, 'encabezado':mlssheet.address})

def mlssearch(request):
	if request.method == "POST":
		form = SearchForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = SearchForm()

	return render(request, 'mlssearch.html',{'form':form,'encabezado':'MLS Search Request'})

@login_required
def pendingmlssearch(request):
	mlssearches = CreateSearch.objects.filter(completed__isnull = True)
	return render(request, 'pendingmlssearch.html',{'mlssearches':mlssearches,
		'encabezado':'MLS Search Pending to be Done'})

@login_required
def detailsmlssearch(request, mlssearch_id):
	mlssearch = get_object_or_404(CreateSearch,pk = mlssearch_id)
	return render(request, 'mlssearchdetails.html', {'mlssearch':mlssearch,
		'encabezado':mlssearch.full_name})
@login_required
def completedmlssearch(request, mlssearch_id):
	mlssearch = get_object_or_404(CreateSearch,pk = mlssearch_id)
	if request.method == "POST":
		mlssearch.completed = datetime.now()
		mlssearch.completed_by = request.user
		mlssearch.save()
		return redirect('mlssearch details', mlssearch_id=mlssearch.id)
	return render(request, 'mlssearchdetails.html', {'mlssearch':mlssearch,
		'encabezado':mlssearch.full_name})

def dotloop(request):
	if request.method == 'POST':
		form = DotloopForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	else:
		form = DotloopForm()

	return render(request, 'dotloop.html', {'form':form,
		'encabezado':"Dorloop Request"})

@login_required
def pendingdotloop(request):
	dotloops = CreateDotloop.objects.filter(completed__isnull = True)
	return render(request,'pendingdotloop.html',{'dotloops':dotloops,
		'encabezado':"Dotloop Request Pending to be Done"})

@login_required
def detailsdotloop(request, dotloop_id):
	dotloop = get_object_or_404(CreateDotloop, pk = dotloop_id)
	return render(request,'dotloopdetails.html',{'dotloop':dotloop,'encabezado':dotloop.address})
		
def completeddotloop(request, dotloop_id):
	dotloop = get_object_or_404(CreateDotloop, pk = dotloop_id)
	if request.method == "POST":
		dotloop.completed = datetime.now()
		dotloop.completed_by = request.user
		dotloop.save()
		return redirect('dotloop details',dotloop_id=dotloop.id)
	return render(request,'dotloopdetails.html',{'dotloop':dotloop,'encabezado':dotloop.address})
