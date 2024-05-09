from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, decorators
from django.shortcuts import render
from django.http import HttpResponse
from .models import Instructor, Department, Article
from collections import defaultdict
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

def display_message(request):
    return render(request, 'pages/message.html')

class LoginClass(View):
    def get(self, request):
        return render(request, template_name='pages/loginPage.html')
    
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_staff:
                login(request, user)
                next_url = request.GET.get('next', 'home')
                return redirect(next_url)
            elif user.is_active:
                login(request, user)
                url_instruction = f'/instructor/{user.username}/'  # Sử dụng user.username để lấy id
                next_url = request.GET.get('next', url_instruction)
                return redirect(next_url)
            else:
                error_message = "Tài khoản không hợp lệ hoặc không có quyền truy cập."
                return render(request, 'pages/loginPage.html', {'error_message': error_message})
        else:
            error_message = "Tên người dùng hoặc mật khẩu không đúng."
            return render(request, 'pages/loginPage.html', {'error_message': error_message})

   

class HomeClass(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        instructors = Instructor.objects.all()
        departments = Department.objects.all()
        # đếm số giảng viên đang dạy
        teaching_instructors_count = Instructor.objects.filter(status='Đang dạy').count()
        # đếm số lượng giảng viên có học vị là tiến sĩ
        retired_instructors_count = Instructor.objects.filter(status='Nghỉ hưu').count()
        #Lấy các trạng thái của giảng viên
        unique_statuses = Instructor.STATUS_CHOICES
        # Tạo một dictionary để lưu trữ số lượng giảng viên theo từng status trong từng khoa
        status_counts_by_department = {}
        for department in departments:
            instructor_qs = Instructor.objects.filter(department=department)
            # tạo cái dic đếm số lượng mỗi status trong từng khoa
            status_counts = {status[0]: 0 for status in unique_statuses}
            for instructor in instructor_qs:
                status_counts[instructor.status] += 1
            status_counts_by_department[department.name] = status_counts

        return render(request, 'pages/index.html', {
            'instructor_count': instructors.count(), 
            'department_count': departments.count(),
            'teaching_instructors_count': teaching_instructors_count,
            'retired_instructors_count': retired_instructors_count,
            'department_names': [department.name for department in departments],
            'status_counts_by_department': status_counts_by_department,
            'unique_statuses': [status[0] for status in unique_statuses],
          
        })

class InstructorManagement(LoginRequiredMixin, View):
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
                return redirect('instmanage')
            except Instructor.DoesNotExist as e:
                return HttpResponse('lỗi {e}')   
        elif 'form2-submit' in request.POST:
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
                # tạo tài khoản cho giảng viên
                instructor = Instructor.objects.get(email=email)

                username = instructor.instructorID 
                password = '1111'
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('instmanage')
            except Exception as e:
                HttpResponse('Lỗi !!! Không thể thêm giảng viên được')
        elif 'delete-instructor-submit' in request.POST:
            instructor_id = request.POST.get('instructor_id')  # Đảm bảo có trường hidden để truyền instructor_id vào POST request
            try:
                instructor = Instructor.objects.get(instructorID=instructor_id)
                instructor.delete()
                # xóa tài khoản giảng viên
                user = User.objects.get(username=instructor_id)
                user.delete()
                return redirect('instmanage') 
            except Instructor.DoesNotExist:
                return HttpResponse('Không tìm thấy giảng viên')
            except Exception as e:
                return HttpResponse(f'Lỗi: {e}')
        return redirect('instmanage')

class InstructorDetailView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, instructor_id):  # Thêm instructor_id vào phương thức get
        try:
            instructor = Instructor.objects.get(instructorID=instructor_id)
            return render(request, 'pages/thongTinGiangVien.html', {'instructor': instructor})
        except Instructor.DoesNotExist:
            return HttpResponse('Không tìm thấy giảng viên')
        except Exception as e:
            return HttpResponse(f'Lỗi: {e}')
      
# trang diễn đàn để đăng bài báo có thông tin của model Article
class ArticlePost(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request):
        articlepost = Article.objects.all()
        return render(request, 'pages/baiBao.html', {'articlepost': articlepost})

    def post(self, request):
        title = request.POST.get('title')
        author_id = request.POST.get('author_id')
        author = Instructor.objects.get(instructorID=author_id)
        image = request.FILES.get('image')
        content = request.POST.get('content')
        publish_date = request.POST.get('publish_date')
        Article.objects.create(title=title, author=author, image=image, content=content, publish_date=publish_date)
        return redirect('articlepost')

class ArticleDetailView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, instructor_id):
        try:
            articles = Article.objects.filter(author_id=instructor_id)  
            return render(request, 'pages/dienDan.html', {'articles': articles})
        except Article.DoesNotExist:
            return HttpResponse('Không có bài báo')
        except Exception as e:
            return HttpResponse(f'Lỗi: {e}')

