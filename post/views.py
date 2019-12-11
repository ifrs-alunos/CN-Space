from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404, redirect 
from django.contrib.auth.decorators import login_required, permission_required
from .forms import NewTopicForm
from .forms import PostForm
from .models.board import Board
from .models.topic import Topic
from .models.postagem import Post 


@login_required
def index(request):
	boards = Board.objects.order_by('-name')
	context = {'boards': boards}
	return render(request, 'post/index.html', context)


def topics(request, board_id):
    try:
        board = get_object_or_404(Board, pk=board_id)
        context = {'board': board}
    except Board.DoesNotExist:
        raise Http404
    return render(request, 'post/topics.html', context)

def create(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    user = User.objects.first()  # TODO: get the currently logged in user
    if request.method == 'POST':
        form = NewTopicForm(request.POST)
        if form.is_valid():
            topic = form.save(commit=False)
            topic.board = board
            topic.starter = request.user
            topic.save()
            post = Post.objects.create(
                message=form.cleaned_data.get('message'),
                topic=topic,
                created_by=user
            )
            return redirect('post:board_topics', board_id)  # TODO: redirect to the created topic page
    else:
        form = NewTopicForm()
    return render(request, 'post/new_topic.html', {'board': board, 'form': form})




def posts(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    return render(request, 'post/topic_posts.html', {'topic': topic})

def reply(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.topic = topic
            post.created_by = request.user
            post.save()
            return redirect('post:topic_posts', topic_id)
    else:
        form = PostForm()
    return render(request, 'post/reply_topic.html', {'topic': topic, 'form': form})
