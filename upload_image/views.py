from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from upload_image.models import Images


def index(request):
    if request.method == 'POST':
        image_title = request.POST.get('title')
        image_file = request.FILES.get('fileupload')
        new_image = Images()
        new_image.title = image_title
        new_image.image = image_file
        new_image.save()
        print('Save Image %s!!!' % image_title)
        return redirect(reverse('upload_image:index'))
    images_data = Images.objects.all()
    return render(request, 'upload_image/home.html', context={'data': images_data})


def delete(request, image_id):
    print('Image ID:', image_id)
    pick_data = get_object_or_404(Images, pk=image_id)
    print('Delete image: %s' % pick_data.title)
    pick_data.delete()
    return redirect(reverse('upload_image:index'))


def update(request, image_id):
    print('Image ID:', image_id)
    pick_data = get_object_or_404(Images, pk=image_id)
    title = request.POST.get('update_title')
    image_file = request.FILES.get('update_image')
    pick_data.title = title
    pick_data.image = image_file
    # print(image_id)
    # print(title)
    # print(image_file)
    print('Update Image: %s' % pick_data.title)
    pick_data.save()
    return HttpResponseRedirect(reverse('upload_image:index'))


# 刪除使用 FileField 或是 ImageField 儲存的檔案
@receiver(post_delete, sender=Images)  # Sender is the model class name.
def post_save_image(sender, instance, *args, **kwargs):
    """ Clean Old Image file """
    try:
        instance.image.delete(save=False)  # instance.(The ImageField Name)
        # print('Remove physical image.')
    except Exception as e:
        print('Error:', e)


# 更新使用 FileField 或是 ImageField 儲存的檔案
@receiver(pre_save, sender=Images)
def pre_save_image(sender, instance, *args, **kwargs):
    """ instance old image file will delete from os """
    try:
        old_img = instance.__class__.objects.get(id=instance.id).image.path
        print(old_img)
        try:
            new_img = instance.image.path
            print(new_img)
        except:
            new_img = None
        if new_img != old_img:
            import os
            if os.path.exists(old_img):
                os.remove(old_img)
    except Exception as e:
        print('Error:', e)
