from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Project, ProjectMember, Task, TaskAssignee

# ✅ Register the Custom User Model
class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ('id', 'username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {'fields': ('username', 'email', 'password1', 'password2', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    search_fields = ('username', 'email')
    ordering = ('id',)

# ✅ Register Project Model
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status', 'start_date', 'end_date', 'created_by')
    list_filter = ('status',)
    search_fields = ('name', 'description')

# ✅ Register Project Member Model
class ProjectMemberAdmin(admin.ModelAdmin):
    list_display = ('id', 'project', 'user', 'role')
    list_filter = ('role',)
    search_fields = ('project__name', 'user__username')

# ✅ Register Task Model
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'project', 'priority', 'status', 'due_date')
    list_filter = ('priority', 'status')
    search_fields = ('title', 'description')

# ✅ Register Task Assignee Model
class TaskAssigneeAdmin(admin.ModelAdmin):
    list_display = ('id', 'task', 'user')
    search_fields = ('task__title', 'user__username')

# 🔹 Registering models to Django Admin
admin.site.register(User, CustomUserAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectMember, ProjectMemberAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskAssignee, TaskAssigneeAdmin)
