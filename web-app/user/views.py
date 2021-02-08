from django.shortcuts import render, redirect
from django.contrib import messages
from .form import UserRegisterForm, rideCreationForm, driverRegisterForm, UserUpdateForm, DriverUpdateForm, startTimeEditForm, areaEditForm, destinationEditForm, passengerNumEditForm, shareableEditForm, search_share_Form, search_unconfirmed_Form
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import driver, ride
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import (
  ListView,
)
from django.utils import timezone
from datetime import timedelta, datetime
from django.core.mail import send_mail


@login_required
def userMain(request):
    context = {
      'ridesOwn' : ride.objects.filter(ownerId = request.user.id, completed = False, startTime__gte = timezone.now()).order_by('startTime', 'passengerNum'), # rides is query
      'ridesShare' : ride.objects.filter(user = request.user, completed = False, startTime__gte = timezone.now()).exclude(ownerId = request.user.id).exclude(driverId = request.user.id).order_by('startTime', 'passengerNum'),
    }
    return render(request, 'user/userMain.html', context)

@login_required
def driverMain(request):
    context = {
      'rides' : ride.objects.filter(completed = False, driverId = request.user.driver.id).order_by('startTime', 'passengerNum'), # rides is query
      'carType' : request.user.driver.carType,
      'plateNum' : request.user.driver.plateNum,
      'capacity' : request.user.driver.capa,
    }
    return render(request, 'user/driverMain.html', context)



    
def register(request):
    if request.method == 'POST':
      form = UserRegisterForm(request.POST)
      if form.is_valid():
          driver_ins = driver(user = form.save())
          driver_ins.save()
          username = form.cleaned_data.get('username')
          email = form.cleaned_data.get('email')
          messages.success(request, f'account for user name {username} has been created, your email is {email}')
          return redirect('login')
    else:
         form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})

def success(request):
    return render(request, 'user/success.html')
    
@login_required
def rideCreation(request):
    if request.method == 'POST':
      r_form = rideCreationForm(request.POST)
      if r_form.is_valid():
          if r_form.cleaned_data.get('startTime') <= timezone.now():
              messages.error(request, f'Invalid startTime, the ride start time needs to be later than now')
              r_form = rideCreationForm()
              return render(request, 'user/rideCreation.html', {'r_form': r_form})
          else:
            ride_ins = r_form.save()
            ride_ins.user.add(request.user)
            ride_ins.ownerId = request.user.id 
            messages.success(request, f'valid rideform saved')
            ride_ins.save()
            return redirect('userMain')
    else:
         r_form = rideCreationForm()
    return render(request, 'user/rideCreation.html', {'r_form': r_form})
    
@login_required
def driverRegister(request):
    if request.method == 'POST':
      d_form = driverRegisterForm(request.POST, instance = request.user.driver)
      if d_form.is_valid():
          driver_ins = d_form.save()
          driver_ins.isDriver = True
          driver_ins.save()
          messages.success(request, f'valid driver form saved')
          return redirect('driverMain')
    else:
         d_form = driverRegisterForm()
         return render(request, 'user/driverRegister.html', {'d_form': d_form})
         
@login_required
def userUpdate(request):
    if request.method == 'POST':
      uu_form = UserUpdateForm(request.POST, instance = request.user)
      if uu_form.is_valid():
          uu_form.save()
          username = uu_form.cleaned_data.get('username')
          messages.success(request, f'user {{username}} info updated')
          return redirect('userMain')
    else:
         uu_form = UserUpdateForm()
    return render(request, 'user/userUpdate.html', {'uu_form': uu_form})
    
@login_required
def driverUpdate(request):
    if request.method == 'POST':
      du_form = DriverUpdateForm(request.POST, instance = request.user.driver)
      if du_form.is_valid():
          du_form.save()
          messages.success(request, f'driver info updated')
          return redirect('driverMain')
    else:
         du_form = DriverUpdateForm()
    return render(request, 'user/driverUpdate.html', {'du_form': du_form})
    
