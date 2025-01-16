from django.db import models

# Create your models here.
# Instagram DB
class User(models.Model):
    username = models.CharField(max_length=200, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    bio = models.TextField(null=True)
    profile_pic = models.ImageField(upload_to='users/', null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=50, null=True)


class UserFollower(models.Model):
    follower = models.ForeignKey( # Abdulloh
        User, 
        on_delete=models.CASCADE, 
        related_name="user_follower"
    )
    following = models.ForeignKey( # Jasur
        User, 
        on_delete=models.CASCADE,
        related_name="user_following"
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )


class Post(models.Model):
    poster = models.ImageField(upload_to="posters/", null=True)
    caption = models.TextField(null=True)
    tagged_users = models.ManyToManyField(User)
    location = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')


class PostContent(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.FileField(upload_to='contents/')
    order = models.IntegerField(default=1)
    

    class Meta:
        ordering = ('order',)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentator = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    gif = models.CharField(max_length=500)
    reply_to = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    top_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True)


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts_like")
    created_at = models.DateTimeField(auto_now_add=True)




# jasur = User.ojbects.create(username='Jasur01')
# kamoliddin = User.ojbects.create(username='kamoliddin02')
# asror = User.ojbects.create(username='asror003')

# asror_post = Post.objects.create(caption='Adbulloh qachon darsga kelasiz') 

# jasur_comment = Comment.objects.create(commentator=jasur, post=asror_post, text='Ertaga kelaman digandi')
# kamoliddin_comment = Comment.objects.create(
#     commentator=kamoliddin, 
#     post=asror_post, 
#     text='Bugun kelmadi',
#     reply_to=jasur_comment)

# jasur = Comment.objects.create(
#     commentator=jasur, 
#     post=asror_post, 
#     text='Meni aldabdida',
#     reply_to=kamoliddin_comment)



# # Jasurning barcha postlarining likelar sonini yig'indisi 
# jasur 

# # jasurning postlari 
# jasur_posts = Post.objects.filter(owner = jasur) # [post1, post2, post3] 

# likes_count = 0
# for jasur_post in jasur_posts:
#     likes_count += jasur_post.post_likes.count()

# print(likes_count)



# 1) bitta postga bosilgan likelar soni
# 2) Jasurning barcha postlariga yozilgan comentariyalar soni
# 3) Jasurning yozgan barcha komentariyalar soni
# 4) Jasurning eng ko'p va eng kam laykka ega posti
# 5) jasurning postlariga yozilgan eng ohirgi comment 
# 6) Eng Ko'p followerga ega bo'lgan foydalanuvchining postlar soni
# 7) Eng ko'p layk bosilgan postdagi komentariyalar soni


def orm(request):
    post = Post.objects.first()

    result = post.post_likes.count() #bitta postga bosilgan like soni


#CRUD  >>>  Cread
    # jasur = User.objects.get_or_create(
    #     username='jasur01',
    #     defaults=(
    #     email='jasur@gmail.com',
    #     posswor='1',
    #     full_name='Jasur'
    # )
    # )

# get or create




























    
    
    