from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from orders.forms import OrderForm
from common.views import TitleMixin


# Create your views here.

class OrderCreteView(TitleMixin, CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
    success_url = reverse_lazy('orders:order_create')
    title = 'Store - Оформление заказа'

    def form_valid(self, form):
        form.instance.initiator = self.request.user
        return super(OrderCreteView, self).form_valid(form)