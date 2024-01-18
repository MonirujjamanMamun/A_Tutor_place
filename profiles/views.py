from django.shortcuts import render, redirect
from tuitions.models import TuitionsModel, ReviewModel
from tuitions.forms import ReviewForms
from django.views.generic import DetailView
# Create your views here.


def profile(request):
    tuition = TuitionsModel.objects.all()
    return render(request, 'profile_data.html', {'tuitions': tuition})


def adminAcceptedtotuition(request, id):
    tuitions = TuitionsModel.objects.get(pk=id)
    tuitions.is_apply = False
    tuitions.tuition_types = 'Accepted'
    tuitions.save()
    return redirect('home')


class DetailPostView(DetailView):
    model = ReviewModel
    pk_url_kwarg = 'id'
    template_name = 'post_details.html'

    def post(self, request, *args, **kwargs):
        comment_form = ReviewForms(data=self.request.POST)
        post = self.get_object()
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.object  # post model er object ekhane store korlam
        comments = post.comments.all()
        comment_form = ReviewForms()

        context['comments'] = comments
        context['comment_form'] = comment_form
        return context
