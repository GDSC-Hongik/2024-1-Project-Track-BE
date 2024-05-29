from .models import post

def validate_post():
    
    posts=post.objects.all()

    for Post in posts:
        if '&' in Post.content:
            print(Post.id,'번 글에 &가 있습니다.')
            Post.content=Post.content.replace('&','')
            Post.save()
            
        if Post.dt_modified< Post.dt_modified:
            print(Post.id , '번글의 수정일이 생성일 보다 과거입니다.')
            Post.save()