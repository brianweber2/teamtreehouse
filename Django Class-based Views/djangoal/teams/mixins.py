from django.contrib import messages


class PageTitleMixin:
    page_title = ""
    
    def get_page_title(self):
        return self.page_title
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["page_title"] = self.get_page_title()
        return context
    
    
class SuccessMessageMixin:
    success_message = ""
    
    def get_success_message(self):
        return self.success_message
    
    def form_valid(self, form):
        messages.success(self.request, self.get_success_message())
        return super().form_valid(form)