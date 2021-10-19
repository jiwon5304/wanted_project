import json 

from django.http import JsonResponse
from django.views import View

from .models import Post
from users.models import User
from users.decorators import login_decorator


class PostDetailView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            author_id = request.user.id
            
            if data["subjects"] == '':
                return JsonResponse({"MESSAGE": "SUBJECTS_ERROR"}, status=400)
            
            if data["contents"] == '':
                return JsonResponse({"MESSAGE": "CONTENTS_ERROR"}, status=400)

            Post.objects.create(
                    author   = User.objects.get(id=author_id), 
                    subjects = data["subjects"],
                    contents = data["contents"],
                )
            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)
    
    def get(self, request):
        try:
            post = request.GET.get("post_id")
            post=Post.objects.get(id=post)

            result = {
                "time"     : post.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
                "subjects" : post.subjects,
                "contents" : post.contents,
                "author"   : post.author.name,
            }
            return JsonResponse({"results": result}, status=200)

        except Post.DoesNotExist:
            return JsonResponse({"MESSAGE": "POST_ERROR"}, status=404)


class PostListView(View):
    def get(self, request):
        limit = int(request.GET.get("limit",'30'))
        offset = int(request.GET.get("offset","0"))
        offset=offset*limit

        all_posts = Post.objects.all()
        posts  = all_posts[offset:offset+limit]
        
        posts_list = [{
            "time"     : post.updated_at.strftime("%Y-%m-%d %H:%M:%S"),
            "subjects" : post.subjects,
            "author"   : post.author.name,
        }for post in posts]

        result = {
            "count": len(posts_list),
            "data" : posts_list
        }
        return JsonResponse({"results": result}, status=200)


class PostUpdateView(View):
    @login_decorator
    def post(self, request):
        try:
            data = json.loads(request.body)
            post = Post.objects.get(id=data["post_id"])

            if not request.user.id == post.author.id:
                return JsonResponse({"MESSAGE": "INVALID_USER"}, status=403)

            if data["subjects"] == '':
                    return JsonResponse({"MESSAGE": "SUBJECTS_ERROR"}, status=400)
                
            if data["contents"] == '':
                return JsonResponse({"MESSAGE": "CONTENTS_ERROR"}, status=400)
            
            post.subjects = data["subjects"]
            post.contents = data["contents"]
            post.save()
            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)

        except Post.DoesNotExist:
            return JsonResponse({"MESSAGE": "POST_ERROR"}, status=404)

        except KeyError:
            return JsonResponse({"MESSAGE": "KEY_ERROR"}, status=400)


class PostDeleteView(View):
    @login_decorator
    def post(self, request,post_id):
        try:
            post = Post.objects.get(id=post_id)

            if not request.user.id == post.author.id:
                    return JsonResponse({"MESSAGE": "INVALID_USER"}, status=403)
            
            Post.objects.filter(id=post_id).delete()
            return JsonResponse({"MESSAGE": "SUCCESS"}, status=201)

        except Post.DoesNotExist:
            return JsonResponse({"MESSAGE": "POST_ERROR"}, status=404)