@login_required
def startTimeEdit(request, user_id, ride_id):
    ride_ins = ride.objects.filter(id = ride_id)[0]
    if user_id != ride_ins.ownerId:
      return redirect('userMain')
    if request.method == 'POST':
      st_form = startTimeEditForm(request.POST, instance = ride.objects.filter(id = ride_id)[0])
      if st_form.is_valid():
          st_form.save()
          messages.success(request, f'start time updated')
          return redirect('userMain')
    else:
         st_form = startTimeEditForm()
    return render(request, 'user/startTimeEdit.html', {'st_form': st_form})

@login_required
def areaEdit(request, user_id, ride_id):
     ride_ins = ride.objects.filter(id = ride_id)[0]
     if user_id != ride_ins.ownerId:
      return redirect('userMain')
     if request.method == 'POST':
        a_form = areaEditForm(request.POST, instance = ride.objects.filter(id = ride_id)[0])
        if a_form.is_valid():
          a_form.save()
          messages.success(request, f'area updated')
          return redirect('userMain')
     else:
         a_form = areaEditForm()
     return render(request, 'user/areaEdit.html', {'a_form': a_form})

@login_required
def destinationEdit(request, user_id, ride_id):
     ride_ins = ride.objects.filter(id = ride_id)[0]
     if user_id != ride_ins.ownerId:
       return redirect('userMain')
     if request.method == 'POST':
        des_form = destinationEditForm(request.POST, instance = ride.objects.filter(id = ride_id)[0])
        if des_form.is_valid():
          des_form.save()
          messages.success(request, f'destination updated')
          return redirect('userMain')
     else:
         des_form = destinationEditForm()
     return render(request, 'user/destinationEdit.html', {'des_form': des_form})

@login_required
def passengerNumEdit(request, user_id, ride_id):
    ride_ins = ride.objects.filter(id = ride_id)[0]
    if user_id != ride_ins.ownerId:
       return redirect('userMain')
    if request.method == 'POST':
      pn_form = passengerNumEditForm(request.POST, instance = ride.objects.filter(id = ride_id)[0])
      if pn_form.is_valid():
          pn_form.save()
          messages.success(request, f'passenger number updated')
          return redirect('userMain')
    else:
         pn_form = passengerNumEditForm()
    return render(request, 'user/passengerNumEdit.html', {'pn_form': pn_form})

@login_required
def shareableEdit(request, user_id, ride_id):
    ride_ins = ride.objects.filter(id = ride_id)[0]
    if user_id != ride_ins.ownerId:
      return redirect('userMain')
    if request.method == 'POST':
      share_form = shareableEditForm(request.POST, instance = ride.objects.filter(id = ride_id)[0])
      if share_form.is_valid():
          share_form.save()
          messages.success(request, f'shareable status updated')
          return redirect('userMain')
    else:
         share_form = shareableEditForm()
    return render(request, 'user/shareableEdit.html', {'share_form': share_form})
     
     
@login_required
def searchShareableRide(request):
     if request.method == 'POST':
      search_share_form = search_share_Form(request.POST)
      if search_share_form.is_valid():#用form的信息找符合条件的rides（starttime lastest starttime， passengernum）
          start = search_share_form.cleaned_data.get('startTime')
          if start <= timezone.now():
              messages.error(request, f'Invalid start time，the ride start time needs to be later than now')
              search_share_form = search_share_Form()
              return render(request, 'user/searchShareableRide.html', {'search_share_form': search_share_form})
          else:
              end = search_share_form.cleaned_data.get('latestStartTime')
              requestArea = search_share_form.cleaned_data.get('area')
              requestPassengerNum = search_share_form.cleaned_data.get('passengerNum')
              help_num = 6 - requestPassengerNum
              context = {
                'rides' : ride.objects.filter( confirmed = False, startTime__gte = start, startTime__lte = end, area = requestArea, passengerNum__lte = help_num, shareable = True).exclude(user = request.user).order_by('startTime', 'passengerNum'),
                'passengerNum' : requestPassengerNum,
              }
              messages.success(request, f'valid search request')
              return render(request, 'user/showShareableRide.html', context)#将rides， passengernum传入下一页面，选择后ride的passengerNum增加
     else:
         search_share_form = search_share_Form()
     return render(request, 'user/searchShareableRide.html', {'search_share_form': search_share_form})
     
