from django.shortcuts import render, redirect
from RecipeProject.models import Recipe
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url="/accounts/login/")
def Create_recipe(request):

    if request.method == "POST":
        data = request.POST
        # print(data)
        recipe_name_ = data.get('recipe_name')
        recipe_details_ = data.get('recipe_details')
        recipe_image_ = request.FILES.get('recipe_image')

        Recipe.objects.create(

            recipe_name = recipe_name_,
            recipe_details = recipe_details_,
            recipe_image = recipe_image_

        )

        return redirect('recipe-list')
    
    return render(request, "RecipeProject/recipe.html")


@login_required(login_url="/accounts/login/")
def Recipe_list(request):
    query_list = Recipe.objects.all()

    if request.GET.get('search'):
        query_list = query_list.filter(recipe_name__icontains=request.GET.get('search'))

    context = {
        'recipe_list':query_list
    }
    return render(request, "RecipeProject/recipe_list.html", context)




@login_required(login_url="/accounts/login/")
def Recipe_delete(request, id):

    query_item = Recipe.objects.get(id=id)
    query_item.delete()
    return redirect('recipe-list')



@login_required(login_url="/accounts/login/")
def Recipe_update(request, id):

    query_item = Recipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST
        recipe_name_ = data.get('recipe_name')
        recipe_details_ = data.get('recipe_details')
        recipe_image_ = request.FILES.get('recipe_image')
        query_item.recipe_name = recipe_name_
        query_item.recipe_details = recipe_details_

        if recipe_image_:
            query_item.recipe_image = recipe_image_

        query_item.save()

        return redirect('recipe-list')
    

    context = {
        'recipe_list': query_item
    }

    return render(request, "RecipeProject/recipe_update.html", context)