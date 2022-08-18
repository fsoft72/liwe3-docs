# Payments

The payments system is implemented in a modular way, similar to the authentication system.

At the moment, only Stripe is supported, but it will be possible to add other payment providers in the future.

The payment system is achieved by using the `/api/payments/[...index].tsx` endpoint, which is a proxy to the payment provider.

In this file, you only have to edit the `callbacks` sections, defining how you want to handle the payment provider responses.