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

class CourseInstanceInline3(admin.TabularInline):
    model = Student.coursesnow.through
    extra = 1
    
class CourseInstanceInline4(admin.TabularInline):
    model = Student.shoppingcart.through
    extra = 1



@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'coursenumber','description', 'credits', 'rating', 'comments', 'gened', 'major')
#fields = ['name', 'coursenumber', 'description', 'credits', 'rating', 'comments', 'gened', 'major']
    inlines = [CourseInstanceInline2]


@admin.register(CourseInstance)
class CourseInstanceAdmin(admin.ModelAdmin):
    list_display = ('name', 'basecourse','prof','prerequisites' , 'classnumber',  'semester','start','end', 'location', 'textbook','students', 'available')
    inlines = [
        CourseInstanceInline3
    ]
    exclude = ( 'coursesnow', )


    
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display = ('name', 'review' )

    inlines = [CourseInstanceInline1]





@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','idnumber','email','phonenumber', 'gender','pronouns', 'emergency','get_shoppingcart','get_coursestaken')
    #fields = ['name','idnumber','email','phonenumber', 'gender','pronouns', 'emergency','coursestaken','shoppingcart']
    inlines = [CourseInstanceInline3]

admin.site.register(Days)






