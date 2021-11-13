# BeMU Patch Notes - Snapshot 1.1.4

This version brings with it many innovations. Let's start the review if you want!

# User Role System

Hmm.. let's think about it! What are roles good for? I'm not talking about the roles given to the actors on a theater stage! I'm talking about roles used to specify security, protection and privileges! Then let's take a closer look at the added role system.

+ Moderator Role

The task of this role is to ensure security on the server, and to intervene immediately in case of any adverse event.

+ Guide Role

The task of this role is to help the users who are newly registered in the system, to help them where they have difficulty by showing them the easy and short ways.

+ Immediate Maintenance Role

This role warns active users, indicating that a problem may occur in the near future and that they need to take precautions.

# New Command System

I hope you can't ask a question about what the commands are for.. ah, no, of course, we don't have to have you code js! (Looks like it's starting to make jokes, huh?) Commands are specific to officials, their main purpose is to simplify or shorten long-running tasks. Then let's examine the main commands to be added.

## +clear <number>

This command deletes the given number from the chat. Only users with Moderators and Admin roles can use this command.

Example Usage:

```
+clear 150
```

## +kick <uid> <time>

This command prohibits the given user from entering the server for the specified period of time.

Example Usage:

```
+kick rVXIDqy5gCSYhzeez5hK32FD5Uh1 15m
```

m = minutes
h = hours
d = days
y = years

## +ban <uid>

It cuts off the user's access from the server for an unlimited period of time.

Example Usage:

```
+ban rVXIDqy5gCSYhzeez5hK32FD5Uh1 "flooding"
```

(Many commands will be added soon, you can read them in macesdev guide documentation.)




