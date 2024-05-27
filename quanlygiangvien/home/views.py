from django.shortcuts import redirect
from django.contrib.auth.decorators import user_passes_test
import requests
from django.utils import timezone
from django.contrib.auth import authenticate, login, decorators
from django.shortcuts import render
from django.http import HttpResponse
from .models import Instructor, Department, Article
from collections import defaultdict
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.urls import reverse

def is_staff(user):
    return user.is_authenticated and user.is_staff

def display_message(request):
    return render(request, 'pages/message.html')

class LoginClass(View):
    def get(self, request):
        return render(request, template_name='html/LoginPage.html')
    
    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        # Lookup the Instructor object using the username
        
        if user is not None:
            if user.is_staff :
                login(request, user)
                next_url = request.GET.get('next','home')
                return redirect(next_url)
            elif user.is_active:
                login(request, user)
                url_instruction = f'/instructor/{user.username}/'  # Sử dụng user.username để lấy id
                next_url = request.GET.get('next', url_instruction)
                return redirect(next_url)
            else:
                error_message = "Tài khoản không hợp lệ hoặc không có quyền truy cập."
                return render(request, 'pages/LoginPage.html', {'error_message': error_message})
        else:
            
            return render(request, 'html/LoginPage.html')

# @user_passes_test(is_staff, login_url='/login/')
class HomeClass(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        user = request.user
        if user.is_staff:
            education_choices=Instructor.EDUCATIONLEVEL_CHOICES
            position_choices = Instructor.POSITION_CHOICES
            status_choices = Instructor.STATUS_CHOICES
            instructors = Instructor.objects.all()
            departments = Department.objects.all()
            article = Article.objects.all()
            instructor_list = []
            for instructor in instructors:
                instructor_list.append({
                    'instructorID': instructor.instructorID,
                    'name': instructor.name,
                    'gender': instructor.gender,
                    'date_of_birth': instructor.date_of_birth,
                    'phone': instructor.phone,
                    'place_of_birth': instructor.place_of_birth,
                    'email': instructor.email,
                    'department': instructor.department,
                    'education_level': instructor.education_level,
                    'job_position': instructor.job_position,
                    'status': instructor.status,
                    'image': instructor.image.url if instructor.image else '',  # Add the full image URL
                    
                })
            return render(request, 'html/HomePage.html', {
                'instructor_list': instructor_list,
                'instructor_count': instructors.count(), 
                'department_count': departments.count(),
                'article_count': article.count(),
                'department_names': [department.name for department in departments],
                'user': user,
                'department_choices':departments, 
                'education_choices': education_choices,
                'position_choices':position_choices, 
                'status_choices':status_choices
            
            })
    def post(self, request):
        if 'form-submit' in request.POST or 'form-submit' in request.FILES:
          
            instructor_ID =request.POST.get('ID')
            try:
                instructor = Instructor.objects.get(instructorID=instructor_ID)
                if request.FILES.get('avt'):
                    instructor.image = request.FILES.get('avt')
                
                instructor.name = request.POST.get('name')
                instructor.gender = request.POST.get('gender')
                instructor.date_of_birth = request.POST.get('birthdate')
                instructor.phone = request.POST.get('phone')
                instructor.place_of_birth = request.POST.get('placeoforigin')
                instructor.email = request.POST.get('email')
                department_id = request.POST.get('department')
                if department_id:
                    try:
                        department = Department.objects.get(departmentID=department_id)
                        instructor.department = department
                    except Department.DoesNotExist:
                        return HttpResponse('Department not found')
                else:
                    return HttpResponse('No department selected')
                instructor.education_level = request.POST.get('education')
                instructor.job_position = request.POST.get('position')
                instructor.status = request.POST.get('status')
                instructor.save()
                return redirect('home')
            except Instructor.DoesNotExist as e:
                return HttpResponse('lỗi {e}')   
        elif 'form2-submit' in request.POST or 'form2-submit' in request.FILES:
    
            avt= request.FILES.get('avt') 
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
                return redirect('home')
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
                return redirect('home') 
            except Instructor.DoesNotExist:
                return HttpResponse('Không tìm thấy giảng viên')
            except Exception as e:
                return HttpResponse(f'Lỗi: {e}')
        return redirect('home')

class ForumView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    # đăng tất cả bài viết trong forum
    def get(self, request):
        user = request.user
        articles = Article.objects.all()
        if user.is_staff:
            return render(request, 'html/ForumPage.html', {'articles': articles})
        else:
            instructor = Instructor.objects.get(instructorID=user.username)
            instructor_name = instructor.name
            return render(request, 'html/ForumPage.html', {'articles': articles, 'instructor_name': instructor_name})
        
    def post(self, request):
        if 'create-submit' in request.POST or 'create-submit' in request.FILES:
            title = request.POST.get('title')
            author_id = request.user.username
            author = Instructor.objects.get(instructorID=author_id)
            upload_file = request.FILES.get('fileUpload')
            image = request.FILES.get('imageUpload')
            content = request.POST.get('content')
            publish_date = timezone.now()
            article = Article.objects.create(title=title, 
                                             author=author, 
                                             image=image, 
                                             content=content,
                                             publish_date=publish_date,
                                             upload_file = upload_file)
            article.save()
            return redirect('forumad')
        return redirect('forumad')

# cái bài viết của user đã đăng
class myForum(LoginRequiredMixin, View):
    login_url = '/login/'
    def get(self, request):
        user = request.user
        articles = Article.objects.filter(author=request.user.username)
        if user.is_staff:
            return render(request, 'html/MyPostPage.html', {'articles': articles, 'user': user})
        else:
            instructor = Instructor.objects.get(instructorID=user.username)
            instructor_name = instructor.name
            return render(request, 'html/MyPostPage.html', {'articles': articles, 'user': user,'instructor_name': instructor_name})
        
    def post(self, request):
        if 'create-submit' in request.POST or 'create-submit' in request.FILES:
            title = request.POST.get('title')
            author_id = request.user.username
            author = Instructor.objects.get(instructorID=author_id)
            upload_file = request.FILES.get('fileUpload')
            image = request.FILES.get('imageUpload')
            content = request.POST.get('content')
            publish_date = timezone.now()
            article = Article.objects.create(title=title, 
                                             author=author, 
                                             image=image, 
                                             content=content,
                                             publish_date=publish_date,
                                             upload_file = upload_file)
            article.save()
            return redirect('myforum')
        return redirect('myforum')



# Hiển thị thông tin chi tiết của giảng viên
class InstructorDetailView(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, instructor_id):  # Thêm instructor_id vào phương thức get
        try:
            instructor = Instructor.objects.get(instructorID=instructor_id)
            return render(request, 'html/InstructorInfo.html', {'instructor': instructor})
        
        except Instructor.DoesNotExist:
            return HttpResponse('Không tìm thấy giảng viên')
        except Exception as e:
            return HttpResponse(f'Lỗi: {e}')
      
# trang diễn đàn để đăng bài báo có thông tin của model Article
class ArticlePost(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, instructor_id):
        # phân quyền chỉ có giảng viên mới đăng bài được
        if request.user.is_staff:
            return HttpResponse('Chỉ giảng viên mới được phép đăng bài báo.')
        elif request.user.is_active:
            article = Article.objects.all()
            instructor = Instructor.objects.get(instructorID=instructor_id)
            return render(request, 'html/MyPostPage.html', {'article': article, 'instructor': instructor})

    def post(self, request):
        title = request.POST.get('title')
        author_id = request.user.username
        author = Instructor.objects.get(instructorID=author_id)
        image = request.FILES.get('imageUpload')
        upload_file = request.FILES.get('fileUpload')
        content = request.POST.get('content')
        publish_date = request.POST.get('publish_date')
        Article.objects.create(title=title, author=author, image=image, upload_file=upload_file, content=content, publish_date=publish_date)
        url_instruction = f'/article/{author_id}/' 
        next_url = request.GET.get('next', url_instruction)
        return redirect(next_url)

class ArticleDetailView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request, instructor_id):
        if request.user.is_staff:
            return HttpResponse('Chỉ giảng viên mới có bài báo.')
        elif request.user.is_active:
            
            if instructor_id is None:
                # Nếu không có instructor_id được cung cấp, chuyển hướng đến URL có instructor_id được lấy từ đầu tiên trong danh sách giảng viên
                first_instructor = Instructor.objects.first()
                if first_instructor:
                    return redirect('article', instructor_id=first_instructor.instructorID)
                else:
                    return HttpResponse('Không có giảng viên nào để hiển thị bài báo.')
            
            try:
                articles = Article.objects.filter(author_id=instructor_id)
                instructor = Instructor.objects.filter(instructorID=instructor_id).first()
                return render(request, 'html/MyPostPage.html', {'articles': articles, 'instructor': instructor})
            except Exception as e:
                return HttpResponse(f'Lỗi: {e}')

