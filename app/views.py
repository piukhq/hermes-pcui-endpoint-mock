import random

import falcon
import harmonia_fixtures

from .encryption import encrypt_credentials


def user_info(fixture: harmonia_fixtures.payment_cards.TokenUserInfo) -> dict:
    return {
        "loyalty_id": fixture.loyalty_id,
        "scheme_account_id": random.randint(0, 1_000_000_000),
        "user_id": random.randint(0, 1_000_000_000),
        "credentials": encrypt_credentials(fixture.credentials),
        "card_information": {
            "first_six": fixture.card_information.first_six,
            "last_four": fixture.card_information.last_four,
            "expiry_year": fixture.card_information.expiry_year,
            "expiry_month": fixture.card_information.expiry_month,
        },
    }


class HealthZ:
    def on_get(self, req: falcon.Request, resp: falcon.Response) -> None:
        pass


class PaymentCardUserInfo:
    def on_post(
        self, req: falcon.Request, resp: falcon.Response, loyalty_scheme_slug: str
    ) -> None:
        if not req.media:
            raise falcon.HTTPBadRequest

        resp.media = {
            token: user_info(
                harmonia_fixtures.token_user_info_map[loyalty_scheme_slug][token]
            )
            for token in req.media.get("payment_cards", [])
            if token in harmonia_fixtures.token_user_info_map[loyalty_scheme_slug]
        }
