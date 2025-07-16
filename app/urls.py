from django.urls import path
from .views import Register,Login,Logout,AddProjects,GetProject,SingleProject,EditProject,DeleteProject,AddTask,GetTask,SingleTask,EditTask,DeleteTask,AddComment,GetComment,SingleComment,EditComment,DeleteComment,AddAuditlog,GetAuditlog,SingleAuditlog,EditAuditlog,DeleteAuditlog

urlpatterns = [
    path('register/',Register.as_view(),name='register'),
    path('login/',Login.as_view(),name='login'),
    path('logout/',Logout.as_view(),name='logout'),
    path('add_projects/',AddProjects.as_view(),name='add_projects'),
    path('get_project/',GetProject.as_view(),name='get_project'),
    path('single_project/<int:project_id>',SingleProject.as_view(),name='single_project'),
    path('edit_project/<int:project_id>',EditProject.as_view(),name='edit_project'),
    path('delete_project/<int:project_id>',DeleteProject.as_view(),name='delete_project'),
    path('add_task/',AddTask.as_view(),name='add_task'),
    path('get_task/',GetTask.as_view(),name='get_task'),
    path('single_task/<int:task_id>',SingleTask.as_view(),name='single_task'),
    path('edit_task/<int:task_id>',EditTask.as_view(),name='edit_task'),
    path('delete_task/<int:task_id>',DeleteTask.as_view(),name='delete_task'),
    path('add_comment/',AddComment.as_view(),name='add_comment'),
    path('get_comment/',GetComment.as_view(),name='get_comment'),
    path('single_comment/<int:comment_id>',SingleComment.as_view(),name='single_comment'),
    path('edit_comment/<int:comment_id>',EditComment.as_view(),name = 'edit_comment'),
    path('delete_comment/<int:comment_id>',DeleteComment.as_view(),name='delete_comment'),
    path('add_auditlog/',AddAuditlog.as_view(),name='add_auditlog'),
    path('get_auditlog/',GetAuditlog.as_view(),name='get_auditlog'),
    path('single_auditlog/<int:auditlog_id>',SingleAuditlog.as_view(),name='single_auditlog'),
    path('edit_auditlog/<int:auditlog_id>',EditAuditlog.as_view(),name='edit_auditlog'),
    path('delete_auditlog/<int:auditlog_id>',DeleteAuditlog.as_view(),name='delete_auditlog')
]