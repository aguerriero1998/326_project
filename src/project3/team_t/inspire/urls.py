from django.urls import path
from . import views

urlpatterns = [
              
               path("class-search/", views.class_search, name="class_search"),
                path("search-results/", views.search_results_general, name="search_results"),
               #path("search-results/", views.search_results_major, name="search_results"),
               #path("search-results/", views.search_results_gened, name="search_results"),
               
    path("students/", views.StudentListView.as_view(), name="student_list"),
    path("courses/", views.CourseListView.as_view(), name="course_list"),
    path("course-instances/", views.CourseInstanceListView.as_view(), name="course_instance_list"),

    path("course/<int:pk>", views.CourseDetailView.as_view(), name="course_info"),
    path("course-instance/<int:pk>", views.CourseInstanceDetailView.as_view(), name="course_instance_info"),
    path("course-review/<int:pk>", views.AddCourseReview, name="add_a_review"),
    path("course-review/success", views.Review_Success, name="review_success"),
               
    


    path("professor/<str:pk>", views.ProfessorDetailView.as_view(), name="professor_info"),
    path("professors/", views.ProfessorListView.as_view(), name="professor_list"),
    path("professor/<str:pk>/review", views.AddProfessorReview, name="add_professor_review"),
    path("professor/<str:pk>/success", views.AddProfessorReviewSuccess, name="professor_review_success"),

    path("<int:pk>", views.Schedule.as_view(), name="dashboard"),
    path("shopping-cart/<int:pk>", views.ShoppingCartView.as_view(), name="shopping_cart"),
    path("student-info/<int:pk>", views.StudentDetailView.as_view(), name="student_info"),
     path("student-info/<int:pk>/edit", views.editInfo, name="edit_info"),
    path("unenroll-classes/", views.unenroll_classes, name="unenroll"),
    path("enroll-classes/", views.enroll_classes, name="enroll"),
    path("add-to-shopping-cart/", views.add_to_shopping_cart, name="add_to_shopping_cart"),
              
               
    
               
    
    
               
               
    

    path("add-course", views.add_course, name="add_course"),

    path("", views.index, name="index"),
    
    
]
