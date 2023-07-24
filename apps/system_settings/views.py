from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from .models import SystemSetting
from django.views.generic import CreateView, UpdateView
from .forms import SettingForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.decorators import  permission_required


class GeneralSettingCreate(SuccessMessageMixin, CreateView):
	model = SystemSetting
	template_name = "general/add_settings.html"
	form_class = SettingForm  # form will render to add_settings.html
	success_message = 'Record is Added Successfully'

	def get_success_url(self, **kwargs):
		return reverse_lazy('setting:add_setting')

	# form will automatically come from form_class when post request hit
	def form_valid(self, form):
		form.instance = form.save(commit=False)
		form.save()
		return super(GeneralSettingCreate, self).form_valid(form)


# class GeneralSettingUpdate(SuccessMessageMixin, UpdateView):
# 	model = Setting
# 	template_name = 'general/general_view.html'
# 	form_class = SettingForm
# 	success_message = 'Setting is Updated Successfully'

# 	# def get_success_url(self,**kwargs):
# 	#     return reverse_lazy('setting:general_setting', kwargs = {'pk':self.object.pk})

@permission_required('student_management_app.view_superadmin_home', raise_exception=True)
def GeneralSettingUpdate(request):
	setting_instance = get_object_or_404(SystemSetting, id=1)
	instance_form = SettingForm(instance = setting_instance)
 
	if request.method == 'POST':
		try:
			form = SettingForm(request.POST, request.FILES, instance=setting_instance)
			if form.is_valid():
				form.save()
				messages.success(request, 'Setting is Updated Successfully')
				return redirect('setting:general_setting')
		except:
			messages.error(request,'Failed To Update Settings')
			return redirect('setting:general_setting')
	  

	context = {'instance_form': instance_form,
            'setting_instance':setting_instance
            }
	return render(request, 'general/general_setting_view.html', context)



