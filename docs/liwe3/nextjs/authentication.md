# Authentication

In `liwe3`, authentication is achieved by using the [Next-Auth Package](https://next-auth.js.org/) and the [JWT](https://jwt.io/) package.
You can work using the various authentication methods provided by Next-Auth, mainly the `Credentials` provider (which is the most flexible since you can use any authentication method you want) and the `OAuth` provider, to login using third party services, such as Google, Facebook, Twitter, etc.

## The `Credentials` Provider

The credentials provider is quite simple, since it calls the nodejs `liwe3` backend, with these keys:

- email		- the email of the user logging in
- password	- the password of the user logging in
- recaptcha - the recaptcha response (by hCaptcha)

To use the `Credentials` provider, you just need to use the provided `Login` component that will call the `liwe3` backend. If you wish to use a different GUI layout, no problems, just have a look at the `Login` component source code (which is quite simple) and you should be able to create your own.

## The `OAuth` Provider

For any OAuth provider, you need follow the steps described in the [Next-Auth documentation](https://next-auth.js.org/providers/)

When you allow users to login using an OAuth provider, you need to create a new user in the backend if the user is logging in for the first time.
This is achieved by the `NextJS` code by performing a remote call to the `liwe3` backend.
So, please, remember to configure correctly the `REMOTE_CHALLENGE` in the `.env` file.

**NOTE**: `REMOTE_CHALLENGE` needs to have the same value on both `.env` file and the `data.json/security/remote` key in the `liwe3` backend.
If this value is mismatched, the user will not be able to login.