# đăng tất cả bài viết trong forum
class ForumDetailViewIns(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, instructor_id):
        articles = Article.objects.all()
        instructor = Instructor.objects.filter(instructorID=instructor_id).first() 
        if not instructor:
            return HttpResponse('Không tìm thấy giảng viên.')
        if not articles:
            return HttpResponse('Không có bài viết nào trong diễn đàn.')
        else:
            return render(request, 'html/ForumIns.html', {'articles': articles, 'instructor': instructor})
    

# chi tiết bài báo (Giảng viên xem)     
class ArticleViewIns(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, instructor_id, article_id):
        article = Article.objects.filter(articleID = article_id).first() 
        instructor = Instructor.objects.filter(instructorID=instructor_id).first() 
        if not instructor:
            return HttpResponse('Không tìm thấy giảng viên.')
        if not article:
            return HttpResponse('Không có bài viết nào trong diễn đàn.')
        else:
            return render(request, 'html/ArticleDetailIns.html', {'article': article, 'instructor': instructor})

# chi tiết bài báo (Admin xem)     
class ArticleViewAdmin(LoginRequiredMixin, View):
    login_url = '/login/'
    
    def get(self, request, article_id):
        article = Article.objects.filter(articleID = article_id).first() 
        if not article:
            return HttpResponse('Không có bài viết nào trong diễn đàn.')
        else:
            return render(request, 'html/ArticleDetailAdmin.html', {'article': article})
        
# about page admin
class AboutUsAdmin(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.is_staff:
            return render(request, 'html/AboutUs.html', {'user': request.user})

# about page user
class AboutUsIns(View):
    def get(self, request, instructor_id):
        if request.user.is_authenticated and request.user.is_active:
            instructor = Instructor.objects.get(instructorID=instructor_id)
            return render(request, 'html/AboutUsIns.html', {'user': request.user, 'instructor': instructor})
