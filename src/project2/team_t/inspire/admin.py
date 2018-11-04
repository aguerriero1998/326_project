from django.contrib import admin
from inspire.models import Course, CourseInstance, Professor, Student, Days


class CourseInstanceInline1(admin.TabularInline):
    model = CourseInstance
    fk_name = "prof"

class CourseInstanceInline2(admin.TabularInline):
    model = CourseInstance
    fk_name = "basecourse"

class StudentInline1(admin.TabularInline):
    model = Student
    fk_name = "coursestaken"




@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'coursenumber','description', 'credits', 'rating', 'comments', 'gened', 'major')
#fields = ['name', 'coursenumber', 'description', 'credits', 'rating', 'comments', 'gened', 'major']
    inlines = [CourseInstanceInline2]


@admin.register(CourseInstance)
class CourseInstanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'basecourse','prof','prerequisites' , 'classnumber',  'semester','time', 'location', 'textbook','students', 'available')
#inlines = [StudentInline1]





    
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'review' )

    inlines = [CourseInstanceInline1]
#because courseInstance has foreignkey to professor




@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','idnumber','email','phonenumber', 'gender','pronouns', 'emergency')
    fields = ['name','idnumber','email','phonenumber','gender','pronouns', 'emergency']

admin.site.register(Days)




#course has foreignkey to courseInstance
#CourseInstance has foreignkey to professor and Course
#professor has foreignkey to courseInstance
#Students have foreignkey to course