@login_required
def searchUnconfirmedRide(request):
     if request.method == 'POST':
      search_unconfirmed_form = search_unconfirmed_Form(request.POST)
      if search_unconfirmed_form.is_valid():#用form的信息找符合条件的rides（starttime lastest starttime， passengernum）
          start = search_unconfirmed_form.cleaned_data.get('startTime')
          if start <= timezone.now():
              messages.error(request, f'Invalid start time，the ride start time needs to be later than now')
              search_unconfirmed_form = search_unconfirmed_Form()
              return render(request, 'user/searchUnconfirmedRide.html', {'search_unconfirmed_form': search_unconfirmed_form})
          else:
            end = search_unconfirmed_form.cleaned_data.get('latestStartTime')
            requestArea = search_unconfirmed_form.cleaned_data.get('area')
            context = {
            'rides' : ride.objects.filter(confirmed = False, startTime__gte = start, startTime__lte = end, area = requestArea, passengerNum__lte = (request.user.driver.capa-1)).exclude(user = request.user).order_by('startTime', 'passengerNum'),
    }
            messages.success(request, f'valid search request')
            return render(request, 'user/showUnconfirmedRide.html', context)
     else:
         search_unconfirmed_form = search_unconfirmed_Form()
     return render(request, 'user/searchUnconfirmedRide.html', {'search_unconfirmed_form': search_unconfirmed_form})

    
@login_required
def share_success(request, passengerNum, ride_id):
    ride_ins = ride.objects.filter(id = ride_id)[0]
    ride_ins.user.add(request.user)
    ride_ins.passengerNum += passengerNum
    ride_ins.save()
    return render(request, 'user/share_success.html')
    
@login_required
def confirm_success(request, ride_id):
    ride_ins = ride.objects.filter(id = ride_id)[0]
    if ride_ins.driverId == 0:
      ride_ins.user.add(request.user)
      ride_ins.driverId = request.user.driver.id
      ride_ins.confirmed = True
      ride_ins.driverName = request.user.username
      ride_ins.carType = request.user.driver.carType
      ride_ins.plateNum = request.user.driver.plateNum
      ride_ins.save()
      email_list = []
      for us in ride_ins.user.all():
        email_list.append(us.email)
      send_mail('Ride confirmed', 'Your ride starting at:'+ "\n" + ride_ins.startTime.strftime('%a %H:%M  %d/%m/%y') + "\n" +  'to:' + "\n" +  ride_ins.destination + "\n" + 'has been confirmed'+ "\n" + 'there are ' + "\n" + str(ride_ins.passengerNum) + "\n" + 'passengers who have joined this ride, enjoy your journey!', None, email_list, fail_silently=False)
      messages.success(request, f'Email have been successfully sent to passengers')
      return render(request, 'user/confirm_success.html')
    else:
      messages.error(request, f'Sorry, this ride has been confirmed by other driver!')
      return redirect('driverMain')
    
@login_required
def complete_success(request, ride_id):
    ride_ins = ride.objects.filter(id = ride_id)[0]
    if  timezone.now() <= timedelta(minutes = 10) + ride_ins.startTime: 
        messages.error(request, f'You should not complete a ride before 10 minutes after the start time of this ride')
        return redirect('driverMain')
    ride_ins.completed = True
    ride_ins.save()
    messages.success(request, f'You have successfully completed a ride! Congratulations!')
    return redirect('driverMain')