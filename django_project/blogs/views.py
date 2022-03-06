from django.shortcuts import render


def blogs(request):
    context= {
        'title': 'Blog1',
        'image': 'img.png'
        
        }
    return render(request, 'blog/blogs.html', context=context)
    