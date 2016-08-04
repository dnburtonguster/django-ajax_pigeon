from talk.models import Post
from talk.forms import PostForm
from talk.serializers import PostSerializer
from rest_framework import generics
from django.shortcuts import render


def home(request):
    tmpl_vars = {'form': PostForm()}
    return render(request, 'talk/index.html', tmpl_vars)


#########################
### class based views ###
#########################

class PostCollection(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostMember(generics.RetrieveDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    
