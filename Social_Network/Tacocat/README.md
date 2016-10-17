# Tacocat Project

## The Brief

Everyone loves tacos, so let's make an app so people can show off the tacos they're eating. This will make us tons of the green stuff (aka guacamole)!

Users should be able to sign up with their email address and a password. We need to make sure they're unique, though, so don't allow multiple accounts for the same email address.

Once someone is signed up, they should be able to log in. Once logged in, be sure to give them a log out link. Can we make this menu change based on whether or not the user is logged in?

Logged in users should be able to post a new taco. For now, let's just let them type in what kind of protein they had (or maybe 'none' if they didn't have one?), whether or not they had cheese, what kind of shell they had, and any additional information. We need to be sure and link each taco to a user.

I'm sure it won't be the case for long, but if there aren't any tacos on the site, have some sort of nice message for that. Other than that, list out each taco that's been entered into the site.

Other than that, it's up to you! Do whatever you think this MVP needs!

## Bullet points:

### Users

* User accounts have an email address and a password
* User email addresses are unique
* Passwords are hashed
* Logged in users see menu items for log out and to create a taco
* Logged out users see menu items to log in or sign up

### Tacos

* Tacos have a protein, a shell, a true/false for cheese, and a freeform area for extras
* Once entered, tacos show up on the home page
* If there aren't any tacos, show a message on the home page