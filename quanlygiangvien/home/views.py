from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, decorators
from django.shortcuts import render
from django.http import HttpResponse
from .models import Instructor, Department

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

def display_message(request):
    # Truyền thông báo vào template để hiển thị
   
    return render(request, 'pages/message.html')
class LoginClass(View):
    def get(self, request):
        return render(request, template_name='pages/loginPage.html')
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next', 'home')
            return redirect(next_url)
        else:
            error_message = "Tên người dùng hoặc mật khẩu không đúng."
            return render(request, 'pages/loginPage.html', {'error_message': error_message})
   

class HomeClass(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        instructor_count = Instructor.objects.count()
        department_count = Department.objects.count()
        return render(request, 'pages/index.html', {'instructor_count': instructor_count, 'department_count': department_count})

class InstructorView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request):
        instructor_list = Instructor.objects.all()
        department_choices = Instructor.DEPARTMENT_CHOICES
        education_choices=Instructor.EDUCATIONLEVEL_CHOICES
        position_choices = Instructor.POSITION_CHOICES
        status_choices = Instructor.STATUS_CHOICES
       
        return render(request, 'pages/quanLyGiangVienPages.html', {'instructor_list': instructor_list,'department_choices':department_choices, 'education_choices': education_choices,'position_choices':position_choices, 'status_choices':status_choices})
    def post(self, request):
        if 'form1-submit' in request.POST:
            instructor_ID =request.POST.get('ID')
            try:
                instructor = Instructor.objects.get(instructorID=instructor_ID)
                instructor.name = request.POST.get('name')
                instructor.gender = request.POST.get('gender')
                instructor.date_of_birth = request.POST.get('birthdate')
                instructor.phone = request.POST.get('phonenumber')
                instructor.place_of_birth = request.POST.get('placeoforigin')
                instructor.email = request.POST.get('email')
     
                instructor.education_level = request.POST.get('education')
                instructor.job_position = request.POST.get('position')
                instructor.status = request.POST.get('status')
                instructor.save()
                return redirect('instructor')
            except Instructor.DoesNotExist as e:
                return HttpResponse('lỗi {e}')
        
        elif 'form2-submit' in request.POST:
            error_messages =[]
            avt= request.POST.get('avt')
            name = request.POST.get('name')
            gender = request.POST.get('gender')
            date_of_birth = request.POST.get('birthdate')
            phone = request.POST.get('phone')
            place_of_birth = request.POST.get('placeoforigin')
            email = request.POST.get('email')
            department_value = request.POST.get('department')
            
            
            education_level = request.POST.get('education')
            job_position = request.POST.get('position')
            status = request.POST.get('status')
                
                
            if not avt:
                error_messages.append("Vui lòng cung cấp avatar.")
                # return redirect('instructor')
            if not name:
                error_messages.append("Vui lòng nhập tên.")
                # return redirect('instructor')
            if not gender:
                error_messages.append("Vui lòng cung cấp giới tính.")
                # return redirect('instructor')
            if not date_of_birth:
                error_messages.append("Vui lòng cung cấp ngày sinh.")
                # return redirect('instructor')
            if not phone:
                error_messages.append("Vui lòng cung cấp số điện thoại.")
                # return redirect('instructor')
            if not place_of_birth:
                error_messages.append("Vui lòng cung cấp số nơi sinh.")
                # return redirect('instructor')
            if not email:
                error_messages.append("Vui lòng cung cấp email.")
                # return redirect('instructor')
            if not department_value or department_value=='':
                error_messages.append("Vui lòng cung cấp tên khoa.")
                # return redirect('instructor')
            if not education_level or education_level=='':
                error_messages.append("Vui lòng cung cấp học vị.")
                # return redirect('instructor')
            if not job_position or job_position=='':
                error_messages.append("Vui lòng cung cấp chức vụ.")
                # return redirect('instructor')
            if not status or status=='':
                error_messages.append("Vui lòng cung cấp trạng thái.")
                # return redirect('instructor')
            if not error_messages:
                try:
                    department = Department.objects.get(departmentID=department_value)
                    Instructor.objects.create(
                    image =avt,
                    name=name,
                    gender=gender,
                    date_of_birth=date_of_birth,
                    phone=phone,
                    place_of_birth=place_of_birth,
                    email=email,
                    department=department,
                    education_level=education_level,
                    job_position=job_position,
                    status=status
                    )
                    return redirect('instructor')
                except Department.DoesNotExist:
                    error_messages.append("Phòng ban không tồn tại.")
                    return render(request, 'pages/message.html', {'error_messages': error_messages})
                except Exception as e:
                    error_messages.append(f'Lỗi: {e}')
            return render(request, 'pages/message.html', {'error_messages': error_messages})
        return redirect('instructor')

