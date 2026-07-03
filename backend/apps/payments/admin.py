from django.contrib import admin
from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id','booking','user','amount','status','gateway_transaction_id')
    list_filter = ('status',)
