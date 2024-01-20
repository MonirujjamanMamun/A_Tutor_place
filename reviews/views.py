from django.shortcuts import render
from django.views.generic import DetailView
from . models import CommentModel
from tuitions.models import TuitionsModel
from . forms import CommentForm
# Create your views here.


class DetailPostView(DetailView):
    model = TuitionsModel
    pk_url_kwarg = 'id'
    template_name = 'review_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context

    def post(self, request, *args, **kwargs):
        comment_form = CommentForm(data=self.request.POST)
        post = self.get_object()

        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.tuition = post
            new_comment.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object
        comments = post.tuitions.all()
        comment_form = CommentForm()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
