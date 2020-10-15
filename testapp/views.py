from django.shortcuts import render,get_object_or_404
from testapp.models import Post,Comment
from twilio.rest import Client
from .forms import CommentForm
# Create your views here.
def home_view(request):
    return render(request,'home.html')

def about_view(request):
    return render(request,'about.html')

def contact_view(request):
    return render(request,'contact.html')

def index_view(request):
    if request.method=='POST':
        name=request.POST['name']
        print(name)
    return render(request,'index.html')

def tracker_view(request):
    return render(request,'tracker.html')

def search_view(request):
    return render(request,'search.html')

def whatsapp_view(request):
     
 
    account_sid = 'AC8ac73a53275da3e4932b03796c272550' 
    auth_token = '6e06ecd2242243e2a8e7701251bb81bc' 
    client = Client(account_sid, auth_token) 
 
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='deii krish',      
                              to='whatsapp:+918675111847' 
                          ) 
 
    print(message.sid)
    
    return render(request,'whatsapp.html')

def productview_view(request,product_name):
    #post=get_object_or_404(Post,product_name=product_name)
    post=Post.objects.get(product_name=product_name)

    comments = post.comments.filter(active=True)
    csubmit=False
    # Comment posted
    if request.method == 'POST':
        form = CommentForm(data=request.POST)
        if form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            csubmit=True
    else:
        form = CommentForm()
    return render(request,'productview.html',{'product':post,'comments': comments,
                                           
                                           'form': form,
                                           })

def checkout_view(request):
    return render(request,'checkout.html')

def order_view(request):
    return render(request,'order.html')

def gold_view(request):
    product=product_model.objects.all()
    return render(request,'gold.html',{'product':product})

def silver_view(request):
    product=Post.objects.all()
    return render(request,'silver.html',{'product':product})