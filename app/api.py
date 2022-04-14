import falcon

import settings


def create_app() -> falcon.API:
    from . import views

    api = falcon.API()
    api.add_route("/healthz", views.HealthZ())
    api.add_route(
        f"{settings.URL_PREFIX}/payment_cards/accounts/payment_card_user_info/{{loyalty_scheme_slug}}",  # noqa
        views.PaymentCardUserInfo(),
    )
    return api
