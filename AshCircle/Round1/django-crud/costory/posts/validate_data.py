from .models import Post


def validate_post():
    posts = Post.objects.all()
    for post in posts:
        if '&' in post.content:
            print(post.id, '번 글에 &가 있습니다.')
            post.content = post.content.replace('&', '')
            post.save()
        if post.dt_modified < post.dt_created:
            print(post.id, '번 글의 수정일이 생성일보다 과거입니다.')
            post.save()
