from django.core.serializers import serialize
from django.shortcuts import render
from .serializer import RegisterSerializer,LoginSerializer,ProjectSerializer,TaskSerializer,CommentSerializer,AuditLogSerializer
from rest_framework import status
from rest_framework.views import APIView
from .models import User,Project,Task,Comment,AuditLog
from rest_framework.response import Response
from django.contrib.auth import logout


class Register(APIView):
    def post(self,request):
        try:
            serializer = RegisterSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have successfully registered'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Login(APIView):
    def post(self,request):
        try:
            serializer = LoginSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have successfully logged in'},status=status.HTTP_200_OK)
            return Response({'message':'Your login details is wrong. Try registering or logging again!','data':serializer.errors},status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','data':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class Logout(APIView):
    def get(self,request):
        try:
            logout(request)
            return Response({'message':'You have successfully logged out'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddProjects(APIView):
    def post(self,request):
        try:
            serializer = ProjectSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have successfully added a project'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetProject(APIView):
    def get(self,request):
        try:
            project = Project.objects.all()
            serializer = ProjectSerializer(project, many=True)
            return Response({'message':'This are all the projects','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleProject(APIView):
    def get(self,request,project_id):
        try:
            project = Project.objects.get(id=project_id)
            serializer = ProjectSerializer(project)
            return Response({'message':'This the project','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditProject(APIView):
    def put(self,request,project_id):
        try:
            project = Project.objects.get(id=project_id)
            serializer = ProjectSerializer(project, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have successfully edited the project'},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteProject(APIView):
    def delete(self,request,project_id):
        try:
            project = Project.objects.get(id=project_id)
            project.delete()
            return Response({'message':'You have successfully deleted this project'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddTask(APIView):
    def post(self,request):
        try:
            serializer = TaskSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Your task has been added'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetTask(APIView):
    def get(self,respect):
        try:
            task = Task.objects.all()
            serializer = TaskSerializer(task, many=True)
            return Response({'message':'This are all the tasks','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleTask(APIView):
    def get(self,request,task_id):
        try:
            task = Task.objects.get(id=task_id)
            serializer = TaskSerializer(task)
            return Response({'message':'This the task','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditTask(APIView):
    def put(self,request,task_id):
        try:
            task = Task.objects.get(id=task_id)
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'Your task has been edited'},status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteTask(APIView):
    def delete(self,request,task_id):
        try:
            task = Task.objects.get(id=task_id)
            task.delete()
            return Response({'message':'Your task has been deleted'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddComment(APIView):
    def post(self,request):
        try:
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'You have successfully dropped a comment'},status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetComment(APIView):
    def get(self,request):
        try:
            comment = Comment.objects.all()
            serializer = CommentSerializer(comment, many=True)
            return Response({'message':'This are all the datas','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleComment(APIView):
    def get(self,request,comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
            serializer = CommentSerializer(comment)
            return Response({'message':'This is your data','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditComment(APIView):
    def put(self,request,comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
            serializer = CommentSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'This comment has been edited'},status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteComment(APIView):
    def delete(self,request,comment_id):
        try:
            comment = Comment.objects.get(id=comment_id)
            comment.delete()
            return Response({'message':'This comment has been deleted'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class AddAuditlog(APIView):
    def post(self,request):
        try:
            serializer = AuditLogSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'This audit log has been added'},status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class GetAuditlog(APIView):
    def get(self,request):
        try:
            auditlog = AuditLog.objects.all()
            serializer = AuditLogSerializer(auditlog, many=True)
            return Response({'message':'This are all the audit log', 'data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SingleAuditlog(APIView):
    def get(self,request,auditlog_id):
        try:
            auditlog = AuditLog.objects.get(id = auditlog_id)
            serializer = AuditLogSerializer(auditlog)
            return Response({'message':'This is the audit log for this','data':serializer.data},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class EditAuditlog(APIView):
    def put(self,request,auditlog_id):
        try:
            auditlog = AuditLog.objects.get(id = auditlog_id)
            serializer = AuditLogSerializer(auditlog, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'This auditlog has been edited'},status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class DeleteAuditlog(APIView):
    def delete(self,request,auditlog_id):
        try:
            auditlog = AuditLog.objects.get(id = auditlog_id)
            auditlog.delete()
            return Response({'message':'This audit log has been deleted'},status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'message':'Internal server error','error':str(e)},status=status.HTTP_500_INTERNAL_SERVER_ERROR)































