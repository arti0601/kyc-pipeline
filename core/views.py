from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils.timezone import now
from datetime import timedelta

from .models import User, KYCSubmission, Notification
from .state_machine import change_state


# SIMPLE AUTH (username in headers)
def get_user(request):
    username = request.headers.get("username")
    return User.objects.filter(username=username).first()


@api_view(["POST"])
def create_submission(request):
    user = get_user(request)
    if not user or user.role != "merchant":
        return Response({"error": "Unauthorized"}, status=403)

    sub = KYCSubmission.objects.create(merchant=user)
    return Response({"id": sub.id, "status": sub.status})


@api_view(["POST"])
def update_status(request, pk):
    user = get_user(request)
    sub = KYCSubmission.objects.get(id=pk)

    # AUTH CHECK
    if user.role == "merchant" and sub.merchant != user:
        return Response({"error": "Not allowed"}, status=403)

    try:
        new_status = change_state(sub.status, request.data.get("status"))
        sub.status = new_status
        sub.save()

        Notification.objects.create(
            merchant=sub.merchant,
            event_type="status_changed",
            payload={"new_status": new_status},
        )

        return Response({"status": new_status})

    except ValueError as e:
        return Response({"error": str(e)}, status=400)


@api_view(["GET"])
def reviewer_queue(request):
    user = get_user(request)
    if not user or user.role != "reviewer":
        return Response({"error": "Unauthorized"}, status=403)

    subs = KYCSubmission.objects.filter(status="submitted").order_by("created_at")

    data = []
    for s in subs:
        at_risk = (now() - s.created_at) > timedelta(hours=24)
        data.append({
            "id": s.id,
            "status": s.status,
            "at_risk": at_risk
        })

    return Response(data)