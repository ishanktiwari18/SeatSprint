from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .services import PaymentService
from .serializers import PaymentSerializer

class PaymentCallbackView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PaymentSerializer
    def post(self, request, payment_id):
        success = request.data.get('success', False)
        gateway_tx_id = request.data.get('gateway_tx_id', '')
        try:
            payment = PaymentService.handle_callback(payment_id=payment_id, success=success, gateway_tx_id=gateway_tx_id)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        return Response(PaymentSerializer(payment).data)
