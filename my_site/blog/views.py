from django.shortcuts import render
from datetime import date

posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "edinburgh.jpg",
        "author": "Pascal",
        "date": date(2022, 9, 18),
        "title": "Scotland Tour",
        "excerpt": "There's nothing like the views when touring in the mountains in Scotland! And I wasn't even what happened whilst I was enjoying the view!",
        "content":"""
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
                Ipsa consequatur obcaecati dolorem fuga harum molestiae 
                dignissimos architecto quasi soluta illum quam sint delectus deserunt, 
                laboriosam quisquam praesentium. Quia, corrupti excepturi.
                
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
                Ipsa consequatur obcaecati dolorem fuga harum molestiae 
                dignissimos architecto quasi soluta illum quam sint delectus deserunt, 
                laboriosam quisquam praesentium. Quia, corrupti excepturi.
                
                Lorem ipsum dolor sit amet, consectetur adipisicing elit. 
                Ipsa consequatur obcaecati dolorem fuga harum molestiae 
                dignissimos architecto quasi soluta illum quam sint delectus deserunt, 
                laboriosam quisquam praesentium. Quia, corrupti excepturi.
            """
    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Pascal",
        "date": date(2022, 3, 10),
        "title": "Programming Is Great!",
        "excerpt": "Did you ever spend hours searching that one error in your code? Yep - that's what happened to me yesterday...",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Pascal",
        "date": date(2020, 8, 5),
        "title": "Nature At Its Best",
        "excerpt": "Nature is amazing! The amount of inspiration I get when walking in nature is incredible!",
        "content": """
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
          Lorem ipsum dolor sit amet consectetur adipisicing elit. Officiis nobis
          aperiam est praesentium, quos iste consequuntur omnis exercitationem quam
          velit labore vero culpa ad mollitia? Quis architecto ipsam nemo. Odio.
        """
    }
    
]

# Create your views here.

def starting_page(request):
    return render(request, "blog/index.html")

def posts(request):
    return render(request, "blog/all-posts.html")

def post_detail(request, slug):
    return render(request, "blog/post-detail.html")