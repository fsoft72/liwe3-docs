# Sending emails

## Introduction

One of the most common tasks for applications is to send emails.

`LiWE3` makes it extremely easy, supporting also localization.

Before sending an email, you should check these steps:

  - Check that the SMTP configuration in `etc/config/data.json` is correct.
  - Create or edit a template inside `etc/templates/(module name)/(template name)` file.

For a complete explanation of the `LiWE3` main configuration file, where you can find SMTP keys and values, please refer to the [documentation](configuration_file.md)

In the next paragraphs, we will explain how to create a template.

## Creating an email template

As we said, email templates are stored in `etc/templates/(module name)/(template name)`.

To support localization, different templates must be created for each language you want to support.
The files must follow the following naming convention:

`(template name).(lang).html`
`(template name).(lang).txt`

Files ending with `.txt` are optional and are used to send plain text emails.

So for example, if you have a template for "Password forgot" in both Italian and English, you should create these files:

- `password_forgot.it.html`
- `password_forgot.en.html`

If you **don't** want to send localized email, you can create a file with the same name as the template, but without the language extension.

### Template creation

Template uses the common [Handlebars](https://handlebarsjs.com/) syntax.

And `handlebars` parameters  are passed inside the `args` parameter (see below).


### Template resolution

When sending an email, the system will check files in the following order:

1. (template name).(user browser language).html
2. (template name).(preferred config language).html
3. (template name).en.txt
4. (template name).txt



## Sending email by code

The `LiWE3` library has a lot of functions to send email, from low level to high level.
The one most used and recommended is `send_mail_template_locale()`  that sends an email respecting all the specifications we have described in the previous section.

The function parameters are:

- `module`: The module name (eg. `user`)
- `template`: The template name (eg. `password_forgot`)
- `language`: The language code (eg. `it`)
- `subject`: The email subject
- `args`: The email arguments
- `to`: The email recipient
- `from`: The email sender
- `cback`: (optional) The callback function to be called when the email is sent