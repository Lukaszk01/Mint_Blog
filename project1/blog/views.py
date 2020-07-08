from django.shortcuts import render
# Create your views here.

posts = [
{
  'author': 'LukaszYo',
  'title':  'Master Blog',
  'content': 'first master blog post awesome!',
  'date_posted': '2020, July, 08'
},
{
  'author': 'KukasYo',
  'title':  'Normal Blog',
  'content': 'second master blog post awesome!',
  'date_posted': '2020, July, 09'
}
]


def home(request):
  context = {
    'posts': posts

  }
  return render(request, 'blog/home.html', context)

def about(request):
  return render(request, 'blog/about.html', { 'title': 'About'})
