
from django.urls import path
from django.contrib.auth import views as auth_views

from .views import (
  # login_view, 
  #                   UserRegisterView,
  #                   UserLogoutView,
  #                     ActivateView,
  #               AccountActivationSentView,
                SubscriptionView,
                SubscriptionActivateView,
                SendEmail,
                UserLogoutView,
                login_view,
                user_change_password,
                )
# from allauth.account.views import LoginView, SignupView 

app_name = 'authentication'
urlpatterns = [
    # path('login/', login_view, name="login"),
    # path('register/', UserRegisterView.as_view(), name="register"),
     path('login/', login_view, name="login"),
    # path('register/', SignupView.as_view(), name="register"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    
    # path(route='account_activation_sent/',
    #      view=AccountActivationSentView.as_view(),
    #      name='account_activation_sent'
    #      ),

    # path(route='activate/<uidb64>/<token>/',
    #      view=ActivateView.as_view(),
    #      name='activate'
    #      ), 
    
    path('user_password_change/', user_change_password, name="change_password"),
        
      #For resetting password via email follow below four link 
    path('password/reset/',auth_views.PasswordResetView.as_view(template_name = 'passwordreset/password_reset_email.html'), 
		 name = "password_reset"),
	
	path('password/reset/done/',auth_views.PasswordResetDoneView.as_view(template_name = 'passwordreset/password_reset_sent.html'), 
		 name = "password_reset_done"),
	
	path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='passwordreset/password_reset_form.html'),
		 name="password_reset_confirm"),  
	   
	 #<token> check  for valid user or not--><uidb64> user id encoded in base 64--this email is sent to the user
	 #<uidb64> helps to know user who request for password
	path('reset/complete/',auth_views.PasswordResetCompleteView.as_view(template_name='passwordreset/password_reset_complete.html'),
		 name="password_reset_complete"),
    
          path('send_message/', SendEmail.as_view(), name="email_sent"),
        path('user_subscription/', SubscriptionView.as_view(), name="user_subscription"),
        path('user_subscription/', SubscriptionView.as_view(), name="user_subscription"),
        path(route='subscription_activate/<uidb64>/<token>/',
            view=SubscriptionActivateView.as_view(),
            name='subscription_activate'
         ),

]
