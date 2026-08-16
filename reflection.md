1b: which change (system prompt / temperature / structured output) had the biggest effect, and why?

If you mean most visually dramatic, the pirate was probably the most fun/obvious change on screen.
If you mean most important for building real software, it's almost certainly the structured output — because it's what lets you plug the model into a program (your Pydantic detour showed exactly why: validation catches bad data). The assignment itself hints at this with its line "this is what turns a chatbot into a software component."
If you mean most surprising, maybe temperature — seeing identical-then-different runs can be the "whoa" moment.

1c: why does forcing a quote and allowing "I don't know" reduce hallucination?

what is a hallucination? It's when the model makes up something false but says it confidently. The model's natural instinct is to always produce an answer — even when it doesn't actually have one, it'll generate something plausible-sounding, because that's what it was trained to do: continue the text.

Now, the two rules each remove a reason to make things up:

Allowing "I don't know" — gives it an escape hatch.
Imagine you're a student in an exam who must write an answer for every question, blank not allowed. What do you do on a question you don't know? You bluff — write something that sounds right. That's the model hallucinating. Now change the rule: "if you don't know, you're allowed to write 'I don't know' and move on." Suddenly there's no pressure to bluff. The model can take the honest exit instead of inventing. You gave it permission to say nothing, so it stops making things up to fill the silence.

Forcing a quote — makes bluffing impossible.
Now add: "every answer must come with the exact sentence from the document that proves it." To answer, the model has to actually find supporting text and copy it. If the document doesn't contain the answer, there's no sentence to quote — so it can't fake it. The quote requirement is like showing your work in math class: you can't just write a made-up final number, you have to point at the line that supports it. If there's no line to point at, the honest move ("I can't find that") becomes the only move.

Put them together:

The quote rule says: you may only answer if you can point to proof.
The "I don't know" rule says: and if you can't point to proof, here's what to say instead.

---

Reflect — closed vs. open
You just ran both. In a sentence or two each:

Closed (OpenAI): what was easy? what did it cost you (money, data leaving your machine, rate limits)?
Open (local HF): what did you gain (privacy, no per-call cost, control)? what did you pay in (speed, quality, setup, RAM)?

closed was way faster, gave better answers, but costed money, api calls.
open was slow, but gave more privacy, undependecy. ( i heard the harware putting effort)
