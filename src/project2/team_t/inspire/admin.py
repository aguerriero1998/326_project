from django.contrib import admin
from inspire.models import Course, CourseInstance, Professor, Student, Days, CourseReview, ProfessorReview



class CourseInstanceInline2(admin.TabularInline):
    model = CourseInstance
    fk_name = "basecourse"

class CourseInstanceInline3(admin.TabularInline):
    model = Student.coursesnow.through
    extra = 1




@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'coursenumber','description', 'credits', 'rating', 'gened', 'major','get_recommendations')
    #fields = ['name', 'coursenumber', 'description', 'credits', 'rating', 'comments', 'gened', 'major','recommendations']
    inlines = [CourseInstanceInline2]   #basecourse inline


@admin.register(CourseInstance)
class CourseInstanceAdmin(admin.ModelAdmin):

    list_display = ('name', 'basecourse','prof','classnumber','prerequisites' ,  'semester','start', 'end','location', 'textbook','students', 'available','get_days')

    inlines = [
               CourseInstanceInline3
    ]
    exclude = ( 'coursesnow', )


    
@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):

    list_display = ('name', 'rating' )


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','idnumber','email','phonenumber','address', 'gender','pronouns', 'emergency','get_shoppingcart','get_coursestaken')
    #fields = ['name','idnumber','email','phonenumber', 'gender','pronouns', 'emergency','coursestaken','shoppingcart']
    inlines = [CourseInstanceInline3]     #for coursesnow

admin.site.register(Days)

@admin.register(ProfessorReview)
class ProfessorReviewAdmin(admin.ModelAdmin):
    list_display = ('remarks', 'giver', 'professor')

@admin.register(CourseReview)
class CourseReviewAdmin(admin.ModelAdmin):
    list_display = ('remarks', 'giver', 'course')


